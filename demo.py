"""
demo.py
Script para demostrar el uso en vivo de las operaciones CRUD
y poblar el catálogo con productos iniciales de prueba.
"""

from product_manager import ProductManager


def ejecutar_demostracion():
    # Inicializamos el gestor conectado al archivo productos.json
    manager = ProductManager(archivo="productos.json")

    print("\n" + "=" * 55)
    print("      DEMOSTRACIÓN DE OPERACIONES CRUD EN PYTHON")
    print("=" * 55)

    # 1. CREAR PRODUCTOS
    print("\n--> 1. CREANDO PRODUCTOS DE PRUEBA...")
    productos_a_crear = [
        ("1", "Laptop Lenovo IdeaPad", "Core i5, 16GB RAM, 512GB SSD", 2450000.0, 6),
        ("2", "Mouse Inalámbrico Logitech", "Óptico ergonómico USB", 75000.0, 25),
        ("3", "Teclado Mecánico Redragon", "RGB switch azul", 190000.0, 14),
        ("4", "Monitor LG 24 Pulgadas", "Panel IPS FHD 75Hz", 520000.0, 8),
    ]

    for id_p, nombre, desc, precio, cant in productos_a_crear:
        try:
            p = manager.crear_producto(id_p, nombre, desc, precio, cant)
            print(f"  [+] Creado: ID {p['id']} - {p['nombre']} (${p['precio']:,.2f})")
        except ValueError as e:
            print(f"  [!] Nota: {e}")

    # 2. LISTAR PRODUCTOS (LEER TODOS)
    print("\n--> 2. LISTANDO CATÁLOGO COMPLETO...")
    catalogo = manager.listar_productos()
    print(f"  Total de productos: {len(catalogo)}\n")
    print(f"  {'ID':<5} | {'Nombre':<30} | {'Precio':<14} | {'Stock'}")
    print("  " + "-" * 60)
    for p in catalogo:
        print(f"  {p['id']:<5} | {p['nombre']:<30} | ${p['precio']:>12,.2f} | {p['cantidad']:>4}")

    # 3. CONSULTAR UN PRODUCTO POR ID (LEER UNO)
    print("\n--> 3. CONSULTANDO PRODUCTO CON ID '2'...")
    prod_leido = manager.obtener_producto("2")
    print(f"  Encontrado: {prod_leido['nombre']} - Stock actual: {prod_leido['cantidad']}")

    # 4. ACTUALIZAR UN PRODUCTO
    print("\n--> 4. ACTUALIZANDO PRECIO Y STOCK DEL PRODUCTO ID '2'...")
    actualizado = manager.actualizar_producto("2", precio=69900.0, cantidad=35)
    print(f"  Nuevo precio: ${actualizado['precio']:,.2f} | Nuevo stock: {actualizado['cantidad']}")

    # 5. ELIMINAR UN PRODUCTO
    print("\n--> 5. PROBANDO ELIMINACIÓN (ID '4')...")
    manager.eliminar_producto("4")
    print("  Producto ID '4' eliminado correctamente.")

    # 6. VERIFICAR LISTADO FINAL
    print("\n--> 6. CATÁLOGO FINAL GUARDADO EN 'productos.json':")
    for p in manager.listar_productos():
        print(f"  * [{p['id']}] {p['nombre']} (${p['precio']:,.2f}) - Stock: {p['cantidad']}")

    print("\n" + "=" * 55)
    print("  DEMOSTRACIÓN FINALIZADA CON ÉXITO")
    print("=" * 55)


if __name__ == "__main__":
    ejecutar_demostracion()
