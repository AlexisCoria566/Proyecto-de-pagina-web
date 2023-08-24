from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.utils import timezone
from django.views.generic.edit import CreateView, DeleteView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from criticas.models import Opinion
from criticas.forms import OpinionForm



# Create your views here.

class OpinionListView(ListView):
    model = Opinion   

class OpinionCreate(CreateView):
    model = Opinion
    form_class = OpinionForm
    success_url = reverse_lazy('reviews')

class OpinionUpdate(UpdateView):
    model = Opinion
    form_class = OpinionForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('reviews')+'?Actualizado'

class OpinionDelete(DeleteView):
    model = Opinion
    
    def get_success_url(self):
        return reverse_lazy('reviews')+'?Eliminado'

class OpinionDetailView(DetailView):
    model = Opinion

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context



