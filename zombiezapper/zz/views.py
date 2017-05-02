from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Profile
from .models import Commitment
from .models import Habit
from .models import Comment
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm
from .forms import HabitForm
from .forms import CommentForm
from django.db.models import Q
from django.shortcuts import render, redirect
from itertools import chain
from django.http import HttpResponse
from cgi import urlparse
from models import Habit
from models import Comment
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

def uncommit(request, pk):
    Commitment.objects.filter(pk=pk).delete()
    return redirect('home')


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
        
# def new_post(request):
#     if request.method == 'POST':
#         author = request.user
#         category = request.GET.get('new-post-category')
#         trigger = request.GET.get('trigger')
#         habit = request.GET.get('habit')
#         num_commitments = 0
#         habit = Habit(author = author, category = category, trigger= trigger, habit = habit)
#         habit.publish()
#     return redirect('../', {'post_success': True})

# def new_comment(request):
#     if request.method ==
def view_habit(request, pk):
    if request.method=='POST': #if comment is posted
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.poster = request.user
            #Commitment = Commitment.objects.get(pk=pk)
            comment.habit = Habit.objects.get(pk=pk)
            comment.date_posted = timezone.now()
            comment.save()

            comments = Comment.objects.filter(habit=comment.habit)
            #return redirect('views_habit', {'habit':comment.habit, 'comments':comments, 'comment_form':comment_form})
            return redirect('view_habit', pk)
    else:
        try:
#            commitment = Commitment.objects.get(pk=pk)
            habit = Habit.objects.get(pk=pk)
            category = habit.category
            comments = Comment.objects.filter(habit = habit)

        except Habit.DoesNotExist, Commitment.DoesNotExist:
            print("habit not found")
            raise Http404("No match")
        comment_form = CommentForm()
        return render(request, 'zz/comment_page.html', {'habit':habit, 'comments':comments, 'comment_form':comment_form})

def view_habit_from_category(request, pk):
    # if request.method=='POST':
    try:
        habit = Habit.objects.get(pk=pk)
        comments = Comment.objects.filter(habit = habit)
    except Habit.DoesNotExist, Commitment.DoesNotExist:
        print("habit not found")
        raise Http404("No match")
    return render(request, 'zz/comment_page.html', {'habit':habit, 'comments':comments, 'category': category})
def post_search(request):
    if request.method == 'GET':
        data = request.GET.get('query_string')
        a = Habit.objects.filter(trigger__contains = data)
        b = Habit.objects.filter(habit__contains = data)
        habits = a | b
        habits.order_by('-num_commitments')
        data = serializers.serialize("json", habits)
        return HttpResponse(data)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'zz/signup.html', {'form':form})
    
def comment(request):
    ID = request.GET.get('id')
    habit = Habit.objects.filter(id=ID)[0]
    icon_html = request.GET.get('icon_html')
    category = request.GET.get('category')
    comments = Comment.objects.filter(habit = habit).order_by('-date_posted')
    return render(request, 'zz/comment_page.html', {'habit': habit, 'icon_html': icon_html, 'category': category, 'comments':comments})
