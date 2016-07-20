from django.shortcuts import render
from django.views.generic import View
from .models import Post
from django.contrib.auth.models import User

class ListView(View):
    def get(self, request):
        template_name = 'blog.html'
        user = User.objects.get(username='luis')
        posts = user.blog_post.all()
        context = {
            'entradas': posts
        }
        return render(request, template_name, context)

class DetailView(View):
    def get(self,request,id):
        template_name = 'detalle.html'
        post = Post.objects.get(pk=id)
        context = {
            'post': post
        }
        return render(request, template_name, context)
