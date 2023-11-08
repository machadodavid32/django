"""
URL configuration for investimento project.

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
from django.urls import path
from invista import views

# Para cada página criada, temos que fazer uma função em views e adicionar esta função abaixo..
# com dados abaixo
urlpatterns = [
    path('',views.pagina_inicial),
    path('contato/', views.pagina_contato, name='contato'),
    path('minha_historia/', views.minha_historia, name='minha_historia'),
    path('novo_investimento/', views.novo_investimento, name='novo_investimento'),
    path('investimento_registrado/', views.investimento_registrado, name='investimento_registrado')
]
