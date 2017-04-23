from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'site/home_page.html')