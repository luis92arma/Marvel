from django.shortcuts import render, HttpResponse
from django.views.generic import View
from .marvelAPI import *
# Create your views here.
class Descripcion(View):
    def get(self, request):
        #avengers = ['thor', 'hulk','iron man']
        #n = len(avengers)
        template_name = 'descripcion.html'
        ultron = PachuMarvel()
        ultron.get_personaje('ultron')
        context = {
            'name': ultron.nombre,
            'descripcion': ultron.descripcion,
            'img': ultron.img,
        }
        return render(request, template_name, context)
