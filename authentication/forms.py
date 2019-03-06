from .models import userprofile
from django.contrib.auth.forms import AuthenticationForm


class UserProfileForm(forms.ModelForm):

	class Meta:
		model=userprofile
		fields='__all__'
