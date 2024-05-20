from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('book/', views.book, name="book"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('bookings', views.bookings, name="bookings"),
    path('reservations/', views.reservations, name="reservations"),
    path('menuitems/',views.MenuItemsView.as_view(), name='MenuItemsView'),
    path('menuitems/<int:pk>',views.SingleMenuItemView.as_view(), name='SingleMenuItemView'),
    path('obtain-auth-token/',obtain_auth_token),
         
]
