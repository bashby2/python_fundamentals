from django.shortcuts import render, HttpResponse
from datetime import datetime
def index(request):
    context = {
    'date': datetime.now().strftime("%b %d, %Y"),
    'time': datetime.now().strftime("%I:%M %p")
    }
    return render(request, 'timedisplay/index.html', context)
# Create your views here.
