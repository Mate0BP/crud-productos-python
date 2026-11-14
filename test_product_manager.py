"""
test_product_manager.py
Pruebas unitarias sencillas para verificar que el CRUD funcione bien.
Usamos la librería 'unittest' que ya viene con Python.
"""

import unittest
from product_manager import ProductManager


class TestProductManager(unittest.TestCase):

    def setUp(self):
        # Creamos un manager en memoria (sin archivo) para cada prueba
        self.manager = ProductManager(archivo=None)
        # Agregamos un producto de prueba inicial
        self.manager.crear_producto("1", "Teclado", "Teclado básico USB", 45000.0, 10)

    # 1. PRUEBAS DE CREAR
    def test_crear_producto_exitoso(self):
        """Caso de éxito: Crear un producto normal con datos válidos."""
        prod = self.manager.crear_producto("2", "Mouse", "Mouse óptico", 25000.0, 15)
        self.assertEqual(prod["id"], "2")
        self.assertEqual(prod["nombre"], "Mouse")
        self.assertEqual(len(self.manager.listar_productos()), 2)

    def test_crear_producto_error_id_duplicado(self):
        """Caso de error: Intentar crear con un ID que ya existe."""
        with self.assertRaises(ValueError):
            self.manager.crear_producto("1", "Otro Teclado", "Copia", 30000.0, 5)

    def test_crear_producto_error_precio_negativo(self):
        """Caso de error: Intentar crear con precio menor a cero."""
        with self.assertRaises(ValueError):
            self.manager.crear_producto("3", "Pantalla", "LED", -50000.0, 2)

    # 2. PRUEBAS DE LEER
    def test_leer_producto_exitoso(self):
        """Caso de éxito: Buscar un producto que sí existe."""
        prod = self.manager.obtener_producto("1")
        self.assertEqual(prod["nombre"], "Teclado")
        self.assertEqual(prod["precio"], 45000.0)

    def test_leer_producto_error_no_existe(self):
        """Caso de error: Buscar un producto con un ID que no existe."""
        with self.assertRaises(KeyError):
            self.manager.obtener_producto("999")

    def test_listar_todos_los_productos(self):
        """Caso de éxito: Listar todos los productos registrados."""
        lista = self.manager.listar_productos()
        self.assertEqual(len(lista), 1)

    # 3. PRUEBAS DE ACTUALIZAR
    def test_actualizar_producto_exitoso(self):
        """Caso de éxito: Cambiar el precio y nombre de un producto."""
        actualizado = self.manager.actualizar_producto("1", nombre="Teclado Gamer", precio=60000.0)
        self.assertEqual(actualizado["nombre"], "Teclado Gamer")
        self.assertEqual(actualizado["precio"], 60000.0)

    def test_actualizar_producto_error_no_existe(self):
        """Caso de error: Intentar actualizar un producto que no existe."""
        with self.assertRaises(KeyError):
            self.manager.actualizar_producto("999", nombre="Nuevo")

    def test_actualizar_producto_error_precio_negativo(self):
        """Caso de error: Intentar actualizar poniendo precio negativo."""
        with self.assertRaises(ValueError):
            self.manager.actualizar_producto("1", precio=-100.0)

    # 4. PRUEBAS DE ELIMINAR
    def test_eliminar_producto_exitoso(self):
        """Caso de éxito: Borrar un producto que sí existe."""
        resultado = self.manager.eliminar_producto("1")
        self.assertTrue(resultado)
        self.assertEqual(len(self.manager.listar_productos()), 0)

    def test_eliminar_producto_error_no_existe(self):
        """Caso de error: Intentar borrar un producto que no existe."""
        with self.assertRaises(KeyError):
            self.manager.eliminar_producto("999")


if __name__ == "__main__":
    unittest.main()
