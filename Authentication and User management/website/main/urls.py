from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('secret/',views.secret,name='secret'),
]
 