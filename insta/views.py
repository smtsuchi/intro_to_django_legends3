from django.shortcuts import render, redirect
from django.http import HttpResponse

# import all of your models
from .models import Post

# import all of your forms
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm

# import extra functionality here
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):

    posts = Post.objects.all()
    print(posts)

    context = {'posts':posts}
    
    return render(request, 'insta/homepage.html', context=context)

def about(request):
    return render(request, 'insta/about.html' , context={})

def contact_us(request):
    return render(request, 'insta/contact_us.html')

def createPost(request):
    form = PostForm()
    if request.method == "POST":
        print('POST req submitted')
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('INVALID! :(')
    else:
        print('GET req submitted', request.method)   

    return render(request, 'insta/createpost.html', context = {'z': form})

def signMeUp(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print('INVALID! :(', form.errors)
    else:
        print('GET req submitted', request.method)   
    return render(request, 'insta/signup.html', context={'form': form})

def logMeIn(request):       
    if request.method == "POST":
        print(request.POST)
        username = request.POST.get('username')
        password1 = request.POST.get('password1')

        user = authenticate(request, username=username, password = password1)

        if user is not None:
            login(request, user)
            print(f'{user} is looged in!')
            return redirect('home')
        else:
            print('incoreect username/password')
    return render(request, 'insta/login.html', context={})


def logMeOut(request):
    logout(request)
    return redirect('login')