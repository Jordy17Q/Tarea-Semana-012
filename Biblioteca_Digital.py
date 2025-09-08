# -----------------------------------------------
# Sistema de Gestión de Biblioteca Digital
# Autor: Jordy
# Descripción: Este archivo contiene las clases y métodos
# necesarios para administrar libros, usuarios y préstamos
# en una biblioteca digital.
# -----------------------------------------------

# -------------------------------
# Clase Libro
# -------------------------------
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Se usa una tupla para autor y título porque son datos inmutables
        self.info = (autor, titulo)
        self.categoria = categoria
        self.isbn = isbn  # Identificador único del libro

    def __str__(self):
        # Representación legible del libro
        return f"{self.info[1]} por {self.info[0]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


# -------------------------------
# Clase Usuario
# -------------------------------
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario  # Debe ser único
        self.libros_prestados = []  # Lista de libros actualmente prestados

    def __str__(self):
        # Representación legible del usuario
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


# -------------------------------
# Clase Biblioteca
# -------------------------------
class Biblioteca:
    def __init__(self):
        # Diccionario para acceso rápido a libros por ISBN
        self.libros_disponibles = {}       # ISBN: Libro
        # Diccionario para acceso rápido a usuarios por ID
        self.usuarios_registrados = {}     # ID: Usuario
        # Conjunto para asegurar unicidad de IDs
        self.ids_usuarios = set()

    # ---------------------------
    # Añadir un libro a la biblioteca
    # ---------------------------
    def agregar_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"📘 Libro añadido: {libro}")
        else:
            print("⚠️ El libro ya existe en la biblioteca.")

    # ---------------------------
    # Quitar un libro por ISBN
    # ---------------------------
    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"🗑️ Libro con ISBN {isbn} eliminado.")
        else:
            print("⚠️ El libro no se encuentra en la biblioteca.")

    # ---------------------------
    # Registrar un nuevo usuario
    # ---------------------------
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios_registrados[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"👤 Usuario registrado: {usuario}")
        else:
            print("⚠️ ID de usuario ya registrado.")

    # ---------------------------
    # Dar de baja a un usuario
    # ---------------------------
    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            del self.usuarios_registrados[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print(f"🗑️ Usuario con ID {id_usuario} eliminado.")
        else:
            print("⚠️ Usuario no encontrado.")

    # ---------------------------
    # Prestar un libro a un usuario
    # ---------------------------
    def prestar_libro(self, id_usuario, isbn):
        usuario = self.usuarios_registrados.get(id_usuario)
        libro = self.libros_disponibles.get(isbn)
        if usuario and libro:
            usuario.libros_prestados.append(libro)
            del self.libros_disponibles[isbn]
            print(f"📚 Libro prestado: {libro} a {usuario.nombre}")
        else:
            print("⚠️ Usuario o libro no disponible.")

    # ---------------------------
    # Devolver un libro prestado
    # ---------------------------
    def devolver_libro(self, id_usuario, isbn):
        usuario = self.usuarios_registrados.get(id_usuario)
        if usuario:
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros_disponibles[isbn] = libro
                    print(f"✅ Libro devuelto: {libro}")
                    return
            print("⚠️ El usuario no tiene este libro prestado.")
        else:
            print("⚠️ Usuario no encontrado.")

    # ---------------------------
    # Buscar libros por criterio
    # ---------------------------
    def buscar_libros(self, criterio, valor):
        resultados = []
        for libro in self.libros_disponibles.values():
            if criterio == "titulo" and valor.lower() in libro.info[1].lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.info[0].lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    # ---------------------------
    # Listar libros prestados a un usuario
    # ---------------------------
    def listar_libros_prestados(self, id_usuario):
        usuario = self.usuarios_registrados.get(id_usuario)
        if usuario:
            return usuario.libros_prestados
        else:
            print("⚠️ Usuario no encontrado.")
            return []