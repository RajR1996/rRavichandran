from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='reviewApp-home'),
	path('about/', views.about, name='reviewApp-about'),
	path('contact/', views.contact, name='reviewApp-contact'),	
	path('product/', views.product, name='reviewApp-product'),	
]