from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Menu,Booking
from .serializers import MenuSerializer,BookingSerializer
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .forms import BookingForm
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import json
from django.http import HttpResponse
from django.core import serializers

# Create your views here.

def index(request):
    return render(request, 'index1.html',{})

def menu(request):
    menu_items = Menu.objects.all()
    return render(request, 'menu.html', {"menu": menu_items})

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
    #     if request.user.groups.filter(name = 'Manager').exists() or request.user.is_superuser:
    #         return super().post(request)
    #     return Response({'Message' : 'You are not Authorized'}, status = status.HTTP_403_FORBIDDEN)
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
    
    # def put(self, request):
    #     if request.user.groups.filter(name = 'Manager').exists() or request.user.is_superuser:
    #         return super().post(request)
    #     return Response({"message": "You are not authorized"}, status = status.HTTP_403_FORBIDDEN)

    # def patch(self, request):
    #     if request.user.groups.filter(name = 'Manager').exists() or request.user.is_superuser:
    #         return super().post(request)
    #     return Response({"message": "You are not authorized"}, status = status.HTTP_403_FORBIDDEN)

    # def delete(self, request):
    #     if request.user.groups.filter(name = 'Manager').exists() or request.user.is_superuser:
    #         return super().post(request)
    #     return Response({"message": "You are not authorized"}, status = status.HTTP_403_FORBIDDEN)

#It returns single menu item based on id
class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    def get(self, request, *args, **kwargs):
        return super().get(request,*args,**kwargs)
    
    def put(self, request,*args, **kwargs):
        if request.user.group.filter(name='Manager').exists():
            return super().put(request,*args, **kwargs)
        return Response({'Message':'You are Not authorized'},status=status.HTTP_403_FORBIDDEN)
    
    def patch(self, request, *args, **kwargs):
        if request.user.group.filter(name = 'Manager').exists():
            return super().patch(request,*args, **kwargs)
        return Response({'Message':'You are Not authorized'},status=status.HTTP_403_FORBIDDEN)
    
    def delete(self, request, *args, **kwargs):
        if request.user.groups.filter(name = 'Manager').exists():
            return super().delete(request, *args, **kwargs)
        return Response({"message": "You are not authorized"}, status = status.HTTP_403_FORBIDDEN)

    
#This class returns booking details
class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# class UserViewSet(ModelViewSet):
#    queryset = User.objects.all() 
#    serializer_class = UserSerializer
#    permission_classes = [permissions.IsAuthenticated] =

def book(request):
    form = BookingForm
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'book.html', context)

def about(request):
    return render(request, "about.html")

@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data = json.load(request)
        exist = Booking.objects.filter(booking_date=data['booking_date']).filter(
            no_of_guests=data['no_of_guests']).exists()
        if exist==False:
            booking = Booking(
                name=data['name'],
                booking_date=data['booking_date'],
                no_of_guests=data['no_of_guests'],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type='application/json')
    
    date = request.GET.get('date',datetime.today().date())

    bookings = Booking.objects.all().filter(booking_date=date)
    booking_json = serializers.serialize('json', bookings)

    return HttpResponse(booking_json, content_type='application/json')


def reservations(request):
    date = request.GET.get('date', datetime.today().date())
    print("date: ", date)
    bookings = Booking.objects.all().filter(booking_date = date)
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html', {'bookings': booking_json})




