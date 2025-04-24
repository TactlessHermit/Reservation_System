from tempfile import template

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from .models import Restaurant
from .forms import RestaurantForm

# Create your views here.
def  add_restaurant(request):

    if request.method == 'POST':
        form = RestaurantForm(request.POST)

        if form.is_valid():
            restaurant = form.save()
            return redirect(reverse('restaurant:details', kwargs={'pk': restaurant.id}))
        else:
            messages.success(request, "Invalid form input.")

    form = RestaurantForm()
    template_name = 'restaurants/forms/add_or_update.html'

    return render(request, template_name, {'form': form})

def all_restaurants(request):
    restaurants = Restaurant.objects.all().values()
    template_name = 'restaurants/webpages/all_restaurants.html'

    return render(request, template_name, {'restaurants': restaurants})

class RestaurantDetails(generic.DetailView):
    model = Restaurant
    context_object_name = 'restaurant'
    template_name = 'restaurants/webpages/restaurant.html'

def update_restaurant(request, pk):
    restaurant = get_object_or_404(Restaurant, pk = pk)

    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)

        if form.is_valid():
            form.save()
            return redirect(reverse('restaurant:details', kwargs={'pk': pk}))
        else:
            messages.success(request, "Invalid form input.")

    form = RestaurantForm(instance=restaurant)
    template_name = 'restaurants/forms/add_or_update.html'

    return render(request, template_name, {'form': form})

def delete_restaurant(request, pk):

    restaurant = Restaurant.objects.get(id = pk)
    restaurant.delete()

    messages.success(request, "Restaurant data deleted.")
    return redirect(reverse('restaurant:all'))
