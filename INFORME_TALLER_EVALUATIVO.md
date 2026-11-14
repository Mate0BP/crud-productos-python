# ACTIVIDAD GUÍA DE TRABAJO NO. 4 - TALLER EVALUATIVO 20%
**Asignatura:** Aplicaciones y servicios web  
**Código:** 580202009 | **Área:** Sistemas  
**Institución:** ITM - Institución Universitaria  

---

## 1. INFORMACIÓN DE LOS ESTUDIANTES
- **Integrantes:** [Nombres y Apellidos de los Estudiantes]
- **Programa Académico:** Ingeniería de Sistemas / Tecnología en Desarrollo de Software
- **Fecha:** [Fecha de Entrega, Ej. Noviembre 2026]
- **Docente:** Jonathan Sánchez Giraldo (`jonathansanchez2948@correo.itm.edu.co`)

---

## 2. ESTRUCTURA Y CONFIGURACIÓN DEL PROYECTO
El proyecto se desarrolló en **Python 3** utilizando únicamente su biblioteca estándar, garantizando portabilidad, legibilidad y facilidad de despliegue sin dependencias complejas externas.

### Estructura de Archivos:
- `product_manager.py`: Módulo principal que contiene la clase `ProductManager`, encargada de toda la lógica de negocio del CRUD y las validaciones de datos.
- `test_product_manager.py`: Archivo de pruebas unitarias implementado con el módulo estándar `unittest`.
- `main.py`: Interfaz de usuario por consola para pruebas interactivas manuales.
- `sonar-project.properties`: Archivo de configuración para el análisis estático de código en SonarQube / SonarScanner.
- `productos.json`: Archivo de almacenamiento persistente en formato JSON.
- `README.md`: Documentación con instrucciones de ejecución y despliegue.

---

## 3. IMPLEMENTACIÓN DEL CRUD DE PRODUCTOS

Cada producto cuenta con los siguientes atributos:
- `id`: Identificador alfanumérico único.
- `nombre`: Nombre descriptivo del producto.
- `descripcion`: Detalles del producto.
- `precio`: Valor numérico (con validación de precio $\ge 0$).
- `cantidad`: Unidades disponibles (con validación de cantidad $\ge 0$).

### Operaciones Implementadas:
1. **Crear (`crear_producto`)**: Valida que el ID no exista previamente y que tanto precio como cantidad sean valores no negativos.
2. **Leer (`obtener_producto` y `listar_productos`)**: Permite consultar un producto puntual por su ID o listar la totalidad del catálogo.
3. **Actualizar (`actualizar_producto`)**: Permite modificar selectivamente campos del producto verificando existencia previa y consistencia en los tipos de datos.
4. **Eliminar (`eliminar_producto`)**: Remueve el producto del catálogo y actualiza el archivo persistente.

---

## 4. PRUEBAS UNITARIAS (UNITTEST)

Se implementaron **11 pruebas unitarias** divididas en casos exitosos y casos de error controlados para cada una de las 4 operaciones del CRUD:

| Operación | Caso Exitoso | Caso de Error |
| :--- | :--- | :--- |
| **Crear** | Registro exitoso de producto nuevo (`test_crear_producto_exitoso`) | Intento con ID duplicado (`test_crear_producto_error_id_duplicado`) o precio negativo (`test_crear_producto_error_precio_o_cantidad_negativa`) |
| **Leer** | Búsqueda exitosa por ID (`test_leer_producto_exitoso`) y listado general (`test_listar_productos_exitoso`) | Búsqueda de ID inexistente lanza `KeyError` (`test_leer_producto_error_inexistente`) |
| **Actualizar** | Actualización de precio/nombre (`test_actualizar_producto_exitoso`) | Actualización sobre ID inexistente (`test_actualizar_producto_error_inexistente`) o valor negativo (`test_actualizar_producto_error_datos_invalidos`) |
| **Eliminar** | Eliminación de producto existente (`test_eliminar_producto_exitoso`) | Eliminación de ID inexistente lanza `KeyError` (`test_eliminar_producto_error_inexistente`) |

### Salida de la Ejecución de Pruebas:
```text
test_actualizar_producto_error_datos_invalidos ... ok
test_actualizar_producto_error_inexistente ... ok
test_actualizar_producto_exitoso ... ok
test_crear_producto_error_id_duplicado ... ok
test_crear_producto_error_precio_o_cantidad_negativa ... ok
test_crear_producto_exitoso ... ok
test_eliminar_producto_error_inexistente ... ok
test_eliminar_producto_exitoso ... ok
test_leer_producto_error_inexistente ... ok
test_leer_producto_exitoso ... ok
test_listar_productos_exitoso ... ok

Ran 11 tests in 0.001s
OK
```

*(Pegar aquí la captura de pantalla de la terminal con el comando `python -m unittest test_product_manager.py -v`)*

---

## 5. CONTROL DE CALIDAD CON SONARQUBE

Se preparó el archivo de configuración `sonar-project.properties` con las exclusiones requeridas para pruebas y fuentes:

```properties
sonar.projectKey=crud-productos-python
sonar.projectName=CRUD Productos Python
sonar.projectVersion=1.0
sonar.sourceEncoding=UTF-8
sonar.sources=.
sonar.exclusions=test_*.py,venv/**,.git/**,__pycache__/**
sonar.tests=.
sonar.test.inclusions=test_*.py
sonar.language=py
```

### Resultados del Análisis:
- **Quality Gate:** Passed
- **Bugs:** 0
- **Vulnerabilities:** 0
- **Security Hotspots:** 0
- **Code Smells:** 0

*(Pegar aquí la captura de pantalla del dashboard de SonarQube o SonarCloud)*

---

## 6. REPOSITORIO EN GITHUB
- **URL del Repositorio:** `[Pegar aquí la URL de tu repositorio GitHub, ej. https://github.com/usuario/crud-productos-python]`
- **Colaborador / Invitado:** `jonathansanchez2948@correo.itm.edu.co`

---

## 7. BIBLIOGRAFÍA
1. Python Software Foundation. (2024). *unittest — Unit testing framework*. Python 3 Documentation. https://docs.python.org/3/library/unittest.html
2. Python Software Foundation. (2024). *json — JSON encoder and decoder*. Python 3 Documentation. https://docs.python.org/3/library/json.html
3. SonarSource. (2024). *SonarQube Documentation: Python Static Code Analysis*. https://docs.sonarsource.com/sonarqube/latest/
4. Chacon, S., & Straub, B. (2014). *Pro Git: Everything you need to know about Git*. Apress. https://git-scm.com/book/en/v2
