from django.shortcuts import render, redirect
from django.http import HttpResponse

# import all of your models
from .models import Post

# import all of your forms
from .forms import PostForm, CreateUserForm

# import extra functionality here
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# import mail dependencies
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

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

@login_required(login_url='login')
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
    if request.user.is_authenticated:
        return redirect('home')
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account was successfully created for {user}')

            recipient = form.cleaned_data.get('email')
            template = render_to_string('insta/emailtemplate.html', {'username': user})
            email_msg = EmailMessage(
                'Welcome to my Django Finstagram!', #subject line
                template, #body
                settings.EMAIL_HOST_USER, #sender
                [recipient] #list of recipients
            )
            email_msg.fail_silently = False
            email_msg.send()
            


            return redirect('login')
        else:
            messages.warning(request, 'Invalid attempt. Please try again')
            print('INVALID! :(', form.errors)
    else:
        print('GET req submitted', request.method)   
    return render(request, 'insta/signup.html', context={'form': form})

def logMeIn(request):    
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')

        user = authenticate(request, username=username, password = password1)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome, {username}!')
            return redirect('home')
        else:
            messages.warning(request, f'Incorrect username/password. Please try again.')
    return render(request, 'insta/login.html', context={})


def logMeOut(request):
    logout(request)
    return redirect('login')