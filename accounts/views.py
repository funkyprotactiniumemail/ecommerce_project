from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile

# SIGNUP VIEW
def signup_view(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        UserProfile.objects.create(user=user)
        login(request, user)
        return redirect('products:product_list')
    return render(request, 'accounts/signup.html', {'form': form})

# LOGIN VIEW
def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('products:product_list')
    return render(request, 'accounts/login.html', {'form': form})

# LOGOUT VIEW
def logout_view(request):
    logout(request)
    return redirect('accounts:login')

# PROFILE VIEW
@login_required  
def profile_view(request):
    return render(request, 'accounts/profile.html', {'user': request.user})

# PROFILE EDIT VIEW
@login_required
def profile_edit(request):
    profile = request.user.userprofile
    if request.method == 'POST':
        profile.bio = request.POST.get('bio')
        profile.save()
        return redirect('accounts:profile')
    return render(request, 'accounts/profile_edit.html', {'profile': profile})
