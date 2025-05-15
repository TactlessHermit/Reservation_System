"""
URL configuration for reservation_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('new', views.add_restaurant, name='new'),
    path('all', views.get_restaurants, name='all'),
    path('tags', views.get_restaurants, name='all'),
    path('all/filtered', views.filtered_restaurants, name='filtered'),
    path('all/<str:tag_name>', views.search_by_tag, name='by_tag'),
    path('<int:pk>', views.restaurant_page, name='details'),
    # path('<int:pk>', views.RestaurantDetails.as_view(), name='details'),
    path('<int:pk>/update', views.update_restaurant, name='update'),
    path('<int:pk>/delete', views.delete_restaurant, name='delete'),
]
