# Taller Evaluativo 20% - CRUD de Productos en Python
**Asignatura:** Aplicaciones y servicios web  
**Institución:** ITM - Institución Universitaria  
**Docente:** Jonathan Sánchez Giraldo (jonathansanchez2948@correo.itm.edu.co)

---

## 📌 Descripción del Proyecto
Este proyecto implementa una solución completa para la gestión CRUD (Crear, Leer, Actualizar y Eliminar) de un catálogo de productos en Python 3, cumpliendo con los estándares de calidad de software, pruebas unitarias y análisis estático con SonarQube.

### Atributos del Producto:
- `id`: Identificador único.
- `nombre`: Nombre del producto.
- `descripcion`: Breve descripción.
- `precio`: Precio unitario (validado no negativo).
- `cantidad`: Stock en inventario (validado no negativo).

---

## 🚀 Estructura del Repositorio
```text
crud-productos-python/
│
├── product_manager.py       # Lógica del CRUD y validaciones
├── test_product_manager.py  # Suite de pruebas unitarias (unittest)
├── main.py                  # Interfaz de consola interactiva
├── sonar-project.properties # Configuración para análisis SonarQube
├── README.md                # Instrucciones de uso y despliegue
└── productos.json           # Archivo de persistencia de datos (generado automáticamente)
```

---

## ⚙️ Requisitos Previos
- Python 3.10 o superior (no requiere librerías externas adicionales; utiliza la biblioteca estándar).

---

## 🧪 Ejecución de Pruebas Unitarias
Las pruebas cubren al menos un caso de éxito y un caso de error para cada operación del CRUD:

```bash
# Ejecutar todas las pruebas con detalle
python -m unittest test_product_manager.py -v
```

---

## 🖥️ Ejecución del Programa Principal (Menú)
Para interactuar con el sistema a través de la terminal:

```bash
python main.py
```

---

## 🔍 Análisis de Calidad con SonarQube

### Opción A: SonarScanner Local
1. Asegurarse de tener SonarQube en ejecución local (`http://localhost:9000`).
2. Abrir la terminal en la raíz del proyecto y ejecutar:
   ```bash
   sonar-scanner
   ```
3. Abrir la URL generada para revisar el reporte (Bugs: 0, Vulnerabilidades: 0, Deuda técnica: 0).

### Opción B: SonarCloud (Recomendado sin instalación local)
1. Vincular este repositorio público en [sonarcloud.io](https://sonarcloud.io).
2. Habilitar el escaneo automático (*Automatic Analysis*).
3. Obtener el dashboard y la insignia de calidad para el informe.

---

## 📤 Publicación en GitHub y Entrega
1. Inicializar el repositorio Git:
   ```bash
   git init
   git add .
   git commit -m "feat: implementacion inicial CRUD productos con pruebas unitarias"
   ```
2. Crear un repositorio público en GitHub (por ejemplo, `crud-productos-python`).
3. Vincular y subir:
   ```bash
   git remote add origin https://github.com/TU_USUARIO/crud-productos-python.git
   git branch -M main
   git push -u origin main
   ```
4. Compartir el enlace con el docente al correo: `jonathansanchez2948@correo.itm.edu.co` o invitarlo como colaborador.
