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


def getCourseData(id):
    course = Course.objects.get(id=id)
    classTimesDict = []
    for classtime in course.classTime.all():
        classTimesDict.append({
            'from_hour': classtime.from_hour,
            'to_hour': classtime.to_hour,
            'day': classtime.get_day_display(),
        })

    courseDict = {'name': course.name, 'code': course.code, 'capacity': course.capacity, 'filled': course.filled,
                  'units': course.units, 'master': course.master, 'exam_date': course.exam_date,
                  'exam_hour': course.exam_hour, 'place': course.place, 'coeducational': course.coeducational,
                  'classTimes': classTimesDict}
    return courseDict


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

def coursePage(request, id):
    if checkCourseAccess(id, request):
        course = getCourseData(id)
    else:
        return HttpResponse("<p>the course does not exist or you dont have the premission to access</p>")
    context = {
        'courseData': course,
    }

    return render(request, 'singleUnit.html', context=context)
