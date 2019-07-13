from django.shortcuts import render, redirect
from users.models import User
from django.contrib import auth


def signup(request):
    if request.method == 'POST':
        if request.POST['user_password'] != request.POST['user_password1']:
            return render(request, 'signup.html', {'password_error': 'you\'re passwords don\'t match'})
        try:
            User.objects.get(email=request.POST['user_email'])
            return render(request, 'signup.html', {'account_error': 'ERROR: user already exists try again'})
        except User.DoesNotExist:
            user = User.objects.create_user(request.POST['user_email'], request.POST['first_name'],
                                            request.POST['last_name'], request.POST['user_password'])
            auth.login(request, user)
            return redirect('login')
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(email=request.POST['user_email'], password=request.POST['user_password'])
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'account_error': 'something went wrong with your password or email'})
    return render(request, 'login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')


def profile(request):
    return render(request, 'profile.html')
