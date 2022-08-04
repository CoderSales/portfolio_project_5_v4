from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email

        send_mail(
            message_name,  # subject
            message,  # message
            message_email,  # from email
            ['recipient@email.com', settings.DEFAULT_TO_EMAIL_SETTER,
             message_email],  # to email

        )
        return render(request, 'contact.html', {'message_name': message_name})

    else:
        return render(request, 'contact.html', {})
