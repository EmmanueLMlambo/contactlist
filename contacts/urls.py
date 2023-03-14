from django.urls import path
from django.shortcuts import render
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add-contact/', views.addContact, name='add-contact'),
    path('profile/<str:pk>', views.contactProfile, name='profile'),
    path('edit-contact/<str:pk>', views.editContact, name='edit-contact'),
]

def contactProfile(request, pk):
    return render(request, 'contact-profile.html')