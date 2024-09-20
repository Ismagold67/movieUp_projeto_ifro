from django.shortcuts import render, redirect
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django, logout as logout_django
from .models import Filme
from django.urls import reverse

def login(request):
    if request.method == "GET":
        return render(request, 'usuarios/login.html')
    else:
        username = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(username = username, password = senha)

        if user:
            login_django(request, user)
            return render(request, 'usuarios/home.html')
        else:
            return render(request, 'usuarios/login.html')

def cadastro(request):
    if request.method == "GET":
        return render(request, 'usuarios/cadastro.html')
    else:
        username = request.POST.get('email')
        email = request.POST.get('email')
        password = request.POST.get('senha')
        first_name = request.POST.get('nome')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Usuário já existe!')
        else:
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name)
            user.save()

            return render(request, 'usuarios/login.html')
        
def cadastrar_filme(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request, 'usuarios/cadastrar_filme.html')
        else:
            return render(request, 'usuarios/login.html')
    else:
        filme = Filme()

        filme.usuario = request.user.first_name
        filme.titulo = request.POST.get('nome')
        filme.situacao = request.POST.get('situacao')
        filme.genero = request.POST.get('genero')  
        filme.sinopse = request.POST.get('sinopse')
        filme.duracao = request.POST.get('duracao')
        filme.data_lancamento = request.POST.get('data_lancamento')
        filme.url_img = request.POST.get('url_img')

        filme_verificado = Filme.objects.filter(usuario=filme.usuario, titulo=filme.titulo).first()

        if filme_verificado:
            return HttpResponse("Este filme ja foi cadastrado!!.")
        else:
            filme.save()
            return render(request, 'usuarios/home.html')
        
def home(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request, 'usuarios/home.html')
        else:
            return redirect('login')
    
def alterar(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            lista_filmes = Filme.objects.filter(usuario = request.user.first_name)
            dicionarios = {"lista_filmes": lista_filmes}
            return render(request, 'usuarios/alterar.html', dicionarios)
        else:
            return render(request, 'usuarios/login.html')
    else:
        return redirect('login')
    
def editar(request, pk):
    if request.method == "POST":
        if request.user.is_authenticated:
            
            titulo = request.POST.get('nome')
            situacao = request.POST.get('situacao') 
            genero = request.POST.get('genero')
            sinopse = request.POST.get('sinopse')
            duracao = request.POST.get('duracao')
            data_lancamento = request.POST.get('data_lancamento')
            url_img = request.POST.get('url_img')


            Filme.objects.filter(pk=pk).update(
                titulo = titulo,
                situacao = situacao,
                genero = genero,
                sinopse = sinopse,
                duracao = duracao,
                data_lancamento = data_lancamento,
                url_img = url_img
            )

            return HttpResponseRedirect(reverse('alterar'))
        else:
            return render(request, 'usuarios/login.html')
        
def editar_verificacao(request, pk):
    lista_situacao = ["Em cartaz", "Em breve", "Formato digital"]
    lista_generos = [
        "Ação",
        "Aventura",
        "Comédia",
        "Drama",
        "Ficção Científica",
        "Suspense",
        "Terror"
    ]
    if request.method == "GET":
        if request.user.is_authenticated:
            lista_filmes = Filme.objects.get(pk=pk)
            if lista_filmes.situacao in lista_situacao:
                lista_situacao.remove(lista_filmes.situacao)
            if lista_filmes.genero in lista_generos:
                lista_generos.remove(lista_filmes.genero)
            dicionario_filmes = {"lista_filmes": lista_filmes, "lista_situacao": lista_situacao, "lista_generos": lista_generos}
            return render(request, 'usuarios/editar.html', dicionario_filmes)
        else:
            return redirect('login')
        
def excluir_verificacao(request, pk):
    if request.method == "GET":
        if request.user.is_authenticated:
            lista_filmes = Filme.objects.get(pk=pk)
            dicionario_filmes = {"lista_filmes": lista_filmes}
            return render(request, 'usuarios/excluir.html', dicionario_filmes)
        else:
            return redirect('login')
    else:
        return redirect('login')
        
def excluir(request, pk):
    if request.method == "GET":
        if request.user.is_authenticated:
            filme_selecionado = Filme.objects.get(pk=pk)
            filme_selecionado.delete()
            return HttpResponseRedirect(reverse('alterar'))
        else:
            return redirect('login')
    
def visualizar(request):
    lista_opcoes = ["Todos os filmes", "Em cartaz", "Em breve", "Formato digital"]
    if request.method == "GET":
        if request.user.is_authenticated:
            lista_filmes = Filme.objects.filter(usuario= request.user.first_name)
            dicionario_filmes = {"lista_filmes": lista_filmes, "lista_opcoes":lista_opcoes}
            return render(request, 'usuarios/visualizar.html', dicionario_filmes)
        else:
            return redirect('login')
    else:
        tipo_filtro = request.POST.get("tipo_filtro")
        if tipo_filtro == "Todos os filmes":
            if tipo_filtro in lista_opcoes:
                temp = tipo_filtro
                lista_opcoes.remove(temp)
                lista_opcoes.insert(0, temp)
            lista_filmes = Filme.objects.filter(usuario=request.user.first_name)
            dicionario_filmes = {"lista_filmes":lista_filmes, "lista_opcoes": lista_opcoes}
            return render(request, 'usuarios/visualizar.html', dicionario_filmes)
        else:
            if tipo_filtro in lista_opcoes:
                temp = tipo_filtro
                lista_opcoes.remove(temp)
                lista_opcoes.insert(0, temp)
            lista_filmes = Filme.objects.filter(usuario=request.user.first_name, situacao=tipo_filtro)
            dicionario_filmes_filtrados = {"lista_filmes": lista_filmes, "lista_opcoes": lista_opcoes}
            return render(request, 'usuarios/visualizar.html', dicionario_filmes_filtrados)

def sobre(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request, 'usuarios/sobre.html')
        else:
            return render(request, 'usuarios/login.html')

def contato(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request, "usuarios/contato.html")
        else:
            return render(request, 'usuarios/login.html')
    else:
        return HttpResponse("Método não suportado.", status=405)

def logout(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            logout_django(request)
            return render(request, 'usuarios/login.html')
        else:
            return render(request, 'usuarios/login.html')
