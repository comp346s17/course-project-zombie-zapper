from django.shortcuts import render, redirect
from itertools import chain
from django.http import HttpResponse
from cgi import urlparse
from models import Habit
from models import Comment
from django.core import serializers

# Create your views here.
def home(request):
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
    if request.method == 'GET':
        author = request.user
        category = request.GET.get('new-post-category')
        trigger = request.GET.get('trigger')
        habit = request.GET.get('habit')
        num_commitments = 0
        habit = Habit(author = author, category = category, trigger= trigger, habit = habit)
        habit.publish()
    return redirect('../', {'post_success': True})
    
def post_search(request):
    if request.method == 'GET':
        data = request.GET.get('query_string')
        a = Habit.objects.filter(trigger__contains = data)
        b = Habit.objects.filter(habit__contains = data)
        habits = a | b
        habits.order_by('-num_commitments')
        data = serializers.serialize("json", habits)
        return HttpResponse(data)

def comment(request):
    if request.method=='GET':
        ID = request.GET.get('id')
        habit = Habit.objects.filter(id=ID)[0]
        icon_html = request.GET.get('icon_html')
        category = request.GET.get('category')
        comments = Comment.objects.filter(habit = habit).order_by('-publish_date')
        return render(request, 'zz/comment_page.html', {'habit': habit, 'icon_html': icon_html, 'category': category, 'comments':comments})
        
def new_comment(request):
    if request.method == 'GET':
        comment = request.GET.get('comment')
        habit = request.GET.get('habit')
        author = request.user
        comment = Comment(comment = comment, author = author, habit = habit)
        comment.publish()
        return redirect('../', {'post_success': True})
        
        
        
        
        