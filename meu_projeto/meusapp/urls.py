from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_produtos, name='listar_produtos'),
    path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('editar/<int:pk>/', views.editar_produto, name='editar_produto'),
    path('excluir/<int:pk>/', views.excluir_produto, name='excluir_produto'),
]