from django import forms
from .models import YourProfile

class ProfileForm(forms.ModelForm):

	class Meta:
		model = YourProfile
		fields = ['user_pic', 'user_title', 'about_user']


