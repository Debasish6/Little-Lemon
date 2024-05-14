from django.test import TestCase
from restaurant.models import Menu
from django.urls import reverse
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User


class MenuViewTest(TestCase):
    
    def setUp(self):
        # self.username = 'testuser'
        # self.password = 'testpassword'
        # self.user = User.objects.create_user(username=self.username, password=self.password)
        
        item1 = Menu.objects.create(Title="Ice Cream", Price=80, inventory = 100)
        item2 = Menu.objects.create(Title = "Pizza", Price = 199, inventory = 20)
         
        
    def test_getall(self):
        url = reverse('MenuItemsView')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many = True)
        self.assertEqual(serializer.data, response.data)