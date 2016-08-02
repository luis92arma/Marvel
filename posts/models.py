from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Post(models.Model):
    STATUS_CHOICE = (
        ('draft','Draft'),
        ('piblished','Published'),
    )
    autor = models.ForeignKey(
        User,
        related_name='blog_post',
        blank=True,
        null=True,
    )
    titulo = models.CharField(max_length = 100)
    cuerpo = models.TextField()
    creado = models.DateTimeField(
        auto_now = True,
        blank = True,
        null = True
    )
    actualizado = models.DateTimeField(
        auto_now_add = True,
        blank = True,
        null = True
    )
    status = models.CharField(
        max_length = 10,
        choices = STATUS_CHOICE,
        default = 'draft',
        blank = True,
        null = True
    )
    slug = models.SlugField(
        max_length = 200,
        unique_for_date = 'creado',
        blank = True,
        null = True
    )

    class Meta:
        ordering = ('-creado', )

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('posts:detalle', args=[self.slug])

class Comentario(models.Model):
    post = models.ForeignKey(
        Post,
        related_name = 'comments',
        blank = True,
        null = True,
    )
    autor = models.CharField(
        max_length = 80,
        blank = True,
        null = True,
    )
    email = models.EmailField(
        blank = True,
        null = True,
    )
    cuerpo = models.TextField()
    fecha = models.DateTimeField(
        auto_now_add = True,
        blank = True,
        null = True,
    )
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ('-fecha',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.autor, self.post)
