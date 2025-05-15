import time
from datetime import date, datetime
from lib2to3.fixes.fix_input import context

from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from reservations.forms import ReservationForm
from reservations.models import Reservation, Cancellations
from restaurants.models import Restaurant
from notifications import views


# Create your views here.
def make_reservation(request):
    """
        Creates reservation for current user (if registered). Redirects to
        user's reservations page
    """
    if request.method == 'POST':
        form = ReservationForm(request.POST)

        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.customer = request.user
            rest_id = form.cleaned_data['restaurant_name']
            reservation.restaurant = Restaurant.objects.get(id = rest_id)
            reservation.save()
            #Send reservation confirmation email
            views.send_reservation_email(reservation)
            return redirect(reverse('reservation:list'))
        else:
            messages.error(request, "Invalid form input.")

    form = ReservationForm()
    template_name = 'reservations/forms/create_form.html'
    return render(request, template_name, {'form': form})

class ReservationDetails(generic.DetailView):
    """
        Shows details of given reservation
    """
    model = Reservation
    context_object_name = 'reservation'
    template_name = 'reservations/webpages/reservation_details.html'

def reservation_details(request, pk):
    """
        Shows details of given reservation
    """
    reservation = Reservation.objects.get(id = pk)
    today_date = date.today()
    cancellable = False

    # If OLD reservation, set variable to prevent cancel option being shown on webpage
    if reservation.date >= today_date:
        cancellable = True

    context = {
        'reservation': reservation,
        'cancellable': cancellable
    }
    template_name = 'reservations/webpages/reservation_details.html'

    return render(request, template_name, context)

def all_reservations(request):
    """
        Shows all reservations for the current user
    """
    today_date = date.today()
    reservations = Reservation.objects.filter(customer = request.user, date__gte=today_date)

    content = {
        'all_reservations': reservations
    }
    template_name = 'reservations/webpages/all_reservations.html'
    return render(request, template_name, content)

def cancel_reservation(request, pk):
    """
        Cancels a specified reservation. Saves reservation data and cancellation reason in
        Cancellations table. Deletes cancelled reservation.
    """
    if request.method == 'POST':
        reason = request.POST['reason']
        #Get reservation to delete
        reservation = Reservation.objects.get(id=pk)

        #Check with cancellation policy
        current_datetime = datetime.now()
        res_datetime = datetime.combine(reservation.date, reservation.time)

        # Cancellation before reservation date and time
        if current_datetime < res_datetime:
            duration = (res_datetime - current_datetime)
            hours = duration.seconds // 3600
            # IF Cancelled AT LEAST an hour earlier
            if hours >= 1:
                messages.info(request, "Cancelled on time!! Refund applicable")
            else:
                messages.info(request, "Cancelled OVER an hour!!  Refund inapplicable")
        elif current_datetime > res_datetime:
            messages.info(request, "Late cancellation!!")
        else:
            pass

        #Save cancellation data
        cancellation = Cancellations(date=reservation.date, time=reservation.time, reason=reason,
                                     customer=reservation.customer, restaurant=reservation.restaurant,
                                     no_of_guests=reservation.no_of_guests)
        cancellation.save()
        #Delete reservation
        reservation.delete()

        # messages.success(request, "Reservation cancelled.")
        return redirect(reverse('reservation:list'))
    else:
        return render(request, 'reservations/forms/cancellation_form.html')

def past_reservations(request):
    """
        Shows all reservations for the current user
    """
    today_date= date.today()
    reservations = Reservation.objects.filter(customer = request.user, date__lt=today_date)

    content = {
        'all_reservations': reservations,
        'past_reserv': True
    }
    template_name = 'reservations/webpages/all_reservations.html'
    return render(request, template_name, content)

def update_status(pk, change):
    pass