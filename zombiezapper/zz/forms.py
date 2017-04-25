from django import forms
from .models import Profile
from .models import Habit

class UserForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('statement',)