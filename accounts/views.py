from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import render, redirect
from django.urls import reverse
from accounts.forms import CustomUserCreationForm, validate_phone_number, CustomUserChangeForm
from accounts.models import CustomUser


# Create your views here.
def homepage(request):
    """
        Renders homepage of website
    """
    return render(request, 'accounts/webpages/home.html')

def new_account(request):
    """
        Creates an account for a new user using form input
    """
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
    """
        Renders profile page of current user (if registered)
    """
    return render(request, 'accounts/webpages/account_profile.html')

def login_account(request):
    """
        Logs into account with given credentials
    """
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Verifies inputted account credentials. Logs in if valid
        user = authenticate(request, username = email, password = password)
        if user is not None:
            login(request, user)
            return redirect(reverse('accounts:profile'))
        else:
            messages.warning(request, 'User Not Found!')

    return render(request,'accounts/registration/login.html')

def logout_account(request):
    """
        Logs out of current user's account
    """
    logout(request)
    return redirect(reverse('accounts:home'))

def update_account(request):

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            # Save updated user
            form.save()
            # Redirect to user profile page
            return redirect(reverse("accounts:profile"))

    else:
        form = CustomUserChangeForm(instance=request.user)

    return render(request, 'accounts/registration/update_account.html', {'form': form})

def delete_account(request, pk):
    """
        Deletes the current user's account
    """
    try:
        user = CustomUser.objects.get(id = pk)
        user.delete()
        messages.success(request, "Successfully deleted account.")
        return redirect(reverse('accounts:home'))
    except Exception as e:
        if hasattr(e, "message"):
            error_msg = e.message
        else:
            error_msg = e
        messages.error(request, error_msg)
        return redirect(reverse('accounts:profile'))

class PasswordReset(PasswordResetView):
    pass