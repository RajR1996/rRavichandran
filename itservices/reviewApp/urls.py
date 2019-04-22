from django.urls import path
from . import views
from .views import ProductListView, ProductDetailView, ProductCreateView, ReviewCreateView, ReviewUpdateView, ReviewDetailView, ReviewListView


urlpatterns = [
	path('', views.home, name='reviewApp-home'),
	path('about/', views.about, name='reviewApp-about'),
	path('contact/', views.contact, name='reviewApp-contact'),	
	#path('product/', views.product, name='reviewApp-product'),
	path('product/', ProductListView.as_view(), name='reviewApp-product'),
	path('product/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
	path('product/new/', ProductCreateView.as_view(), name='product-create'),
	path('review/new/<int:pk>', ReviewCreateView.as_view(), name='review-create'),
	path('review/<int:pk>', ReviewDetailView.as_view(), name='review-detail'),
	path('review/<int:pk>/update', ReviewUpdateView.as_view(), name='review-update'),
	path('review/', ReviewListView.as_view(), name='reviewApp-review'),
]