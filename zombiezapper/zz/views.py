from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from .models import User
from .forms import UserForm
from django.db.models import Q

# Create your views here.

@login_required
def home(request):
#    user = User.objects.get(user=request.user)

    return render(request, 'zz/home_page.html')

@login_required
def edit_profile(request):
#     try:
#         user = User.objects.get(request.user)
#         print(user.statement)
#     except User.DoesNotExist:
#         raise Http404("No user")
#     if(request.method=='POST'):
#         user=UserForm(request.POST, instance=user)
# # 		user = User.objects.get(request.user)
# # 		print(user.statement)
#         return render(request, 'zz/edit_profile.html')
#     else:
#         return render(request, 'zz/edit_profile.html',{'user':user})
    return render(request, 'zz/edit_profile.html')