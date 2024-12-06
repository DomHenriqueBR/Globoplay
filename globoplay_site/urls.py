from django.contrib import admin
from django.urls import path
from cadastro import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categorias/criar/', views.criar_categoria, name='criar_categoria'),
    path('categorias/editar/<int:categoria_id>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/excluir/<int:categoria_id>/', views.excluir_categoria, name='excluir_categoria'),
    path('videos/', views.listar_videos, name='listar_videos'),
    path('videos/criar/', views.criar_video, name='criar_video'),
    path('videos/editar/<int:video_id>/', views.editar_video, name='editar_video'),
    path('videos/excluir/<int:video_id>/', views.excluir_video, name='excluir_video'),
]
