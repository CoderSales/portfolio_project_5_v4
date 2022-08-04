from django.shortcuts import render
from django.core.mail import send_mail


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email

        send_mail(
            message_name, # subject
            message, # message
            message_email, # from email
            ['recipeint@email.com', message_email], # to email

        )
        return render(request, 'contact.html', {'message_name': message_name})

    else:
        return render(request, 'contact.html', {})
