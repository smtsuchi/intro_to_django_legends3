from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact_coding_summit/', views.contact_us, name='x'),
    path('posts/create/', views.createPost, name='y'),
    path('signup/', views.signMeUp, name='signup'),
    path('login/', views.logMeIn, name='login'),
    path('logout/', views.logMeOut, name='logout'),
]
