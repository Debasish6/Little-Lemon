from django.test import TestCase
from restaurant.models import Menu

class MenuItemClass(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.item =  Menu.objects.create(
            Title = 'Ice Cream',
            Price = 80,
            inventory = 50
            )
        
    def test_get_item(self):
        # item = Menu.objects.create(Title = 'Ice Cream', Price = 80, inventory = 50)
        
        self.assertEqual(str(self.item), "Ice Cream : 80")
    
    def test_fields(self):
        self.assertIsInstance(self.item.Title,str)