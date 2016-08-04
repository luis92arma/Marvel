from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .models import Post, Comentario
from django.contrib.auth.models import User
from .forms import PostForm, ComentarioForm
from django.utils.text import slugify
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class ListView(View):
    def get(self, request):
        template_name = 'blog.html'
        user = User.objects.get(username='luis')
        posts = user.blog_post.all()
        #print(user,' ', posts)
        context = {
            'entradas': posts
        }
        return render(request, template_name, context)

class DetailView(View):
    def get(self,request,slug):
        template_name = 'detalle.html'
        post = Post.objects.get(slug=slug)
        form = ComentarioForm()
        comment = post.comments.filter(activo = True)
        #print(comment)
        context = {
            'post': post,
            'comments': comment,
            'form': form,
        }
        #url = post.get_absolute_url
        #redirect(url)
        return render(request, template_name, context)

    def post(self, request, slug):
        form = ComentarioForm(request.POST)
        if form.is_valid():
            post = Post.objects.get(slug=slug)
            #print(post)
            newComment = form.save(commit=False)
            newComment.post = post
            newComment.save()
            form.save()
            messages.success(request, 'Hey! que buen comentario...')
            return redirect('posts:detalle', slug=slug)
        else:
            messages.error(request, 'Intentalo de nuevo')
            return redirect('posts:detalle', slug=slug)


class NuevoPost(View):
    @method_decorator(login_required)
    def get(self, request):
        template_name = 'nuevo.html'
        form = PostForm()
        context = {
            'form': form,
        }
        return render(request, template_name, context)

    def post(self,request):
        template_name = 'nuevo.html'
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            NuevoPost = form.save(commit = False)
            NuevoPost.slug = slugify(NuevoPost.titulo)
            NuevoPost.user = request.user
            NuevoPost.save()
            messages.success(request, 'Gran Post Guardado')
            return redirect('posts:blog')
        else:
            messages.error(request, 'Intentalo de nuevo')
            return redirect('posts:new')





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
