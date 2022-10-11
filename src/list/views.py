from multiprocessing import context
from tkinter.messagebox import QUESTION
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views import generic
from . import models
from datetime import datetime
from django.urls import reverse_lazy


# Create your views here.



class BesedkaDetailView(generic.DetailView):
    template_name = 'list/besedka_view.html'
    model=models.Besedka

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['today'] = datetime.now().date
        q = models.Besedka.objects.get(pk = self.object.pk)    
        return context


class BilliardDetailView(generic.DetailView):
    template_name = 'list/billiard_view.html'
    model=models.Billiard

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['today'] = datetime.now().date
        q = models.Billiard.objects.get(pk = self.object.pk)    
        return context


class PoolDetailView(generic.DetailView):
    template_name = 'list/pool_view.html'
    model=models.Pool

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['today'] = datetime.now().date
        q = models.Pool.objects.get(pk = self.object.pk)    
        return context