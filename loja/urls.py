from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('drone/<int:drone_id>/', views.detalhe_drone, name='detalhe_drone'),
    path('carrinho/', views.ver_carrinho, name='ver_carrinho'),
    path('carrinho/adicionar/<int:drone_id>/', views.adicionar_carrinho, name='adicionar_carrinho'),
    path('carrinho/remover/<int:drone_id>/', views.remover_carrinho, name='remover_carrinho'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('drone/<int:drone_id>/', views.detalhe_drone, name='detalhe_drone'),
    path('carrinho/', views.ver_carrinho, name='ver_carrinho'),
    path('carrinho/adicionar/<int:drone_id>/', views.adicionar_carrinho, name='adicionar_carrinho'),
    path('carrinho/remover/<int:drone_id>/', views.remover_carrinho, name='remover_carrinho'),
    path('checkout/', views.checkout, name='checkout'), # Nova linha
]