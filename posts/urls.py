from django.conf.urls import url, include
from . import views
#from information import urls as viewInformation

urlpatterns = [
    url(r'^$', views.ListView.as_view(), name='blog'),
    url(r'^nuevo/$', views.NuevoPost.as_view(), name='new'),
    url(r'^(?P<slug>[\w-]+)/$', views.DetailView.as_view(), name="detalle"),
    #url(r'^', views.viewInformation.as_view(), name='homeReturn')
]
