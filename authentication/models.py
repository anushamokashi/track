from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel



# Create your models here.

class userprofile(TimeStampedModel, models.Model):
	firstname=models.CharField(max_length=200)
	lastname = models.CharField(max_length=200)
	email =models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	confirmpassword=models.CharField(max_length=200)
	phnno=models.BigIntegerField()


	def __str__(self):
		return self.email
