from django.shortcuts import render
from django.views.generic import View
from .models import Post
from django.contrib.auth.models import User
from .forms import PostForm

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
    def get(self,request,slug,id):
        template_name = 'detalle.html'
        post = Post.objects.get(id=id,slug=slug)
        context = {
            'post': post
        }
        return render(request, template_name, context)

class NuevoPost(View):
    def get(self, request):
        template_name = 'nuevo.html'
        form = PostForm()
        context = {
            'form': form,
        }
        return render(request, template_name, context)

    def post(self,request):
        template_name = 'nuevo.html'
        context = {
            'guardado':True,
        }
        form = PostForm(request.POST)
        form.save()
        return render(request,template_name, context)





        '''
        titulo = request.POST.get('titulo')
        cuerpo = request.POST.get('cuerpo')
        post = Post() #instanciar
        post.titulo = titulo
        post.cuerpo = cuerpo
        try:
            post.autor = request.user
        except:
            pass
        post.save()
        template_name = 'nuevo.html'
        context = {
            'guardado': True
        }
        return render(request, template_name, context)'''
