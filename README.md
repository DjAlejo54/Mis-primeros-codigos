# Proyecto Final - Inventario de Productos

Este proyecto fue realizado como entrega final del curso de Inciciacion Inicial de Programación en Python.  
Consiste en una aplicación de consola para gestionar productos de un inventario utilizando una base de datos SQLite.

---

## 📦 Características del proyecto

- Registro de nuevos productos
- Visualización de productos existentes
- Modificación de productos por ID
- Eliminación de productos por ID
- Búsqueda por ID
- Reporte de productos con bajo stock
- Validaciones de entradas
- Interfaz por consola con colores (usando `colorama`)

---

## 🗃️ Base de datos

El proyecto utiliza una base de datos llamada `inventario.db` que contiene una tabla llamada `productos` con los siguientes campos:

- `id` (clave primaria, autoincremental)
- `nombre` (texto, no nulo)
- `descripcion` (texto)
- `cantidad` (entero, no nulo)
- `precio` (real, no nulo)
- `categoria` (texto)

---

## 🧪 Requisitos para ejecutarlo

1. Tener instalado Python 3
2. Instalar el módulo colorama:
   pip install colorama
3. Ejecutar el script:
   python proyecto_inventario.py

---

## 🎨 Tecnologías utilizadas

- Python 3
- SQLite3 (`sqlite3`)
- Interfaz en consola
- `colorama` para mejorar la experiencia del usuario

---

## 👨‍💻 Autor
Agustin Alejo Iovino  
