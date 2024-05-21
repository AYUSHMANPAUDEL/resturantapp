from django.shortcuts import render , HttpResponse , redirect

# Create your views here.

def sui(request):
    return redirect("home/")
def home(request):
    return render(request,"login.html")

def dashboard(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print (username , password)

    return HttpResponse("timro response hami vatha ai sako")