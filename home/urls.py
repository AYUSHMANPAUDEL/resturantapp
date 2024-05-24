from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('chef/', views.chef_page, name='chef_page'),
    path('get_menu_items/<str:item_type>/', views.get_menu_items, name='get_menu_items'),
    path('add_to_session/', views.add_to_session, name='add_to_session'),
]


