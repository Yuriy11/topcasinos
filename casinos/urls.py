from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('casinos/', views.casinos, name='casinos'),
    path('casino/<int:casino_id>/', views.cinfo, name='cinfo'),
    path('', views.index, name='index'),
    path('bonuses/', views.bonuses, name='bonuses'),
    path('bonus/<int:bonus_id>/', views.binfo, name='binfo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)