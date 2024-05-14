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
        #It receives url of Menu Item Views
        """Name must be declared as MenuItemsView in urls.py(app) file"""
        url = reverse('MenuItemsView')
        response = self.client.get(url) # It gets some response from above url as Html status code
        self.assertEqual(response.status_code,200) # If Status code equal to 200 then assertion is true otherwise test would be failed.
        
        items = Menu.objects.all() # It returns all object of Menu model
        serializer = MenuSerializer(items, many = True) # It serialize data of item
        self.assertEqual(serializer.data, response.data) # If serialize data is equal to response data then test would be Passed. 