from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .models import Menu,Booking
from .serializers import MenuSerializer,BookingSerializer
# Create your views here.

def index(request):
    return render(request, 'index.html',{})

#It return all the menu items
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    # def get(self,request):
    #     items = Menu.objects.all()
    #     serialize_item = MenuSerializer(items,many = True)
    #     return Response(serialize_item.data)
    
    # def post(self,request):
    #     # title = request.POST.get('Title')
    #     # price = request.POST.get('Price')
    #     # inventory = request.POST.get('inventory')
    #     # menu = Menu(
    #     #     Title = title
    #     #     Price = price
    #     #     inventory = inventory
    #     # )
    #     serialized_item=MenuSerializer(data=request.data)
    #     serialized_item.is_valid(raise_exception=True)
    #     serialized_item.save()
    #     return Response(serialized_item.data)

#It returns single menu item based on id
class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    # def get(self,request,pk):
        