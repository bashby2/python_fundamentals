from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'survey/index.html', context)

def create(request):
    if request.method == 'POST':
        print ('*' *50)
        print (request.POST)
        print ('*' *50)
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        return render(request, 'survey/result.html')
    else:
        return redirect('/')
