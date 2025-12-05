"""
URL configuration for BD2_Trabalhofinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from .App import views
from django.shortcuts import redirect
from django.http import HttpResponseForbidden

# Decorador de proteção para admin
def admin_protected(view_func):
    def wrapper(request, *args, **kwargs):
        # VERIFICA EXATAMENTE COMO NO TEU TEMPLATE
        if request.user.is_authenticated and request.user.is_staff:
            # Se está autenticado E é staff, permite o acesso
            return view_func(request, *args, **kwargs)
        else:
            # Se não, redireciona ou mostra erro
            if not request.user.is_authenticated:
                # Não está autenticado - redireciona para login
                return redirect(f'/login/?next={request.path}')
            else:
                # Está autenticado mas não é staff - mostra erro
                return HttpResponseForbidden("""
                <div style="text-align: center; padding: 50px; font-family: Arial, sans-serif;">
                    <h1 style="color: #dc3545;">Acesso Negado</h1>
                    <p>Apenas administradores podem aceder a esta área.</p>
                    <p><a href="/">Voltar à página inicial</a></p>
                </div>
                """)
    return wrapper

# URL patterns para as views protegidas
admin_urlpatterns = [
    # PERFIL ADMIN - se necessário
    # path('', views.admin_dashboard, name='admin_dashboard'),
    
    # POSIÇÕES DE CAMPO DOS JOGADORES
    path('posicoes/', admin_protected(views.listar_posicoes), name='listar_posicoes'),
    path('posicoes/adicionar/', admin_protected(views.adicionar_posicao), name='adicionar_posicao'),
    path('posicoes/editar/<str:id>/', admin_protected(views.editar_posicao), name='editar_posicao'),
    path('posicoes/apagar/<str:id>/', admin_protected(views.apagar_posicao), name='apagar_posicao'),
    
    # ASSOCIAÇÕES DE FUTEBOL
    path('associacoes/', admin_protected(views.listar_associacoes), name='listar_associacoes'),
    path('associacoes/adicionar/', admin_protected(views.adicionar_associacao), name='adicionar_associacao'),
    path('associacoes/editar/<str:id>/', admin_protected(views.editar_associacao), name='editar_associacao'),
    path('associacoes/apagar/<str:id>/', admin_protected(views.apagar_associacao), name='apagar_associacao'),
    
    # FORMATOS DE COMPETIÇÃO
    path('formatos/', admin_protected(views.listar_formatos), name='listar_formatos'),
    path('formatos/adicionar/', admin_protected(views.adicionar_formato), name='adicionar_formato'),
    path('formatos/editar/<str:id>/', admin_protected(views.editar_formato), name='editar_formato'),
    path('formatos/apagar/<str:id>/', admin_protected(views.apagar_formato), name='apagar_formato'),
    
    # ESTÁDIOS
    path('estadios/', admin_protected(views.listar_estadios), name='listar_estadios'),
    path('estadios/adicionar/', admin_protected(views.adicionar_estadio), name='adicionar_estadio'),
    path('estadios/editar/<str:id>/', admin_protected(views.editar_estadio), name='editar_estadio'),
    path('estadios/apagar/<str:id>/', admin_protected(views.apagar_estadio), name='apagar_estadio'),
    
    # JOGADORES
    path('jogadores/', admin_protected(views.listar_jogadores), name='listar_jogadores'),
    path('jogadores/adicionar/', admin_protected(views.adicionar_jogador), name='adicionar_jogador'),
    path('jogadores/editar/<str:id>/', admin_protected(views.editar_jogador), name='editar_jogador'),
    path('jogadores/apagar/<str:id>/', admin_protected(views.apagar_jogador), name='apagar_jogador'),
    
    # CLUBES  
    path('clubes/', admin_protected(views.listar_clubes), name='listar_clubes'),
    path('clubes/adicionar/', admin_protected(views.adicionar_clube), name='adicionar_clube'),
    path('clubes/editar/<str:id>/', admin_protected(views.editar_clube), name='editar_clube'),
    path('clubes/apagar/<str:id>/', admin_protected(views.apagar_clube), name='apagar_clube'),
    
    # EQUIPAS
    path('equipas/', admin_protected(views.listar_equipas), name='listar_equipas'),
    path('equipas/adicionar/', admin_protected(views.adicionar_equipa), name='adicionar_equipa'),
    path('equipas/editar/<str:id>/', admin_protected(views.editar_equipa), name='editar_equipa'),
    path('equipas/apagar/<str:id>/', admin_protected(views.apagar_equipa), name='apagar_equipa'),
    
    # COMPETIÇÕES
    path('competicoes/', admin_protected(views.listar_competicoes), name='listar_competicoes'),
    path('competicoes/adicionar/', admin_protected(views.adicionar_competicao), name='adicionar_competicao'),
    path('competicoes/editar/<str:id>/', admin_protected(views.editar_competicao), name='editar_competicao'),
    path('competicoes/apagar/<str:id>/', admin_protected(views.apagar_competicao), name='apagar_competicao'),
    
    # JOGOS
    path('jogos/', admin_protected(views.listar_jogos), name='listar_jogos'),
    path('jogos/adicionar/', admin_protected(views.adicionar_jogo), name='adicionar_jogo'),    
    path('jogos/editar/<str:id>/', admin_protected(views.editar_jogo), name='editar_jogo'),
    path('jogos/apagar/<str:id>/', admin_protected(views.apagar_jogo), name='apagar_jogo'),
    
    # ESTATISTICAS JOGOS
    path('jogos/estatisticas/<str:id>/', admin_protected(views.listar_estatisticas), name='listar_estatisticas'),
    
    ## Golos
    path('jogos/estatisticas/golo/adicionar/<str:id>/', admin_protected(views.adicionar_golo), name='adicionar_golo'),
    path('jogos/estatisticas/golo/editar/<str:id>/', admin_protected(views.editar_golo), name='editar_golo'),
    path('jogos/estatisticas/golo/apagar/<str:id>/', admin_protected(views.apagar_golo), name='apagar_golo'),
    
    ## Penaltis  
    path('jogos/estatisticas/penalti/adicionar/<str:id>/', admin_protected(views.adicionar_penalti), name='adicionar_penalti'),
    path('jogos/estatisticas/penalti/editar/<str:id>/', admin_protected(views.editar_penalti), name='editar_penalti'),
    path('jogos/estatisticas/penalti/apagar/<str:id>/', admin_protected(views.apagar_penalti), name='apagar_penalti'),
    
    ## Faltas  
    path('jogos/estatisticas/falta/adicionar/<str:id>/', admin_protected(views.adicionar_falta), name='adicionar_falta'),
    path('jogos/estatisticas/falta/editar/<str:id>/', admin_protected(views.editar_falta), name='editar_falta'),
    path('jogos/estatisticas/falta/apagar/<str:id>/', admin_protected(views.apagar_falta), name='apagar_falta'),
    
    ## Substituições
    path('jogos/estatisticas/substituicao/adicionar/<str:id>/', admin_protected(views.adicionar_substituicao), name='adicionar_substituicao'),
    path('jogos/estatisticas/substituicao/editar/<str:id>/', admin_protected(views.editar_substituicao), name='editar_substituicao'),
    path('jogos/estatisticas/substituicao/apagar/<str:id>/', admin_protected(views.apagar_substituicao), name='apagar_substituicao'),
]

# URL patterns principais
urlpatterns = [
    path('', views.home, name='home'),
    path('bd/conectividade', views.lista_utilizadores, name='lista_utilizadores'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    
    # PERFIL
    path('perfil/', views.ver_perfil, name='perfil'),
    path('perfil/editar/dados', views.editar_perfil, name='editar_perfil'),
    path("perfil/editar/senha/", views.editar_senha, name="editar_senha"),
    
    # ASSOCIAÇÕES PÚBLICAS
    path('associacoes/', views.todas_associacoes, name='todas_associacoes'),
    path('associacoes/<str:id>/', views.detalhes_associacao, name='detalhes_associacao'),
    
    # ESTÁDIOS PÚBLICOS
    path('estadios/', views.todos_estadios, name='todos_estadios'),
    path('estadios/<str:id>/', views.detalhes_estadio, name='detalhes_estadio'),
    
    # JOGADORES PÚBLICOS
    path('jogadores/', views.todos_jogadores, name='todos_jogadores'),
    path('jogadores/<str:id>/', views.detalhes_jogador, name='detalhes_jogador'),
    
    # CLUBES PÚBLICOS
    path('clubes/', views.todos_clubes, name='todos_clubes'),
    path('clubes/<str:id>/', views.detalhes_clube, name='detalhes_clube'),
    
    # EQUIPAS - CLUBES - JOGADORES (APIs)
    path('api/equipas-por-clube/<str:clube_id>/', views.get_equipas_por_clube, name='equipas_por_clube'),
    path('api/jogadores-por-clube/', views.get_jogadores_por_clube, name='get_jogadores_por_clube'),
    
    # COMPETIÇÕES PÚBLICAS
    path('competicoes/<str:id>/', views.detalhes_competicao, name='detalhes_competicao'),
    path('competicoes/', views.todas_competicoes, name='todas_competicoes'),
    
    # JOGOS PÚBLICOS
    path('jogos/<str:id>/', views.detalhes_jogo, name='detalhes_jogo'),
    path('jogos/', views.todos_jogos, name='todos_jogos'),
    
    # CLUBES FAVORITOS
    path('favorito_clube/<str:clube_id>/', views.favorito_clube, name='favorito_clube'),
    path('remover_favorito/<str:clube_id>/', views.remover_favorito, name='remover_favorito'),
    
    # ÁREA ADMIN (todas as rotas protegidas)
    path('admin/', include(admin_urlpatterns)),
]