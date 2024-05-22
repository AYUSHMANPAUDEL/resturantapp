from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.

def sui(request):
    return redirect("home/")
def home(request):
    if request.user is authenticate:
        return render("dashboard/")
    return render(request,"login.html")

def dashboard(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            rows = 3
            columns = 5
            return render(request, "dashboard.html", {'rows': rows, 'columns': columns})
        else:
            return redirect("home/")
    return HttpResponse("timro response hami vatha ai sako")