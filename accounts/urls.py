from django.urls import path
from . import views

urlpatterns = [
    path('',views.signup, name= 'signup'),
    path('r^login/$',views.login_f, name='login')
]