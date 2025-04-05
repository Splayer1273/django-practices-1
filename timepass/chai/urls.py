
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name='../templates/base.html'),

    path('chai/<int:id>/view/', views.view_chai, name='view_chai'),

    path('home/', views.home, name='home'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
