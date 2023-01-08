from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from .models import Post
from django.views.generic import ListView, DetailView,FormView
from .forms import PostFrom
# Create your views here.
class indexView(TemplateView):
    template_name  = 'index.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['name'] = 'hoseyn'
        context ['test'] = Post.objects.all()
        return context

class RedirectToGoogle(RedirectView):
    url = 'https://google.com/'



class PostList(ListView):
    # model = Post
    queryset = Post.objects.all()   
    # def get_queryset(self):
    #     posts = Post.objects.filter(status = True)  
    #     return posts
    paginate_by = 2
    # ordering = '-title'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model  = Post


class PostCreate(FormView):
    template_name = 'blog/contact.html'
    form_class = PostFrom 
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
