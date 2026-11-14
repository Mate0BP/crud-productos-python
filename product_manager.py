"""
product_manager.py
Lógica básica para el CRUD de productos.
Permite crear, consultar, modificar y eliminar productos,
guardando los datos en un archivo JSON sencillo.
"""

import json
import os


class ProductManager:
    def __init__(self, archivo="productos.json"):
        # Nombre del archivo donde se guardan los productos
        self.archivo = archivo
        # Diccionario para almacenar los productos en memoria
        self.productos = {}
        # Si el archivo ya existe en la computadora, cargamos los datos
        self.cargar_datos()

    def guardar_datos(self):
        """Guarda el diccionario de productos en el archivo JSON."""
        if self.archivo:
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump(self.productos, f, indent=4, ensure_ascii=False)

    def cargar_datos(self):
        """Lee el archivo JSON para recuperar los productos guardados."""
        if self.archivo and os.path.exists(self.archivo):
            with open(self.archivo, "r", encoding="utf-8") as f:
                try:
                    self.productos = json.load(f)
                except Exception:
                    self.productos = {}

    def crear_producto(self, id_prod, nombre, descripcion, precio, cantidad):
        """Agrega un producto nuevo verificando que no esté repetido."""
        id_texto = str(id_prod).strip()

        # Validaciones básicas
        if not id_texto:
            raise ValueError("El ID no puede estar vacío.")

        if id_texto in self.productos:
            raise ValueError(f"El producto con ID '{id_texto}' ya existe.")

        if not nombre or not str(nombre).strip():
            raise ValueError("El nombre no puede estar vacío.")

        if float(precio) < 0:
            raise ValueError("El precio no puede ser negativo.")

        if int(cantidad) < 0:
            raise ValueError("La cantidad no puede ser negativa.")

        # Guardamos el producto con sus campos
        producto = {
            "id": id_texto,
            "nombre": str(nombre).strip(),
            "descripcion": str(descripcion).strip() if descripcion else "",
            "precio": float(precio),
            "cantidad": int(cantidad)
        }

        self.productos[id_texto] = producto
        self.guardar_datos()
        return producto

    def obtener_producto(self, id_prod):
        """Busca un producto por su ID."""
        id_texto = str(id_prod).strip()
        if id_texto not in self.productos:
            raise KeyError(f"No se encontró ningún producto con el ID '{id_texto}'.")
        return self.productos[id_texto]

    def listar_productos(self):
        """Devuelve una lista con todos los productos registrados."""
        return list(self.productos.values())

    def actualizar_producto(self, id_prod, nombre=None, descripcion=None, precio=None, cantidad=None):
        """Modifica los datos de un producto que ya existe."""
        id_texto = str(id_prod).strip()
        if id_texto not in self.productos:
            raise KeyError(f"No existe el producto con ID '{id_texto}' para actualizar.")

        producto = self.productos[id_texto]

        if nombre is not None:
            if not str(nombre).strip():
                raise ValueError("El nombre no puede quedar vacío.")
            producto["nombre"] = str(nombre).strip()

        if descripcion is not None:
            producto["descripcion"] = str(descripcion).strip()

        if precio is not None:
            if float(precio) < 0:
                raise ValueError("El precio no puede ser negativo.")
            producto["precio"] = float(precio)

        if cantidad is not None:
            if int(cantidad) < 0:
                raise ValueError("La cantidad no puede ser negativa.")
            producto["cantidad"] = int(cantidad)

        self.guardar_datos()
        return producto

    def eliminar_producto(self, id_prod):
        """Elimina un producto del diccionario y del archivo."""
        id_texto = str(id_prod).strip()
        if id_texto not in self.productos:
            raise KeyError(f"No existe el producto con ID '{id_texto}' para eliminar.")

        del self.productos[id_texto]
        self.guardar_datos()
        return True
