from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Profile
from .models import Commitment
from .models import Habit
from .models import Comment
from .forms import ProfileForm
from .forms import HabitForm
from django.db.models import Q
from django.shortcuts import render, redirect
from itertools import chain
from django.http import HttpResponse
from cgi import urlparse
from models import Habit
from django.core import serializers

# Create your views here.

@login_required
def home(request):
    if(request.method=='POST'):
        habit_form = HabitForm(request.POST)
        if habit_form.is_valid():
            habit = habit_form.save(commit=False)
            habit.author = request.user
            habit.save()
            return redirect('home')
    else:
        habit_form = HabitForm()
        commitments = Commitment.objects.filter(user=request.user).order_by('date_commited')
        return render(request, 'zz/home_page.html',{
        'commitments':commitments,
        'habit_form': habit_form,
        })

@login_required
def edit_profile(request):
    if(request.method=='POST'):
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
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

    return render(request, 'zz/home_page.html')

def category(request):
    categories = {
        'mental_health': 'Mental Health',
        'fitness': 'Fitness',
        'memory' : 'Memory',
        'creativity' : 'Creativity',
        'time_management' : 'Time Management',
        'other' : 'Other'
    }
    
    icon_html = {
        'mental_health': '<i class="fa fa-smile-o fa-3x" aria-hidden="true"></i>',
        'fitness': '<i class="fa fa-bicycle fa-3x" aria-hidden="true"></i>',
        'memory' : '<i class="fa fa-cogs fa-3x" aria-hidden="true"></i>',
        'creativity' : '<i class="fa fa-paint-brush fa-3x" aria-hidden="true"></i>',
        'time_management' : '<i class="fa fa-clock-o fa-3x" aria-hidden="true"></i>',
        'other' : '<i class="fa fa-ellipsis-h fa-3x" aria-hidden="true"></i>'
    }
    if request.method=='GET':
        category = request.GET.get('category')
        habits = Habit.objects.filter(category=categories[category]).order_by('-num_commitments')
        return render(request, 'zz/category_page.html', {'category': categories[category], 'habits': habits, 'icon_html': icon_html[category]})
        
def new_post(request):
    if request.method == 'POST':
        author = request.user
        category = request.GET.get('new-post-category')
        trigger = request.GET.get('trigger')
        habit = request.GET.get('habit')
        num_commitments = 0
        habit = Habit(author = author, category = category, trigger= trigger, habit = habit)
        habit.save()
        print('HABIT', habit)
    return redirect('../', {'post_success': True})

def view_habit(request, pk):
    # if request.method=='POST':
    try:
        commitment = Commitment.objects.get(pk=pk)
        habit = Habit.objects.get(pk=commitment.habit.pk)
        comments = Comment.objects.filter(habit = habit)
    except Habit.DoesNotExist, Commitment.DoesNotExist:
        print("habit not found")
        raise Http404("No match")
    return render(request, 'zz/comment_page.html', {'habit':habit, 'comments':comments})
def post_search(request):
    if request.method == 'GET':
        data = request.GET.get('query_string')
        a = Habit.objects.filter(trigger__contains = data)
        b = Habit.objects.filter(habit__contains = data)
        habits = a | b
        habits.order_by('-num_commitments')
        data = serializers.serialize("json", habits)
        #data=[]
        #for i in habits:
        #    data.append([i.trigger, i.habit, i.id])
        return HttpResponse(data)

def comment(request):
    ID = request.GET.get('id')
    habit = Habit.objects.filter(id=ID)[0]
    icon_html = request.GET.get('icon_html')
    category = request.GET.get('category')
    comments = Comment.objects.filter(habit = habit).order_by('-date_posted')
    return render(request, 'zz/comment_page.html', {'habit': habit, 'icon_html': icon_html, 'category': category, 'comments':comments})