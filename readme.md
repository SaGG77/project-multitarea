# Project Multitarea

Aplicacion web desarrollada con **Flask** para centralizar tareas personales en tres areas: seguimiento de contenido, habitos y finanzas. El proyecto usa una arquitectura modular con rutas separadas, modelos de base de datos, formularios protegidos con CSRF y vistas construidas con Bootstrap.

---

## Modulos principales

- **Media:** registro de peliculas, series, musica, libros y juegos.
- **Habitos:** seguimiento diario, rachas, metricas y visualizaciones.
- **Finanzas:** registro de ingresos, gastos, categorias e historial.

---

## Tecnologias

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-WTF
- PyMySQL
- Bootstrap 5
- Chart.js

---

## Requisitos previos

Antes de iniciar, asegurate de tener instalado:

- Python 3.10 o superior
- pip
- Git
- MySQL, solo si vas a usar una base de datos MySQL

> Si solo quieres probar el proyecto rapido, puedes usar SQLite. No necesitas instalar MySQL para esa opcion.

---

## Instalacion paso a paso

### 1. Clonar el repositorio

```bash
git clone https://github.com/SaGG77/Project-Multi.git
cd Project-Multi
```

### 2. Crear un entorno virtual

```bash
python -m venv .venv
```

Activar el entorno virtual:

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Configuracion de base de datos

El proyecto lee la conexion desde la variable `DATABASE_URL`.

Si no configuras esta variable, Flask usara SQLite por defecto con este valor:

```env
sqlite:///app.db
```

### Opcion A: usar SQLite

Esta es la forma mas sencilla para probar el proyecto localmente.

Crea un archivo `.env` en la raiz del proyecto:

```env
FLASK_SECRET_KEY=una_clave_secreta_para_desarrollo
DATABASE_URL=sqlite:///app.db
```

Con esta opcion, la base de datos queda como un archivo local llamado `app.db`.

### Opcion B: usar MySQL

1. Crea una base de datos en MySQL:

```sql
CREATE DATABASE project_multi CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

2. Crea o edita el archivo `.env`:

```env
FLASK_SECRET_KEY=una_clave_secreta_para_desarrollo
DATABASE_URL=mysql+pymysql://usuario:contraseña@localhost/project_multi
```

Ejemplo:

```env
DATABASE_URL=mysql+pymysql://root:123456@localhost/project_multi
```

> Si tu contraseña tiene simbolos especiales como `@`, `#` o `%`, puede ser necesario codificarla para que la URL funcione correctamente.

---

## Crear o actualizar las tablas

Despues de configurar la base de datos, ejecuta las migraciones.

Si el proyecto todavia no tiene carpeta `migrations`, inicia Flask-Migrate:

```bash
flask --app app db init
```

Luego crea la migracion inicial:

```bash
flask --app app db migrate -m "initial database"
```

Aplica los cambios a la base de datos:

```bash
flask --app app db upgrade
```

> Si la carpeta `migrations` ya existe, no repitas `flask --app app db init`. Solo ejecuta `migrate` y `upgrade` cuando cambien los modelos.

---

## Ejecutar la aplicacion

```bash
python run.py
```

Abre el navegador en:

```text
http://127.0.0.1:5000
```

---

## Estructura general

```text
Project-Multi/
├── app.py
├── run.py
├── extensions.py
├── forms.py
├── models/
├── routes/
├── templates/
├── static/
└── utils/
```

---

## Problemas comunes

### No se conecta a la base de datos

Revisa que `DATABASE_URL` este bien escrito en `.env` y que el servidor de MySQL este encendido si usas MySQL.

### No reconoce el comando `flask`

Verifica que el entorno virtual este activado y que las dependencias esten instaladas.

### Error al importar paquetes

Ejecuta nuevamente:

```bash
pip install -r requirements.txt
```

---

## Autor

Samuel Guevara
