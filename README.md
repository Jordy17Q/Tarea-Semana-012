# Tarea-Semana-012
# 📚 Sistema de Gestión de Biblioteca Digital

Este proyecto implementa un sistema modular en Python para gestionar una biblioteca digital. Permite administrar libros, usuarios registrados y el historial de préstamos, utilizando estructuras eficientes como diccionarios, listas, tuplas y conjuntos.

---

## 🎯 Objetivo

Desarrollar una solución clara y mantenible que permita:

- Añadir y eliminar libros del catálogo
- Registrar y dar de baja usuarios
- Prestar y devolver libros
- Buscar libros por título, autor o categoría
- Listar libros prestados por usuario

---

## 🧱 Estructura del sistema

El sistema está compuesto por tres clases principales:

| Clase       | Descripción                                                                 |
|-------------|------------------------------------------------------------------------------|
| `Libro`     | Representa un libro con título, autor, categoría e ISBN. Usa tupla inmutable. |
| `Usuario`   | Representa un usuario con nombre, ID único y lista de libros prestados.       |
| `Biblioteca`| Gestiona libros disponibles, usuarios registrados y operaciones del sistema.  |

---

## 🛠️ Tecnologías utilizadas

- **Python 3.10+**
- Estructuras: `dict`, `list`, `tuple`, `set`
- Estilo modular y comentado para facilitar mantenimiento

