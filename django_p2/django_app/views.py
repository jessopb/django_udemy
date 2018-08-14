from django.shortcuts import render
from django.http import HttpResponse
from django_app.models import OurUsers

# Create your views here.


def index(request):
    cdict = {'content': 'Index Stuff'}
    return render(request, 'django_app/index.html', context=cdict)


def users(request):
    users = OurUsers.objects.order_by('last_name')
    udict = {'users': users}
    return render(request, 'django_app/users.html', context=udict)
