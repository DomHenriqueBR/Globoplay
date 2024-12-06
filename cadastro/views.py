from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Categoria, Video


# Página principal
def index(request):
    return render(request, 'cadastro/index.html')


# CRUD Categoria
def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'cadastro/listar_categorias.html', {'categorias': categorias})


def criar_categoria(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        Categoria.objects.create(nome=nome)
        return redirect('listar_categorias')
    return render(request, 'cadastro/criar_categoria.html')


def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        categoria.nome = request.POST.get('nome')
        categoria.save()
        return redirect('listar_categorias')
    return render(request, 'cadastro/editar_categoria.html', {'categoria': categoria})


def excluir_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    categoria.delete()
    return redirect('listar_categorias')


# CRUD Video
def listar_videos(request):
    videos = Video.objects.select_related('categoria').all()
    return render(request, 'cadastro/listar_videos.html', {'videos': videos})


def criar_video(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        categoria_id = request.POST.get('categoria')
        categoria = get_object_or_404(Categoria, id=categoria_id)
        Video.objects.create(titulo=titulo, descricao=descricao, categoria=categoria)
        return redirect('listar_videos')
    return render(request, 'cadastro/criar_video.html', {'categorias': categorias})


def editar_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        video.titulo = request.POST.get('titulo')
        video.descricao = request.POST.get('descricao')
        categoria_id = request.POST.get('categoria')
        video.categoria = get_object_or_404(Categoria, id=categoria_id)
        video.save()
        return redirect('listar_videos')
    return render(request, 'cadastro/editar_video.html', {'video': video, 'categorias': categorias})


def excluir_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    video.delete()
    return redirect('listar_videos')
