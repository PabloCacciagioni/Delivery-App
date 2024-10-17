from django.shortcuts import render
from django.views import View
from .models import MenuItem

# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'costumer/index.html')
    
class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'costumer/about.html')

class Order(View):
    def get(self, request, *args, **kwargs):
        #Get every item from each category
        appetizers = MenuItem.objects.filter(category__name__contains='Appetizer')
        entres = MenuItem.objects.filter(category__name__contains='Entre')
        desserts = MenuItem.objects.filter(category__name__contains='Appetizer')
        drinks = MenuItem.objects.filter(category__name__contains='Drink')
        
        #Pass into context
        context = {
            'appetizers': appetizers,
            'entres': entres,
            'desserts': desserts,
            'drinks': drinks
        }
        
        #Render the template
        return render(request, 'costumer/order.html', context)