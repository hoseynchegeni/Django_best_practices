from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from .models import Post
from django.views.generic import ListView, DetailView,FormView, CreateView, UpdateView, DeleteView
from .forms import PostFrom
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
class indexView(TemplateView):
    template_name  = 'index.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['name'] = 'test'
        context ['test'] = Post.objects.all()
        return context

class RedirectToGoogle(RedirectView):
    url = 'https://google.com/'



class PostList(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    # model = Post
    permission_required = 'blog.view_post'
    queryset = Post.objects.all()   
    # def get_queryset(self):
    #     posts = Post.objects.filter(status = True)  
    #     return posts
    paginate_by = 5
    # ordering = '-title'
    context_object_name = 'posts'


class PostDetailView(LoginRequiredMixin,DetailView):
    model  = Post


'''
class PostCreate(FormView):
    template_name = 'blog/contact.html'
    form_class = PostFrom 
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
'''

class PostCreate(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content','status','category','published_date']
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostFrom
    success_url = '/blog/post/'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/blog/post/'

@api_view()
def ApiView(request):
    return Response('Ok')