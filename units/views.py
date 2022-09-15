from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core import serializers

from .forms import CourseForm, ClassTimeForm
from .models import *
from users.models import *
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from .serializers import *


class IndexPage(TemplateView):
    def get(self, request, **kwargs):
        context = {}
        return render(request, 'index.html', context)


@login_required(login_url='login')
def CreateCourse(request):
    classtimeform = formset_factory(ClassTimeForm, extra=7, max_num=2)
    timeForm = classtimeform(request.POST)
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if timeForm.is_valid() and form.is_valid():
            course = form.save()
            course.user = request.user
            cts = []
            for j in timeForm:
                if j.cleaned_data != {}:
                    print(j.cleaned_data)
                    i = j.save()
                    cts.append(i)
            course.classTime.set(cts)
            course.save()

        return redirect('Home')

    context = {'form': form,
               'timeform': classtimeform,
               }

    return render(request, 'CreateCourse.html', context)


def userCourses(request):
    courses = request.user.course_set.all().order_by('name')

    courseData = []
    for course in courses:
        courseData.append(getCourseData(course.id))

    context = {
        'courseData': courseData,
    }
    return render(request, 'unit.html', context=context)


def checkCourseAccess(id, request):
    try:
        course = Course.objects.get(id=id)
        if request.user.id != course.user.id:
            return False
        return True
    except models.ObjectDoesNotExist as e:
        return False


def coursePage(request, course_id):
    if checkCourseAccess(course_id, request):
        course = getCourseData(course_id)
    else:
        return HttpResponse("<p>the course does not exist or you dont have the premission to access</p>")
    context = {
        'courseData': course,
    }

    return render(request, 'singleUnit.html', context=context)


