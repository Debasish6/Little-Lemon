from django.test import TestCase
from restaurant.models import Menu

class MenuItemClass(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title = 'Ice Cream', Price = 80, inventory = 50)
        
        self.assertEqual(str(item), "Ice Cream : 80")