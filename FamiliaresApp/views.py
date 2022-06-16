from django.shortcuts import render
from .models import Familiar



def index (request):
    Familiares = Familiar.objects.all()
    ctx = {"Familiar": Familiares }

    return render ( request ,"FamiliaresApp/index.html", ctx)