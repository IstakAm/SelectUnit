from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
# Create your views here.
from users.forms import CreateUserForm, CourseStackForm
from users.models import UserProfile
from django.contrib.auth import authenticate, login, logout


@login_required(login_url='login')
def homePage(request):
    context = {}
    return render(request, 'index.html', context)


def registerUser(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            u = UserProfile(user=User.objects.get(username=username))
            u.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.info(request, 'Your username or your password is wrong')

    context = {}
    return render(request, 'login.html', context)


def logOutUser(request):
    logout(request)
    return redirect('login')


def createCourseStack(request):
    form = CourseStackForm()
    if request.method == 'POST':
        form = CourseStackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'courseStack.html', context=context)
