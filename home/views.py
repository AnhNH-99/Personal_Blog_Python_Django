from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/admin')
        else:
            return render(request, 'pages/home.html')
    return render(request, 'pages/home.html')
