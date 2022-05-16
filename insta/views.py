from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('Testing!! hello world')
    # dummy code, mimicking a database
    posts = [
        {
            'author': "Shoha",
            'caption': 'THIS IS MY BIKE',
            'img_url': 'https://media.wired.com/photos/61afb905d184762c75e00411/master/pass/Gear-Jackbrabbit-Bike-Yellow-top.jpg'
        }
        ,
        {
            'author': "Frankie",
            'caption': 'Its spring',
            'img_url': 'https://www.lovethispic.com/uploaded_images/85888-Spring-Landscape.jpg'
        }
        ]

    context = {'posts':posts}
    return render(request, 'insta/homepage.html', context=context)

def about(request):
    return render(request, 'insta/about.html' , context={})

def contact_us(request):
    return render(request, 'insta/contact_us.html')