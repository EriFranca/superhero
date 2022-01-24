from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='index'),
    path('single-hero/<int:id>', views.single_hero, name='single-hero'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)