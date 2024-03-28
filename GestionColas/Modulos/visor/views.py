from django.shortcuts import render
from Modulos.visor.models import *
# Create your views here.
def home(request):
    
    fichas = Ficha.objects.all()
    data={
        "fichas": fichas
    }
    
    return render(request,"home.html",data)