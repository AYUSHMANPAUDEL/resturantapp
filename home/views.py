from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Sample data for demonstration
menu_data = {
    'pizza': [
        {'name': 'Margherita', 'price': '$10'},
        {'name': 'Pepperoni', 'price': '$12'},
        {'name': 'Veggie', 'price': '$11'}
    ],
    'momo': [
        {'name': 'Chicken Momo', 'price': '$8'},
        {'name': 'Veg Momo', 'price': '$7'}
    ],
    'drinks': [
        {'name': 'Coke', 'price': '$2'},
        {'name': 'Pepsi', 'price': '$2'},
        {'name': 'Lemonade', 'price': '$3'}
    ],
    'burger': [
        {'name': 'Cheeseburger', 'price': '$9'},
        {'name': 'Veggie Burger', 'price': '$8'}
    ],
    'others': [
        {'name': 'Fries', 'price': '$3'},
        {'name': 'Onion Rings', 'price': '$4'}
    ]
}

def sui(request):
    return redirect("home/")

def home(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard/")
        
    if request.user.is_authenticated:
        return redirect("dashboard/")
    return render(request, "login.html")

@login_required
def dashboard(request):
    rows = 3
    columns = 5
    return render(request, "dashboard.html", {'rows': rows, 'columns': columns})
    

@login_required
def get_menu_items(request, item_type):
    items = menu_data.get(item_type, [])
    return JsonResponse({'items': items})

@login_required
def add_to_session(request):
    item = request.POST.get('item')
    if 'cart' not in request.session:
        request.session['cart'] = []
    request.session['cart'].append(item)
    request.session.modified = True
    return JsonResponse({'status': 'success'})

def chef_page(request):
    return render(request,"chef.html")