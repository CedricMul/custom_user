from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from user_app.forms import SignInForm, CreateUserForm
from user_app.models import MyUser
from Userspace.settings import AUTH_USER_MODEL

def index(request):
    return render(request, 'index.html', {'mod': AUTH_USER_MODEL})

def login_view(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            c_user = authenticate(
                username = data.get('username'),
                password = data.get('password')
            )
            if c_user:
                login(request, c_user)
                return HttpResponseRedirect(reverse('home'))
    form = SignInForm()
    return render(request, 'form.html', {'form': form})

def create_user_view(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = MyUser.objects.create_user(
                username=data.get('username'),
                displayname=data.get('displayname'),
                password=data.get('password')
            )
            if new_user:
                login(request, new_user)
                return HttpResponseRedirect(reverse('home'))
    form = CreateUserForm()
    return render(request, 'form.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('home')
