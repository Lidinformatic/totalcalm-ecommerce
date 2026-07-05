from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from tienda import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Administración
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
    path('carrito/actualizar/<int:id>/', views.actualizar_carrito, name='actualizar_carrito'),

    # Contacto
    path('contacto/', views.contacto, name='contacto'),

    # Autenticación
    path('login/', auth_views.LoginView.as_view(template_name='tienda/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    
    # Logout ahora acepta GET y redirige al home
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

# Configuración para servir archivos de media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
