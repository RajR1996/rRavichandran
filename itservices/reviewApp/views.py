from django.shortcuts import render
from django.db import models
from .models import Product, Review, Profile, User
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
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

class ProductListView(ListView):
	model = Product
	template_name = 'reviewApp/product.html'
	context_object_name = 'products'
	ordering = ['-releasedate']

# class ProductDetailView(DetailView):
# 	model = Product
# 	reviews = Review.objects.all()

class ProductDetailView(TemplateView):
	# template_name = 'reviewApp/test.html'
	template_name = 'reviewApp/product_detail.html'
	def get_context_data(self, **kwargs):
		prod = self.kwargs['pk']
		context = super(ProductDetailView, self).get_context_data(**kwargs)
		context['Products'] = Product.objects.filter(id=prod)
		context['Reviews'] = Review.objects.filter(product=prod)
		profile_ids = Review.objects.values_list('profile_id', flat=True)
		context['Profiles'] = Profile.objects.filter(id__in=profile_ids)
		return context

class ReviewListView(ListView):
	model = Review
	template_name = 'reviewApp/review.html'
	context_object_name = 'reviews'

class ProductCreateView(CreateView):
	model = Product
	fields = ['name', 'brand', 'cost', 'category', 'releasedate', 'description', 'productphoto']

class ReviewCreateView(LoginRequiredMixin, CreateView):
	model = Review
	fields = ['product', 'profile', 'author', 'rating', 'reviewtext']
	#fields = ['rating', 'reviewtext']
	def testfunc(self):
		if self.request.user == review.author:
			return True
		return False

class ReviewDetailView(DetailView):
	model = Review
		
	
		