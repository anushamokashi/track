from .models import userprofile
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class UserProfileForm(forms.ModelForm):

	class Meta:
		model=userprofile
		fields='__all__'
