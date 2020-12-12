from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Application
from .models import Password
from .forms import DetailsForm
from cryptography.fernet import Fernet
# Create your views here.

def Home(request):
    return render(request, 'SafePassword/home.html/')

def AddNew(request):

    if request.method == "POST":
        form = DetailsForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            form1 = Application(name=name)
            
            try:
                form1.save()
                aid = Application.objects.get(name=name)
                key = generate_key()
                print("key",key)
                encoded_username = encode(username,key)
                print("u",encoded_username)
                encoded_password = encode(password,key)
                print("p",encoded_password)
                form2 = Password(application=aid,key=key,username=encoded_username,password=encoded_password)
                form2.save()
            except:
                print("error")
            

    form = DetailsForm()

    return render(request, 'SafePassword/add.html/',{'form': form})

def Retrive(request):

    all_application = Application.objects.all()
    context={
         'all_application': all_application
    }
    return render(request, 'SafePassword/retrive.html/',context)

def Show(request,aid):
    details = Password.objects.get(application=aid)
    username = decode(details.username, details.key)
    password = decode(details.password, details.key)
    application = Application.objects.get(id=aid)
    context={
        'username': username,
        'password': password,
        'application': application
    }
    return render(request, 'SafePassword/details.html/',context)


def generate_key():
    k = Fernet.generate_key()
    key = k.decode("utf-8")
    return key

def encode(text, k):
    
    key = k.encode("utf-8")
    Btext = text.encode("utf-8")
    cipher_suite = Fernet(key)
    Bencoded_text = cipher_suite.encrypt(Btext)
    encoded_text = Bencoded_text.decode("utf-8")

    return encoded_text

def decode(text, k):

    key = k.encode("utf-8")
    Btext = text.encode("utf-8")
    cipher_suite = Fernet(key)
    Bdecoded_text = cipher_suite.decrypt(Btext)
    decoded_text = Bdecoded_text.decode("utf-8")

    return decoded_text
