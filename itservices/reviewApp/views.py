from django.shortcuts import render
from django.db import models
from .models import Product, Review, Profile, User, Error
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.views.generic import TemplateView

def home(request):
	if request.method == 'POST':
		message = "Name: %s \r Email: %s \r Subject: %s  \r Message: %s \r" % (
			request.POST['Name'], 
			request.POST['Email'], 
			request.POST['Subject'], 
			request.POST['Message']
		)
		send_mail(
			'Contact Form',
			message,
			settings.EMAIL_HOST_USER,
			['django.reviewapp@zohomail.eu'],
			fail_silently=False
		)
		messages.success(request, f'Contact Form Sent!')
	return render(request, 'reviewApp/home.html', {'title': 'Home'})

def about(request):
	return render(request, 'reviewApp/about.html', {'title': 'About Us'})

def contact(request):
	return render(request, 'reviewApp/contact.html', {'title': 'Contact Us'})

def product(request):
	all_products = {
		'products': Product.objects.all()
	}
	return render(request, 'reviewApp/product.html', all_products)

#Products

class ProductListView(ListView):
	model = Product
	template_name = 'reviewApp/product.html'
	context_object_name = 'products'
	ordering = ['-releasedate']
	paginate_by = 3

# class ProductDetailView(DetailView):
# 	model = Product
# 	reviews = Review.objects.all()

class ProductDetailView(LoginRequiredMixin ,TemplateView):
	# template_name = 'reviewApp/test.html'
	template_name = 'reviewApp/product_detail.html'

	def get_context_data(self, **kwargs):
		prod = self.kwargs['pk']
		context = super(ProductDetailView, self).get_context_data(**kwargs)
		context['Products'] = Product.objects.filter(id=prod)
		context['Reviews'] = Review.objects.filter(product=prod)
		context['Action'] = Review.objects.filter(author=self.request.user, product=prod)
		# profile_ids = Review.objects.values_list('profile_id', flat=True)
		#profile_ids = Review.objects.filter(product=prod).values_list('profile_id', flat=True)
		#context['Profiles'] = Profile.objects.filter(id__in=profile_ids)
		return context

class ProductCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
	model = Product
	fields = ['name', 'brand', 'cost', 'category', 'releasedate', 'description', 'productphoto']
	def test_func(self):
		if self.request.user.is_superuser:
			return True
		return False

#Reviews

class ReviewListView(TemplateView):
	#model = Review
	template_name = 'reviewApp/review.html'
	#context_object_name = 'reviews'
	def get_context_data(self, **kwargs):
		context = super(ReviewListView, self).get_context_data(**kwargs)
		context['Reviews'] = Review.objects.all().order_by('-postdate')
		# product_ids = Review.objects.values_list('product_id', flat=True)
		# profile_ids = Review.objects.values_list('profile_id', flat=True)
		# context['Products'] = Product.objects.filter(id__in=product_ids)
		# context['Profiles'] = Profile.objects.filter(id__in=profile_ids)
		return context


class ReviewCreateView(LoginRequiredMixin, CreateView):
	model = Review
	fields = ['rating', 'reviewtext']
	def form_valid(self, form, **kwargs):
		form.instance.product_id = self.kwargs['pk']
		form.instance.author = self.request.user
		form.instance.profile = self.request.user.profile
		return super().form_valid(form)

class ReviewDetailView(DetailView):
	model = Review

class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Review
	fields = ['rating', 'reviewtext']
	def form_valid(self, form, **kwargs):
		form.instance.author = self.request.user
		return super().form_valid(form)
	def test_func(self):
		review = self.get_object()
		if self.request.user == review.author:
			return True
		return False

class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Review
	success_url = '/product'
	def test_func(self):
		review = self.get_object()
		if self.request.user == review.author:
			return True
		return False

# Errors

class ErrorListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
	model = Error
	template_name = 'reviewApp/error.html'
	context_object_name = 'errors'
	ordering = ['-reportdate']
	paginate_by = 3
	def test_func(self):
		if self.request.user.is_superuser:
			return True
		return False

class ErrorCreateView(CreateView):
	model = Error
	fields = ['type', 'page', 'description']
	