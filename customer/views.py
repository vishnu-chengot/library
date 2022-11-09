from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'customer/home.html')

def login(request):
    return render(request,'customer/login.html')


def bookshelf(request):
    return render(request,'customer/bookshelf.html')

def audiobook(request):
    return render(request,'customer/audiobook.html')   


def contact(request):
    return render(request,'customer/contact.html')
