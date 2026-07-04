from django.contrib import admin
from .models import Producto, Categoria, Pedido, PedidoItem

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)
    ordering = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'stock', 'categoria')
    list_filter = ('categoria',)
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)

class PedidoItemInline(admin.TabularInline):
    model = PedidoItem
    extra = 0

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'fecha', 'total')
    list_filter = ('fecha', 'usuario')
    inlines = [PedidoItemInline]

@admin.register(PedidoItem)
class PedidoItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'pedido', 'producto', 'cantidad', 'precio')
    list_filter = ('pedido', 'producto')

