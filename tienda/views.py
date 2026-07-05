from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Producto, Categoria, Pedido, PedidoItem

# Home con productos destacados
def home(request):
    productos = Producto.objects.all()[:3]
    return render(request, 'tienda/home.html', {'productos': productos})

# Catálogo agrupado por categorías (solo usuarios logueados)
@login_required
def catalogo(request):
    categorias = Categoria.objects.prefetch_related('productos').all()
    return render(request, 'tienda/catalogo.html', {'categorias': categorias})

# Detalle de producto
@login_required
def detalle(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'tienda/detalle.html', {'producto': producto})

# Agregar producto al carrito
@login_required
def agregar_carrito(request, id):
    producto = get_object_or_404(Producto, id=id)
    carrito = request.session.get('carrito', {})

    cantidad = int(request.POST.get('cantidad', 1))
    if cantidad < 1:
        messages.error(request, "La cantidad debe ser mayor a 0.")
        return redirect('detalle', id=id)

    if cantidad > producto.stock:
        messages.error(request, f"No hay suficiente stock de {producto.nombre}. Stock disponible: {producto.stock}")
        return redirect('detalle', id=id)

    if str(id) in carrito:
        nueva_cantidad = carrito[str(id)]['cantidad'] + cantidad
        if nueva_cantidad > producto.stock:
            messages.error(request, f"No puedes agregar más de {producto.stock} unidades de {producto.nombre}.")
            return redirect('detalle', id=id)
        carrito[str(id)]['cantidad'] = nueva_cantidad
    else:
        carrito[str(id)] = {
            'nombre': producto.nombre,
            'precio': float(producto.precio),
            'cantidad': cantidad,
            'imagen': producto.imagen.url,
            'stock': producto.stock,
        }

    request.session['carrito'] = carrito
    messages.success(request, f"{producto.nombre} agregado al carrito.")
    return redirect('carrito')

# Carrito dinámico
@login_required
def carrito(request):
    carrito = request.session.get('carrito', {})
    total = 0
    for item in carrito.values():
        item['subtotal'] = item['precio'] * item['cantidad']
        total += item['subtotal']
    return render(request, 'tienda/carrito.html', {'carrito': carrito, 'total': total})

# Quitar producto
@login_required
def quitar_carrito(request, id):
    carrito = request.session.get('carrito', {})
    if str(id) in carrito:
        del carrito[str(id)]
        request.session['carrito'] = carrito
        messages.info(request, "Producto eliminado del carrito.")
    return redirect('carrito')

# Confirmar compra
@login_required
def confirmar_compra(request):
    carrito = request.session.get('carrito', {})
    if not carrito:
        messages.error(request, "El carrito está vacío.")
        return redirect('carrito')

    pedido = Pedido.objects.create(usuario=request.user, total=0)
    total = 0

    for id, item in carrito.items():
        producto = get_object_or_404(Producto, id=id)
        cantidad = item['cantidad']
        precio = producto.precio
        subtotal = cantidad * precio

        PedidoItem.objects.create(
            pedido=pedido,
            producto=producto,
            cantidad=cantidad,
            precio=precio
        )
        total += subtotal

        producto.stock -= cantidad
        producto.save()

    pedido.total = total
    pedido.save()

    request.session['carrito'] = {}
    return render(request, 'tienda/confirmacion.html', {'pedido': pedido})

# Contacto
def contacto(request):
    return render(request, 'tienda/contacto.html')

# Actualizar carrito
@login_required
def actualizar_carrito(request, id):
    carrito = request.session.get('carrito', {})
    if str(id) in carrito:
        nueva_cantidad = int(request.POST.get('cantidad', 1))
        if nueva_cantidad < 1:
            messages.error(request, "La cantidad debe ser mayor a 0.")
        elif nueva_cantidad > carrito[str(id)]['stock']:
            messages.error(request, f"No puedes superar el stock disponible ({carrito[str(id)]['stock']}).")
        else:
            carrito[str(id)]['cantidad'] = nueva_cantidad
            messages.success(request, "Cantidad actualizada correctamente.")
        request.session['carrito'] = carrito
    return redirect('carrito')

# Registro de usuario
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cuenta creada correctamente. Ahora puedes iniciar sesión.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'tienda/signup.html', {'form': form})


