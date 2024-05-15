from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .models import Menu,Booking
from .serializers import MenuSerializer,BookingSerializer
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.

def index(request):
    return render(request, 'index.html',{})

#It return all the menu items

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    # def get(self,request,pk):
    
#This class returns booking details
class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# class UserViewSet(ModelViewSet):
#    queryset = User.objects.all() 
#    serializer_class = UserSerializer
#    permission_classes = [permissions.IsAuthenticated] =

@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({'message':"This is protected view"})




