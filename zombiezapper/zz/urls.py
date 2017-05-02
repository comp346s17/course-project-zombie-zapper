from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^edit_profile/', views.edit_profile, name='edit_profile'),
    url(r'^category/$', views.category),
    url(r'^uncommit/(?P<pk>\d+)/$', views.uncommit, name='uncommit'),
    url(r'^post_search', views.post_search),
    url(r'^post/(?P<pk>\d+)/', views.view_habit, name='view_habit'),
    url(r'^signup/$', views.signup, name='signup'),
    #url(r'^login/$', auth_views.login, {'template_name': 'zz/login.html'}, name='login'),
]