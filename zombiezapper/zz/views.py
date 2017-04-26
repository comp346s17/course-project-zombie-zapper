from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Profile
from .models import Commitment
from .models import Habit
#from .forms import UserForm
from .forms import ProfileForm
from django.db.models import Q

# Create your views here.

@login_required
def home(request):
#    user = User.objects.get(user=request.user)
    commitments = Commitment.objects.filter(user=request.user).order_by('date_commited')
    return render(request, 'zz/home_page.html',{
        'commitments':commitments})

@login_required
def edit_profile(request):
    if(request.method=='POST'):
        profile_form=ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
        	profile_form.save()
        	#message.success(request, _('Your Profile was saved!'))
        	return redirect('home')
        else:
        	messages.error(request, _('Please fix errors.'))
    else:
    	profile_form = ProfileForm(instance=request.user.profile)
    	return render(request, 'zz/edit_profile.html',{'profile_form':profile_form
    	})
    