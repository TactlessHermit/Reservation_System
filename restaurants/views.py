from lib2to3.fixes.fix_input import context

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from .models import Restaurant, Tag, RestaurantTags
from .forms import RestaurantForm

# Create your views here.
def  add_restaurant(request):
    """
        Adds new restaurant to database.
    """
    if request.method == 'POST':
        form = RestaurantForm(request.POST)

        if form.is_valid():
            tags = form.cleaned_data['tags']
            restaurant = form.save()
            #Creates a RestaurantTags entry for each tag
            for tag_id in tags:
                RestaurantTags.objects.create(restaurant = restaurant, tag = Tag.objects.get(id = tag_id))

            return redirect(reverse('restaurant:details', kwargs={'pk': restaurant.id}))
        else:
            messages.success(request, "Invalid form input.")

    form = RestaurantForm()
    template_name = 'restaurants/forms/add_or_update.html'

    return render(request, template_name, {'form': form})

def get_restaurants(request):
    """
        Gets all listed restaurants in database
    """
    restaurants = Restaurant.objects.all().values()
    tags = Tag.objects.all().values()
    template_name = 'restaurants/webpages/all_restaurants.html'

    return render(request, template_name, {'restaurants': restaurants, 'tags': tags})

class RestaurantDetails(generic.DetailView):
    model = Restaurant
    context_object_name = 'restaurant'
    template_name = 'restaurants/webpages/restaurant.html'

def restaurant_page(request, pk):
    """
        Shows details of selected restaurant
    """
    restaurant = Restaurant.objects.get(id = pk)
    rest_tags = RestaurantTags.objects.filter(restaurant = restaurant)
    tags = []

    #Fills array with related tags from RestaurantTags
    for rest_tag in rest_tags:
        tags.append(Tag.objects.get(id = rest_tag.tag.id))

    context_tuple = {
        'restaurant': restaurant,
        'tags': tags
    }

    return render(request, 'restaurants/webpages/restaurant.html', context_tuple)

def update_restaurant(request, pk):
    """
        Updates select details of a given restaurant
    """
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
    """
        Delists a specific restaurant
    """
    restaurant = Restaurant.objects.get(id = pk)
    restaurant.delete()

    messages.success(request, "Restaurant data deleted.")
    return redirect(reverse('restaurant:all'))

def filtered_restaurants(request):
    """
        Gets a filtered list of restaurants
    """
    if request.method == 'POST':
        restaurants = []
        id = request.POST['filter_tag']

        # Query join restaurant & restaurant_tags. Filter based on tag_id
        results = RestaurantTags.objects.filter(tag_id=id)

        #Gets list of restaurants in queryset (if not empty)
        if results:
            for result in results:
                restaurants.append(result.restaurant)

        tags = Tag.objects.all().values()
        template_name = 'restaurants/webpages/all_restaurants.html'
        context = {
            'restaurants': restaurants,
            'tags': tags,
            'is_filtered': True
        }

        return render(request, template_name, context)

def show_tags(request):
    """
        Displays all restaurant tags
    """
    tags = Tag.objects.all().values()
    template_name = 'restaurants/webpages/select_tag.html'
    context = {
        'tags': tags
    }

    return render(request, template_name, context)

def search_by_tag(request, tag_name):
    """"
        Gets list of restaurants with given restaurant tag
    """
    restaurants = []

    # Query join restaurant & restaurant_tags. Filter based on tag_name
    results = RestaurantTags.objects.filter(tag__name__iexact = tag_name)

    # Gets list of restaurants in queryset (if not empty)
    if results:
        for result in results:
            restaurants.append(result.restaurant)

    tags = Tag.objects.all()
    template_name = 'restaurants/webpages/all_restaurants.html'
    context = {
        'restaurants': restaurants,
        'tags': tags,
        'is_filtered': True
    }

    return render(request, template_name, context)