from django.shortcuts import render, redirect
from .models import Contacts
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')


def home(request):
    contacts = Contacts.objects.all()
    search_input = request.GET.get('search-area')
    if search_input:
        contacts = Contacts.objects.filter(Q(full_name__icontains=search_input) | Q(department__icontains=search_input)).order_by('full_name')
    else:
        contacts = Contacts.objects.all().order_by('full_name')
        search_input = ''
    return render(request, 'home.html', {'contacts':contacts, 'search_input': search_input }, )


def addContact(request):
    if request.method == 'POST':
        new_contact = Contacts(
            full_name = request.POST['fullname'],
            department = request.POST['department'],
            email = request.POST['email'],
            cell_number = request.POST['cell-number'],
            land_number = request.POST['land-number'],
            location = request.POST['location']
        )
        new_contact.save()
        return redirect ('/')

    return render(request, 'new.html')

def contactProfile(request, pk ):
    contact = Contacts.objects.get(id=pk)
    return render(request, 'contact-profile.html ', {'contact' : contact})

def editContact(request, pk):
    contact = Contacts.objects.get(id=pk)

    if request.method == 'POST':


        contact.full_name = request.POST['fullname']
        contact.department = request.POST['department']
        contact.email = request.POST['email']
        contact.cell_number = request.POST['cell-number']
        contact.land_number = request.POST['land-number']
        contact.location = request.POST['location']
        contact.save()

        return redirect('/profile/'+str(contact.id))

    return render(request, 'edit.html', {'contact' : contact})

