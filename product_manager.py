"""
Módulo para la gestión CRUD de productos.
Permite crear, leer, actualizar y eliminar productos con validaciones y
soporte opcional para persistencia en archivo JSON o almacenamiento en memoria.
"""

import json
import os
from typing import Dict, List, Optional, Any


class ProductManager:
    """Administrador de productos en memoria con opción de persistencia JSON."""

    def __init__(self, storage_file: Optional[str] = None):
        """
        Inicializa el gestor.
        Si storage_file es proporcionado, se cargará y guardará en dicho archivo JSON.
        De lo contrario, opera 100% en memoria.
        """
        self.storage_file = storage_file
        self.products: Dict[str, Dict[str, Any]] = {}
        if self.storage_file and os.path.exists(self.storage_file):
            self._load_from_file()

    def _save_to_file(self) -> None:
        """Guarda el estado actual de los productos en el archivo JSON configurado."""
        if self.storage_file:
            with open(self.storage_file, "w", encoding="utf-8") as f:
                json.dump(self.products, f, indent=4, ensure_ascii=False)

    def _load_from_file(self) -> None:
        """Carga productos desde el archivo JSON configurado."""
        if self.storage_file and os.path.exists(self.storage_file):
            with open(self.storage_file, "r", encoding="utf-8") as f:
                try:
                    self.products = json.load(f)
                except json.JSONDecodeError:
                    self.products = {}

    def crear_producto(self, id_prod: Any, nombre: str, descripcion: str, precio: float, cantidad: int) -> Dict[str, Any]:
        """
        Crea un nuevo producto en el catálogo.

        Validaciones:
        - id_prod no debe estar vacío ni repetido.
        - nombre no debe estar vacío.
        - precio debe ser mayor o igual a 0.
        - cantidad debe ser mayor o igual a 0.
        """
        prod_id_str = str(id_prod).strip()
        if not prod_id_str:
            raise ValueError("El ID del producto no puede estar vacío.")

        if prod_id_str in self.products:
            raise ValueError(f"Ya existe un producto con el ID '{prod_id_str}'.")

        if not nombre or not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")

        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

        nuevo_producto = {
            "id": prod_id_str,
            "nombre": nombre.strip(),
            "descripcion": descripcion.strip() if descripcion else "",
            "precio": float(precio),
            "cantidad": int(cantidad)
        }

        self.products[prod_id_str] = nuevo_producto
        self._save_to_file()
        return nuevo_producto

    def obtener_producto(self, id_prod: Any) -> Dict[str, Any]:
        """Obtiene un producto por su ID. Lanza KeyError si no existe."""
        prod_id_str = str(id_prod).strip()
        if prod_id_str not in self.products:
            raise KeyError(f"Producto con ID '{prod_id_str}' no encontrado.")
        return self.products[prod_id_str]

    def listar_productos(self) -> List[Dict[str, Any]]:
        """Retorna una lista con todos los productos registrados."""
        return list(self.products.values())

    def actualizar_producto(
        self,
        id_prod: Any,
        nombre: Optional[str] = None,
        descripcion: Optional[str] = None,
        precio: Optional[float] = None,
        cantidad: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Actualiza los campos de un producto existente.
        Lanza KeyError si el producto no existe o ValueError si los datos son inválidos.
        """
        prod_id_str = str(id_prod).strip()
        if prod_id_str not in self.products:
            raise KeyError(f"No se puede actualizar: producto con ID '{prod_id_str}' no existe.")

        producto = self.products[prod_id_str]

        if nombre is not None:
            if not nombre.strip():
                raise ValueError("El nombre no puede estar vacío.")
            producto["nombre"] = nombre.strip()

        if descripcion is not None:
            producto["descripcion"] = descripcion.strip()

        if precio is not None:
            if precio < 0:
                raise ValueError("El precio no puede ser negativo.")
            producto["precio"] = float(precio)

        if cantidad is not None:
            if cantidad < 0:
                raise ValueError("La cantidad no puede ser negativa.")
            producto["cantidad"] = int(cantidad)

        self._save_to_file()
        return producto

    def eliminar_producto(self, id_prod: Any) -> bool:
        """Elimina un producto por su ID. Lanza KeyError si no existe."""
        prod_id_str = str(id_prod).strip()
        if prod_id_str not in self.products:
            raise KeyError(f"No se puede eliminar: producto con ID '{prod_id_str}' no existe.")

        del self.products[prod_id_str]
        self._save_to_file()
        return True
