from django.http import HttpResponse

def home(req):
    return HttpResponse("Welcome to Well Crafters Mini E-commerce-backend")