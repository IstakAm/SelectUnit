from django.urls import path
from . import views
urlpatterns = [
    path('', views.userCourses, name='courses'),
    path('create/', views.CreateCourse, name='createcourse'),
    path('<int:id>/', views.coursePage, name='singleUnit')
]