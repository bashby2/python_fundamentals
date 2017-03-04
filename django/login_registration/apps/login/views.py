from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def index(request):
    return render(request, 'login/index.html')
def logout(request):
    return redirect('/')

def login(request):
    if request.method == 'POST':
        returned_tuple = User.objects.login_user(request.POST)
        print returned_tuple
        print ('*8'*50)
        if returned_tuple == True:
            print "it's working",('|'*50)
            return render(request, 'login/success.html')
        else:
            print "NOT VAILD",('--'*60)
            for err in returned_tuple[1]:
                messages.error(request, err)
            return redirect('/')
    else:
        print('@'*60)
        return redirect('/')

def register(request):
    print ('8'*50)
    print ('8'*50)
    print 'what is going on?'
    if request.method == 'POST':
        returned_tuple = User.objects.create_new_user(request.POST)
        print returned_tuple
        print ('*8'*50)
        if returned_tuple == True:
            print "it's working",('|'*50)
            return render(request, 'login/success.html')
        else:
            print "NOT VAILD",('--'*60)
            for err in returned_tuple[1]:
                messages.error(request, err)
            return redirect('/')
    else:
        print('@'*60)
        return redirect('/')
