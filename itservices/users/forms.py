from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Row, Submit, Button, Column

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	address = forms.CharField()
	dob = forms.DateField(
		widget=forms.TextInput(
			attrs={'type': 'date'}
		), label='Date of Birth'
	)
	helper = FormHelper()
	helper.layout = Layout(
		Div(
			Div('fullname', css_class='col-md-6',),
			Div('dob', css_class='col-md-6',),
			css_class='row',
		),
		Div(
			Div('address', css_class='col-md-6',),
			Div('city', css_class='col-md-6',),
			css_class='row',
		),
		Div(
			Div('country', css_class='col-md-6',),
			Div('profilephoto', css_class='col-md-6',),
			css_class='row',
		),
	)
	class Meta:
		model = Profile
		fields = ['fullname', 'dob', 'address', 'city', 'country', 'profilephoto']
		labels = {
			'fullname': 'Full Name',
			'address': 'Address',
			'city': 'City',
			'country': 'Country',
			'profilephoto': 'Profile Photo',
		}