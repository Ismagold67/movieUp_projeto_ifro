from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('cadastro/', views.cadastro, name="cadastro"),
    path('sobre/', views.sobre, name="sobre"),
    path('home/', views.home, name="home"),
    path('alterar/', views.alterar, name="alterar"),
    path('visualizar/', views.visualizar, name="visualizar"),

    path('alterar/', views.alterar, name="alterar"),
    path('editar/<int:pk>', views.editar, name="editar"),
    path('editar_verificacao/<int:pk>', views.editar_verificacao, name="editar_verificacao"),
    path('excluir/<int:pk>', views.excluir, name="excluir"),
    path('excluir_verificacao/<int:pk>', views.excluir_verificacao, name="excluir_verificacao"),
    
    path('contato/', views.contato, name="contato"),
    path('cadastrar_filme/', views.cadastrar_filme, name="cadastrar_filme"),
    path('logout/', views.logout, name="logout"),
]