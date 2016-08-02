from django import forms
from .models import Post, Comentario


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo','cuerpo']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'email', 'cuerpo']
