"""
Programa principal con menú interactivo por consola.
Permite interactuar con las operaciones CRUD de productos.
"""

from product_manager import ProductManager


def imprimir_menu():
    print("\n" + "=" * 45)
    print("      SISTEMA DE GESTIÓN DE PRODUCTOS")
    print("=" * 45)
    print("1. Registrar nuevo producto (Crear)")
    print("2. Consultar producto por ID (Leer)")
    print("3. Listar todos los productos (Leer)")
    print("4. Actualizar producto (Actualizar)")
    print("5. Eliminar producto (Eliminar)")
    print("6. Salir")
    print("=" * 45)


def solicitar_float(mensaje: str) -> float:
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("Error: El valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("Error: Ingrese un número válido (ej. 1500.50).")


def solicitar_int(mensaje: str) -> int:
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Error: El valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("Error: Ingrese un número entero válido (ej. 5).")


def main():
    # Se inicializa con persistencia en 'productos.json'
    manager = ProductManager(archivo="productos.json")

    while True:
        imprimir_menu()
        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == "1":
            print("\n--- REGISTRAR NUEVO PRODUCTO ---")
            id_prod = input("ID único: ").strip()
            nombre = input("Nombre: ").strip()
            desc = input("Descripción: ").strip()
            precio = solicitar_float("Precio: ")
            cantidad = solicitar_int("Cantidad en inventario: ")

            try:
                prod = manager.crear_producto(id_prod, nombre, desc, precio, cantidad)
                print(f"✅ Producto '{prod['nombre']}' registrado exitosamente con ID: {prod['id']}")
            except ValueError as e:
                print(f"❌ Error al crear: {e}")

        elif opcion == "2":
            print("\n--- CONSULTAR PRODUCTO ---")
            id_prod = input("Ingrese el ID del producto a buscar: ").strip()
            try:
                prod = manager.obtener_producto(id_prod)
                print("\nDatos del Producto:")
                print(f"  • ID:          {prod['id']}")
                print(f"  • Nombre:      {prod['nombre']}")
                print(f"  • Descripción: {prod['descripcion']}")
                print(f"  • Precio:      ${prod['precio']:.2f}")
                print(f"  • Cantidad:    {prod['cantidad']}")
            except KeyError as e:
                print(f"❌ {e}")

        elif opcion == "3":
            print("\n--- LISTADO DE PRODUCTOS ---")
            productos = manager.listar_productos()
            if not productos:
                print("No hay productos registrados en el sistema.")
            else:
                print(f"{'ID':<10} | {'Nombre':<25} | {'Precio':<10} | {'Stock':<6} | {'Descripción'}")
                print("-" * 75)
                for p in productos:
                    print(f"{p['id']:<10} | {p['nombre']:<25} | ${p['precio']:<9.2f} | {p['cantidad']:<6} | {p['descripcion']}")

        elif opcion == "4":
            print("\n--- ACTUALIZAR PRODUCTO ---")
            id_prod = input("Ingrese el ID del producto a actualizar: ").strip()
            try:
                prod_actual = manager.obtener_producto(id_prod)
                print(f"Producto encontrado: {prod_actual['nombre']}")
                print("(Presione Enter sin escribir nada para conservar el valor actual)")

                nuevo_nombre = input(f"Nuevo nombre [{prod_actual['nombre']}]: ").strip() or None
                nueva_desc = input(f"Nueva descripción [{prod_actual['descripcion']}]: ").strip() or None

                precio_in = input(f"Nuevo precio [{prod_actual['precio']}]: ").strip()
                nuevo_precio = float(precio_in) if precio_in else None

                cant_in = input(f"Nueva cantidad [{prod_actual['cantidad']}]: ").strip()
                nueva_cant = int(cant_in) if cant_in else None

                actualizado = manager.actualizar_producto(
                    id_prod=id_prod,
                    nombre=nuevo_nombre,
                    descripcion=nueva_desc,
                    precio=nuevo_precio,
                    cantidad=nueva_cant
                )
                print(f"✅ Producto '{actualizado['id']}' actualizado exitosamente.")
            except (KeyError, ValueError) as e:
                print(f"❌ Error al actualizar: {e}")

        elif opcion == "5":
            print("\n--- ELIMINAR PRODUCTO ---")
            id_prod = input("Ingrese el ID del producto a eliminar: ").strip()
            confirmacion = input(f"¿Está seguro de eliminar el producto '{id_prod}'? (s/n): ").strip().lower()
            if confirmacion == "s":
                try:
                    manager.eliminar_producto(id_prod)
                    print(f"✅ Producto '{id_prod}' eliminado correctamente.")
                except KeyError as e:
                    print(f"❌ Error: {e}")
            else:
                print("Operación cancelada.")

        elif opcion == "6":
            print("\n¡Gracias por utilizar el sistema! Saliendo...")
            break
        else:
            print("Opción inválida. Por favor seleccione un número del 1 al 6.")


if __name__ == "__main__":
    main()
