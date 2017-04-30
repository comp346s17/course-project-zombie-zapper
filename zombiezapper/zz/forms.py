from django import forms
from .models import Profile
from .models import Habit
from django.contrib.auth.models import User

# class UserForm(forms.ModelForm):
# 	class Meta:
# 		model = User
# 		fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('statement',)


class HabitForm(forms.ModelForm):
	class Meta:
		model = Habit
		fields = ('trigger', 'habit', 'category')

