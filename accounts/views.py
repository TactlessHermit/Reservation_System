from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse
from accounts.forms import CustomUserCreationForm


# Create your views here.
def homepage(request):
    return render(request, 'accounts/webpages/home.html')

def new_account(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            # Save new user
            user = form.save()
            # Login new user
            login(request, user)
            return redirect(reverse('accounts:home'))

        else:
            messages.warning(request, "Registration failed. Big Sad.")

    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/registration/create_account.html', {'form': form})

def account_page(request):
    return render(request, 'accounts/webpages/account_profile.html')

def login_account(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username = email, password = password)

        if user is not None:
            login(request, user)
            return redirect(reverse('accounts:profile'))
        else:
            messages.warning(request, 'User Not Found!')

    return render(request,'accounts/registration/login.html')

def logout_account(request):
    logout(request)
    return redirect(reverse('accounts:home'))

def update_account(request):
    pass

def delete_account(request):
    pass