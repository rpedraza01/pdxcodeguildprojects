from django.urls import path

from . import views

app_name = 'grocery_list_lab'
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    # path('groceries', views.form, name='form'),
    path('', views.get_grocerylist_items, name='get_grocerylist_items'),
    path('add_item', views.add_item, name='add_item'),
    path('remove_item/<int:pk>', views.remove_item, name='remove_item')
]