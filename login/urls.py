from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name = 'index'),
    path('login', views.login_view, name='login'),
    path('signup', views.signup_view, name='signup'),
    path('saved', views.get_saved_regex_view, name='saved'),
    path('getusername', views.get_username_view, name="username"),
    path('saveregex', views.save_regex_view, name="saveregex"),
    path('delete', views.delete_saved_regex, name="deleteregex")
]
