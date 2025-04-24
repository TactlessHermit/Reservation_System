from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import UserRegistrationForm


# Create your views here.
def register_user(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            #Set username (to email) and password from form data
            new_user.username = form.cleaned_data['email']
            new_user.set_password(form.cleaned_data['password2'])
            new_user.save()

            # Log in user and redirect to 'My Page'
            email = form.cleaned_data['email']
            password = form.cleaned_data['password2']
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Registered successfully. Welcome.")
                return redirect(reverse('user:profile'))
            else:
                #THIS SHOULD NOT HAPPEN
                messages.error(request, "User not found. Issue with registration.")

        else:
            messages.success(request, "Invalid form input.")

    form = UserRegistrationForm()
    template_name = 'users/registration/create_user.html'
    context = {
        'form': form
    }
    return render(request, template_name, context)

def login_user(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful. Welcome.")
            return redirect(reverse('user:profile'))
        else:
            messages.error(request, "User not found.")

    return render(request, 'users/registration/login.html')

def logout_user(request):
    logout(request)

    return redirect(reverse('user:home'))

def homepage(request):
    return render(request, 'users/webpages/home.html')

def user_profile(request):
    return render(request, 'users/webpages/profile.html')

def update_user(request):
    pass

def delete_user(request):
    pass