from django.shortcuts import HttpResponse


def home(request):
    return HttpResponse("<center><h2>Vous êtes sur l'API de vegan-breath network</h2></center>")