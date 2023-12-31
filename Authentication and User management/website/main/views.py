from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    count=User.objects.count()
    return render(request,'main/home.html', {
        'count':count
    })
@login_required    
def secret(request):
    return render(request,'main/secret.html')

def signup(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })
    
