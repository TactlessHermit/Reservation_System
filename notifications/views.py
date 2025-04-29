from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
def send_cancel_email(reservation):
    subject = "Reservation Cancellation Update"
    msg = "Dear User,\nYour reservation at {} on {} has been cancelled successfully.\nKind regards,\nRnS Team. "
    recipient_list = ['alfayedmalik@outlook.com']

    formatted_msg = msg.format(reservation.restaurant.name,
                    reservation.date
                    )

    send_mail(subject, formatted_msg, settings.EMAIL_HOST_USER, recipient_list)

def send_promo_email():
    msg = ""

    return msg

def send_reservation_email(reservation):
    subject = "Reservation Made!"
    msg = "Dear User,\nYour reservation at {} on {} has been created successfully.\nKind regards,\nRnS Team. "
    recipient_list = ['alfayedmalik@outlook.com']

    formatted_msg = msg.format(reservation.restaurant.name,
                               reservation.date
                               )

    send_mail(subject, formatted_msg, settings.EMAIL_HOST_USER, recipient_list)

def send_registration_email(user):
    subject = "Welcome Abaord"
    msg = "Dear {} {},\nYour account has been created successfully.\nKind regards,\nRnS Team. "
    recipient_list = [user.username]

    formatted_msg = msg.format(user.first_name,
                               user.last_name
                               )

    send_mail(subject, formatted_msg, settings.EMAIL_HOST_USER, recipient_list)