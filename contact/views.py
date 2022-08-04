from django.shortcuts import render
from django.core.mail import send_mail


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        return render(request, 'contact.html', {'message_name': message_name})

        # send an email

        send_mail(
            message_name, # subject
            message, # message
            message_email, # from email
            ['recipeint@email.com'], # to email

        )

    else:
        return render(request, 'contact.html', {})
