from django.shortcuts import render
from .models import data_twitter


# Create your views here.
def index(request):

    queryset = data_twitter.objects.all()

    data = {
        'data': queryset
    }

    return render(request, 'index.html', data)

def contact(request):
    return render(request, 'contact.html')


