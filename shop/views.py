from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact,Index

def index(request):
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        print(name,email,phone,desc)
        index = Index(name=name, email=email, phone=phone, desc=desc)
        index.save()
        thank = True
    return render(request,'shop/index.html',{'thank':thank})

def about(request):
    return render(request,'shop/about.html')
def contact(request):
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'shop/contact.html',{'thank':thank})

def search(request):
    return render(request,'shop/search.html')



# def contact1(request):
#     thank = False
#     if request.method=="POST":
#         name = request.POST.get('name', '')
#         email = request.POST.get('email', '')
#         phone = request.POST.get('phone', '')
#         desc = request.POST.get('desc', '')
#         contact = Contact(name=name, email=email, phone=phone, desc=desc)
#         contact.save()
#         thank = True
#     return render(request, 'shop/index.html',{'thank':thank})