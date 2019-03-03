from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import GroceryItem
# Create your views here.

model = GroceryItem
template_name = "grocery_list_lab/form.html"

def get_grocerylist_items(request):
    grocery_list = GroceryItem.objects.filter(item_was_completed=False).order_by('-created_date')
    completed_grocery_list = GroceryItem.objects.filter(item_was_completed=True)
    context = {
        'grocery_list':grocery_list,
        'completed_grocery_list':completed_grocery_list
    }
    return render(request, 'grocery_list_lab/form.html', context)

def add_item(request):
    print(request.POST)
    item_description_text = request.POST["description"]
    created_date = timezone.now()
    new_item = GroceryItem(item_description_text=item_description_text, created_date=created_date)
    new_item.save()
    grocery_list = GroceryItem.objects.filter(item_was_completed=False).order_by('-created_date')
    return HttpResponseRedirect(reverse('grocery_list_lab:get_grocerylist_items'))

def remove_item(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.item_was_completed = True
    item.completed_date = timezone.now()
    item.save()
    return HttpResponseRedirect(reverse('grocery_list_lab:get_grocerylist_items'))