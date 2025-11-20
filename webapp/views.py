from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # redirect to some page
    else:
        form = UserCreationForm()
    return render(request, 'webapp/signup.html', {'form': form})

from django.shortcuts import render

def home_view(request):
    return render(request, 'webapp/home.html')
