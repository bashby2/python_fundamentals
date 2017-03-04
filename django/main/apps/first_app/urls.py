from django.conf.urls import url

def index(request):
    print ("8" * 100)
    print ("bannanapeel")
urlpatterns = [
      url(r'^$', index)
]
