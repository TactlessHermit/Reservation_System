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
from django.urls import path
from . import views

app_name = 'reservation'

urlpatterns = [
    path('new', views.make_reservation, name='new'),
    path('active', views.all_reservations, name='list'),
    path('old', views.past_reservations, name='past'),
    path('<int:pk>', views.reservation_details, name='details'),
    # path('<int:pk>', views.ReservationDetails.as_view(), name='details'),
    path('<int:pk>/cancel', views.cancel_reservation, name='cancel'),
]
