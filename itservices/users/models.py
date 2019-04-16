from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	fullname = models.CharField(max_length=100, null=True)
	dob = models.DateField(null=True)
	address = models.TextField(null=True)
	city = models.CharField(max_length=100, null=True)
	profilephoto = models.ImageField(default='profiles/default_profile.jpg', upload_to='profiles')

def __str__(self):
	return f'Profile for {self.user.username}'