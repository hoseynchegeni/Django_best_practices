from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from .models import Post
# Create your views here.
class indexView(TemplateView):
    template_name  = 'index.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['name'] = 'Tahmine Aminzade'
        context ['test'] = Post.objects.all()
        return context

class RedirectToGoogle(RedirectView):
    url = 'https://google.com/'