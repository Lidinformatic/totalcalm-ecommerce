from django.contrib import admin
from .models import Producto, Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')          # columnas visibles
    search_fields = ('nombre',)              # buscador por nombre
    ordering = ('nombre',)                   # orden alfabético

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'stock', 'categoria')  # muestra más info
    list_filter = ('categoria',)             # filtro lateral por categoría
    search_fields = ('nombre', 'descripcion') # buscador por nombre y descripción
    ordering = ('nombre',)                   # orden alfabético
