from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail


# Create your views here.
def contact(request):
    # Get data from the from
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
    
    # Check
    if request.user.is_authenticated:
        user_id = request.user.id
        has_contacted = Contact.objects.all().filter(user_id=user_id)
        if has_contacted:
            messages.info(request, 'Mensagem anterior econtrada, entraremos em contato os breve possível')
            return redirect('index')

    contact = Contact(name=name, email=email, phone=phone, message=message, user_id=user_id)

    # Saving the data from the in the DB
    contact.save()

    # Sending email

    mail_list = [
        'leofelipe222@hotmail.com',
        'soskardec@gmail.com',
        'contact@soskardec.com',
        'flaviacarolyne@hotmail.com',
    ]

    send_mail(
        'Nova mensagem recebida do SOS Kardec website',
        'Mensagem: \n' + message + '\n',
        'soskardec@gmail.com',
        mail_list,
        fail_silently=False,
    )

    messages.success(request, 'Mensagem Enviada!')
    return redirect('/sobre')