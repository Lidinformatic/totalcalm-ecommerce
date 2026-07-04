from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from tienda import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', views.home, name='home'),
    path('home/', views.home, name='home_page'),

    # Catálogo y detalle
    path('catalogo/', views.catalogo, name='catalogo'),
    path('detalle/<int:id>/', views.detalle, name='detalle'),

    # Carrito
    path('carrito/', views.carrito, name='carrito'),
    path('carrito/agregar/<int:id>/', views.agregar_carrito, name='agregar_carrito'),
    path('carrito/quitar/<int:id>/', views.quitar_carrito, name='quitar_carrito'),
    path('carrito/confirmar/', views.confirmar_compra, name='confirmar_compra'),

    # Contacto
    path('contacto/', views.contacto, name='contacto'),
]

# Configuración para servir archivos de media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

