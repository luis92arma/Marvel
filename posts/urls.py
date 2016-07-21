from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ListView.as_view(), name='home'),
    url(r'^nuevo/$', views.NuevoPost.as_view()),
    url(r'^(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name="detalle"),
]
