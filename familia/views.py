from django.shortcuts import render
from familia.models import Familia

def familia(request):
    familiar1 = Familia(nombre='Juan', apellido='Gonzalez')
    familiar1.save()
    contexto = {
        'familia':familiar1

    }

    return render(request,'familia.html', contexto)

def familiar2(request):
    familiar2 = Familia(nombre='Lucia', apellido='Gonzalez')
    familiar2.save()
    contexto = {
        'familia':familiar2

    }

    return render(request,'familia.html', contexto)

def familiar3(request):
    familiar3 = Familia(nombre='Hector', apellido='Gonzalez')
    familiar3.save()
    contexto = {
        'familia':familiar3

    }

    return render(request,'familia.html', contexto)



