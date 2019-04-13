from django.shortcuts import render

def home(request):
	return render(request, 'reviewApp/home.html', {'title': 'Home'})

def about(request):
	return render(request, 'reviewApp/about.html', {'title': 'About Us'})

def contact(request):
	return render(request, 'reviewApp/contact.html', {'title': 'Contact Us'})

def product(request):
	all_products = {
		'products': products
	}
	return render(request, 'reviewApp/product.html', all_products)