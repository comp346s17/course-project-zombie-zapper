from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'zz/home_page.html')