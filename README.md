# TotalCalm Ecommerce

Aplicación web desarrollada en Django para una tienda de ropa deportiva enfocada en yoga y pilates.  
Incluye catálogo de productos, detalle, carrito de compras y formulario de contacto.

---

## Instalación y ejecución

### Clonar el repositorio

git clone https://github.com/Lidinformatic/totalcalm-ecommerce.git
cd totalcalm-ecommerce

- Crear entorno virtual

python -m venv venv

- Activar entorno virtual
  En Windows (PowerShell):

venv\Scripts\activate

En Linux/Mac:
source venv/bin/activate

- Instalar dependencias
  pip install -r requirements.txt

Si no tienes requirements.txt, puedes generarlo con:

pip freeze > requirements.txt

- Migrar base de datos

python manage.py migrate

- Crear superusuario (para acceder al admin)

python manage.py createsuperuser

- Ejecutar servidor de desarrollo

python manage.py runserver

Accede en tu navegador a:
http://127.0.0.1:8000

- Estructura del proyecto

totalcalm-ecommerce/
│
├── totalcalm/ # Configuración principal del proyecto
├── tienda/ # App principal (productos, carrito, contacto)
│ ├── templates/tienda/ # Templates HTML
│ ├── static/tienda/ # Archivos estáticos (CSS, JS, imágenes fijas)
│ ├── models.py # Modelos de base de datos
│ ├── views.py # Lógica de vistas
│ └── urls.py # Rutas de la app
│
├── media/productos/ # Imágenes dinámicas subidas desde el admin
├── db.sqlite3 # Base de datos local
├── manage.py # Comando principal de Django
├── requirements.txt # Dependencias del proyecto
└── README.md # Documentación del proyecto

- Funcionalidades

Home con productos destacados
Página de detalle de producto
Carrito de compras con validación de stock
Formulario de contacto
Panel de administración para gestionar productos y categorías

Panel de administración para gestionar productos y consultas.

- Tecnologías
  Python 3.14.3
  Django 6.0.5
  Bootstrap 5.3.2
  SQLite (por defecto, fácilmente reemplazable por MySQL/PostgreSQL)

## Credenciales de prueba

Para probar el sistema, cree los siguientes usuarios en el admin de Django:

- **Admin**
  Usuario: Lidia  
  Clave: Lidi0354

- **Cliente**
  Usuario: cliente  
  Clave: cl123456

> Nota: Estos usuarios no vienen incluidos en la base de datos del repositorio. Deben crearse manualmente con `python manage.py createsuperuser` o desde el panel de administración.
