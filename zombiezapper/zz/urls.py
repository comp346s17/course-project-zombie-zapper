from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^category/$', views.category),
    url(r'^new_post', views.new_post),
    url(r'^post_search', views.post_search),
    url(r'^comment/$', views.comment)
    #url(r'^login/$', auth_views.login, {'template_name': 'messenger/login.html'}, name='login'),
    #url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    #url(r'^signup/$', views.signup, name='signup'),
    #url(r'^message/$', views.message, name='message'),
]