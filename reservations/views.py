from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from reservations.forms import ReservationForm
from reservations.models import Reservation
from restaurants.models import Restaurant


# Create your views here.
def make_reservation(request):

    if request.method == 'POST':
        form = ReservationForm(request.POST)

        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.customer = request.user
            rest_id = form.cleaned_data['restaurant_name']
            reservation.restaurant = Restaurant.objects.get(id = rest_id)
            reservation.save()
            return redirect(reverse('reservation:list'))
        else:
            messages.error(request, "Invalid form input.")

    form = ReservationForm()
    template_name = 'reservations/forms/create_form.html'
    return render(request, template_name, {'form': form})

class ReservationDetails(generic.DetailView):
    model = Reservation
    context_object_name = 'reservation'
    template_name = 'reservations/webpages/reservation_details.html'

def all_reservations(request):
    reservations = Reservation.objects.filter(customer = request.user)

    content = {
        'all_reservations': reservations
    }
    template_name = 'reservations/webpages/all_reservations.html'
    return render(request, template_name, content)

def cancel_reservation(request, pk):
    reservation = Reservation.objects.get(id=pk)
    reservation.delete()

    messages.success(request, "Reservation cancelled.")
    return redirect(reverse('reservation:list'))