from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'ninjas/index.html')

# Create your views here.
