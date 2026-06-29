// js/app.js

// Recuperar carrito desde localStorage o iniciar vacío
let carrito = JSON.parse(localStorage.getItem("carrito")) || [];

// Referencias al DOM
const contador = document.querySelector("#contador");
const listaCarrito = document.querySelector("#listaCarrito");
const totalCompra = document.querySelector("#totalCompra");

// Función para actualizar el contador en el navbar
function actualizarContador() {
  if (contador) {
    contador.textContent = carrito.length;
  }
}

// Función para guardar en localStorage
function guardarCarrito() {
  localStorage.setItem("carrito", JSON.stringify(carrito));
}

// Función para calcular el total
function calcularTotal() {
  if (!totalCompra) return;

  let total = 0;
  carrito.forEach((producto) => {
    const precioNumerico = parseInt(
      producto.precio.replace("$", "").replace(".", "").replace(",", ""),
    );
    total += precioNumerico;
  });

  totalCompra.textContent = `$${total.toLocaleString("es-CL")}`;
}

// Función para renderizar los productos en carrito.html
function renderCarrito() {
  if (!listaCarrito) return;

  listaCarrito.innerHTML = "";

  // Mostrar mensaje si el carrito está vacío
  if (carrito.length === 0) {
    const li = document.createElement("li");
    li.className = "list-group-item text-center";
    li.textContent = "Tu carrito está vacío 🛒";
    listaCarrito.appendChild(li);

    if (totalCompra) totalCompra.textContent = "$0";
    return;
  }

  carrito.forEach((producto, index) => {
    const li = document.createElement("li");
    li.className =
      "list-group-item d-flex justify-content-between align-items-center";

    li.innerHTML = `
      <div>
        <h5 class="card-title mb-1">${producto.nombre}</h5>
        <p class="card-text mb-0">${producto.precio}</p>
      </div>
      <button class="btn btn-sm btn-danger">Eliminar</button>
    `;

    // Botón eliminar
    li.querySelector("button").addEventListener("click", () => {
      carrito.splice(index, 1);
      guardarCarrito();
      actualizarContador();
      renderCarrito();
    });

    listaCarrito.appendChild(li);
  });

  calcularTotal();
}

// Función para agregar producto al carrito
function agregarAlCarrito(producto) {
  carrito.push(producto);
  guardarCarrito();
  actualizarContador();
  renderCarrito();
}

// Detectar qué producto mostrar en detalle.html
const params = new URLSearchParams(window.location.search);
const productoParam = params.get("producto");

const detalleContainer = document.querySelector("main .row");
if (detalleContainer && productoParam) {
  let producto;

  if (productoParam === "leggings") {
    producto = {
      nombre: "Leggings Yoga",
      precio: "$19.990",
      descripcion: "Leggings cómodos y flexibles, ideales para pilates y yoga.",
      imagen: "assets/img/leggings.jpg",
    };
  } else if (productoParam === "mat") {
    producto = {
      nombre: "Mat Yoga Antideslizante",
      precio: "$24.990",
      descripcion:
        "Mat antideslizante para mayor estabilidad en tus prácticas.",
      imagen: "assets/img/mat-yoga.jpg",
    };
  } else if (productoParam === "polera") {
    producto = {
      nombre: "Polera Yoga",
      precio: "$14.990",
      descripcion:
        "Polera ligera y transpirable, perfecta para yoga y pilates.",
      imagen: "assets/img/polera-yoga.jpg",
    };
  }

  // Renderizar detalle dinámico
  detalleContainer.innerHTML = `
    <article class="col-md-6">
      <img src="${producto.imagen}" class="img-fluid" alt="${producto.nombre}" />
    </article>
    <article class="col-md-6">
      <h2 class="card-title">${producto.nombre}</h2>
      <p class="card-text">${producto.descripcion}</p>
      <p class="card-text"><strong>${producto.precio}</strong></p>
      <button class="btn btn-primary" id="agregarCarrito">Agregar al carrito</button>
    </article>
  `;

  // Activar botón agregar
  const botonAgregar = document.querySelector("#agregarCarrito");
  botonAgregar.addEventListener("click", () => {
    agregarAlCarrito(producto);
    alert("Producto agregado al carrito");
  });
}

// Inicializar al cargar la página
actualizarContador();
renderCarrito();
