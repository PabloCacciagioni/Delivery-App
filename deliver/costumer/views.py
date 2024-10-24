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
            'drinks': drinks,
        }
        
        #Render the template
        return render(request, 'costumer/order.html', context)
    
    def post(self, request, *args, **kwargs):
        order_items = {
            'items': []
        }
        
        items = request.POST.getlist('items[]')
        
        for item in items:
            menu_item = MenuItem.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }
            order_items['items'].append(item_data)
            
            price = 0
            item_ids = []
            
            for item in order_items['items']:
                price += item['price']
                item.ids.append(item['id'])
                
            order = OrderModel.objects.create(price=price)
            order.items.add(*item_id)
            
            context = {
                'items': order_items['items'],
                'price': price
            }
            
            return render(request, 'customer/order_information.html', context)