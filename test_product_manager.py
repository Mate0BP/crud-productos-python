"""
Pruebas unitarias para ProductManager.
Cubre operaciones CRUD con casos exitosos y casos de error según los requisitos del taller.
"""

import unittest
from product_manager import ProductManager


class TestProductManager(unittest.TestCase):
    """Casos de prueba para las operaciones Crear, Leer, Actualizar y Eliminar."""

    def setUp(self):
        """Inicializa una instancia limpia en memoria para cada prueba."""
        self.manager = ProductManager()
        # Producto base de referencia para pruebas de lectura/actualización/eliminación
        self.manager.crear_producto(
            id_prod="P001",
            nombre="Laptop Gamer",
            descripcion="Laptop 16GB RAM 512GB SSD",
            precio=1200.50,
            cantidad=10
        )

    # -----------------------------
    # 1. PRUEBAS DE CREAR (CREATE)
    # -----------------------------
    def test_crear_producto_exitoso(self):
        """Caso Exitoso: Se crea un producto con datos válidos."""
        nuevo = self.manager.crear_producto(
            id_prod="P002",
            nombre="Mouse Inalámbrico",
            descripcion="Mouse ergonómico Bluetooth",
            precio=25.99,
            cantidad=50
        )
        self.assertEqual(nuevo["id"], "P002")
        self.assertEqual(nuevo["nombre"], "Mouse Inalámbrico")
        self.assertEqual(nuevo["precio"], 25.99)
        self.assertEqual(nuevo["cantidad"], 50)
        # Verificar que efectivamente está en la lista de productos
        self.assertEqual(len(self.manager.listar_productos()), 2)

    def test_crear_producto_error_id_duplicado(self):
        """Caso Error: Falla al intentar crear un producto con un ID que ya existe."""
        with self.assertRaises(ValueError) as ctx:
            self.manager.crear_producto(
                id_prod="P001",
                nombre="Otro Equipo",
                descripcion="Descripción",
                precio=500.0,
                cantidad=5
            )
        self.assertIn("Ya existe un producto con el ID", str(ctx.exception))

    def test_crear_producto_error_precio_o_cantidad_negativa(self):
        """Caso Error: Falla al crear producto con precio o cantidad negativa."""
        with self.assertRaises(ValueError):
            self.manager.crear_producto("P003", "Teclado", "Mecánico", precio=-10.0, cantidad=5)

        with self.assertRaises(ValueError):
            self.manager.crear_producto("P004", "Monitor", "4K", precio=300.0, cantidad=-2)

    # -----------------------------
    # 2. PRUEBAS DE LEER (READ)
    # -----------------------------
    def test_leer_producto_exitoso(self):
        """Caso Exitoso: Obtener los datos de un producto existente."""
        producto = self.manager.obtener_producto("P001")
        self.assertEqual(producto["id"], "P001")
        self.assertEqual(producto["nombre"], "Laptop Gamer")
        self.assertEqual(producto["precio"], 1200.50)

    def test_leer_producto_error_inexistente(self):
        """Caso Error: Lanza excepción al buscar un producto que no existe."""
        with self.assertRaises(KeyError) as ctx:
            self.manager.obtener_producto("ID_INEXISTENTE")
        self.assertIn("no encontrado", str(ctx.exception))

    def test_listar_productos_exitoso(self):
        """Caso Exitoso: Listar todos los productos registrados."""
        lista = self.manager.listar_productos()
        self.assertIsInstance(lista, list)
        self.assertEqual(len(lista), 1)

    # -----------------------------
    # 3. PRUEBAS DE ACTUALIZAR (UPDATE)
    # -----------------------------
    def test_actualizar_producto_exitoso(self):
        """Caso Exitoso: Modificar campos de un producto existente."""
        actualizado = self.manager.actualizar_producto(
            id_prod="P001",
            nombre="Laptop Gamer Pro",
            precio=1350.00,
            cantidad=8
        )
        self.assertEqual(actualizado["nombre"], "Laptop Gamer Pro")
        self.assertEqual(actualizado["precio"], 1350.00)
        self.assertEqual(actualizado["cantidad"], 8)
        # La descripción no se modificó, debe mantenerse
        self.assertEqual(actualizado["descripcion"], "Laptop 16GB RAM 512GB SSD")

    def test_actualizar_producto_error_inexistente(self):
        """Caso Error: Intentar actualizar un producto con un ID que no existe."""
        with self.assertRaises(KeyError) as ctx:
            self.manager.actualizar_producto(
                id_prod="NO_EXISTE",
                nombre="Nuevo Nombre"
            )
        self.assertIn("no existe", str(ctx.exception))

    def test_actualizar_producto_error_datos_invalidos(self):
        """Caso Error: Intentar actualizar con precio negativo."""
        with self.assertRaises(ValueError):
            self.manager.actualizar_producto(id_prod="P001", precio=-5.0)

    # -----------------------------
    # 4. PRUEBAS DE ELIMINAR (DELETE)
    # -----------------------------
    def test_eliminar_producto_exitoso(self):
        """Caso Exitoso: Eliminar un producto existente."""
        resultado = self.manager.eliminar_producto("P001")
        self.assertTrue(resultado)
        # Verificar que ya no existe
        self.assertEqual(len(self.manager.listar_productos()), 0)
        with self.assertRaises(KeyError):
            self.manager.obtener_producto("P001")

    def test_eliminar_producto_error_inexistente(self):
        """Caso Error: Intentar eliminar un producto que no existe."""
        with self.assertRaises(KeyError) as ctx:
            self.manager.eliminar_producto("ID_FANTASMA")
        self.assertIn("no existe", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
