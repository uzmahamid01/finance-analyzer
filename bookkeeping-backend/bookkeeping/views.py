# in bookkeeping/views.py or any app's views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the homepage!")
