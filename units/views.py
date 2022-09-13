from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import CourseForm, ClassTimeForm
from .models import *
from users.models import *
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


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
        if timeForm.is_valid():
            print("shash1")
            if form.is_valid():
                print("shash 2")
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
            else:
                print(form.errors)
        else:
            print(timeForm.errors)

    context = {'form': form,
               'timeform': classtimeform,
               }

    return render(request, 'CreateCourse.html', context)


def userCourses(request):
    courses = request.user.course_set.all().order_by('name')
    classtime = request.user.course_set
    courseData = []
    for course in courses:
        classtimes = ClassTime.objects.get(id = course.classTime.)
        print(classtimes)
        courseData.append({
            'name': course.name,
            'code': course.code,
            'capacity': course.capacity,
            'filled': course.filled,
            'units': course.units,
            'master': course.master,
            'exam_date': course.exam_date,
            'exam_hour': course.exam_hour,
            'place': course.place,
            'classTime': classtimes,
            'coeducational': course.coeducational,
        })

    context = {
        'courseData': courseData,
    }
    return render(request, 'unit.html', context=context)
