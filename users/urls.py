from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logOutUser, name='logout'),
    path('coursestack/', views.createCourseStack, name='courseStack'),
]