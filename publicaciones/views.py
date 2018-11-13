from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import SingleObjectMixin
from publicaciones.models import Titulare, Articulo

# Create your views here.

class Inicio(ListView):
    template_name = "publicacion/inicio.html"
    def get_queryset(self):
        queryset = Titulare.objects.all()    
        return queryset
    
class Noticia(SingleObjectMixin, ListView):
    template_name='publicacion/noticia.html'
    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset = Titulare.objects.all())
        return super(Noticia, self).get(request,*args,**kwargs)
    def get_queryset(self):
        queryset= Articulo.objects.all()
        aux = []
        for item in queryset:
            if item.slug == self.object.slug:
                aux.append(item.slug)
        return queryset.filter(slug__in=aux)
    def get_context_data(self, **kwargs):
        context = super(Noticia, self).get_context_data(**kwargs)
        context['titular'] = self.object
        return context