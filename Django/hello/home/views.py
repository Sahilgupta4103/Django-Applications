from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.contrib import messages

def index(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse("this is about page")

def services(request):
    return HttpResponse("this is services page")

def contact(request):
    if request.method == "POST":
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        new_contact = Contact(email=email, phone=phone)
        if (new_contact.save()):
            messages.success(request, "Details Saved.")
    return render(request,'contact.html')

