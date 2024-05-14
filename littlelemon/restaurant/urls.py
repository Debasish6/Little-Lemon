from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('index/',views.index, name='index'),
    path('menu/',views.MenuItemsView.as_view(), name='MenuItemsView'),
    path('menu/<int:pk>',views.SingleMenuItemView.as_view(), name='SingleMenuItemView'),
    path('message/',views.msg),
    path('obtain-auth-token/',obtain_auth_token),
    
        
]
