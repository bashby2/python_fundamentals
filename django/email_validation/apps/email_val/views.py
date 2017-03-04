from django.shortcuts import render, redirect
from .models import Email, EmailManager
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'email_val/index.html')

def create(request):
    data = request.POST['email']
    print ("*"*50)
    print data
    valid, response = Email.objects.register(data)

    if valid:
        request.session['email'] = data
        Email.objects.create(email=data)
        context = {
            'emails' : Email.objects.all()
            }
        return redirect('/success')

    else:
        messages.error(request, "Not a valid email, please enter a valid email address")
        return redirect('/')


def success(request):
    context = {
    'emails' : Email.objects.all()
    }
    return render(request, 'email_val/success.html', context)
