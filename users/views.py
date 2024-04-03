from django.shortcuts import render

# Create your views here.
def login(request):
    context = {
        'title': 'Home - авторизация'
    }
    return render(request, 'users/login.html', context)

def registration(request):
    context = {
        'title': 'Home - авторизация'
    }
    return render(request, 'users/registration.html', context)

def profile(request):
    context = {
        'title': 'Home - авторизация'
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    context = {
        'title': 'Home - авторизация'
    }
    return render(request, '', context)
