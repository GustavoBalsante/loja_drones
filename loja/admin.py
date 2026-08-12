from django.contrib import admin
from .models import Drone, Pedido

@admin.register(Drone)
class DroneAdmin(admin.ModelAdmin):
    list_display = ('marca', 'nome', 'preco', 'estoque', 'autonomia_minutos')
    search_fields = ('nome', 'marca')
    list_filter = ('marca',)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    # Colunas visíveis no painel administrativo de vendas
    list_display = ('id', 'nome', 'email', 'cidade', 'total', 'criado_em')
    search_fields = ('nome', 'email', 'cidade')
    list_filter = ('criado_em',)