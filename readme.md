# Project Multitarea

Aplicación web desarrollada con **Flask** para centralizar la gestión de contenido multimedia, hábitos y finanzas personales en una sola plataforma.

La aplicación implementa una arquitectura modular utilizando Blueprints, persistencia de datos mediante SQLAlchemy, migraciones con Flask-Migrate y una interfaz responsive desarrollada con Bootstrap.

---

## Vista previa

![Vista previa del proyecto](static/img/Captura-proyecto.png)

---

## Funcionalidades

### 🎬 Gestión de contenido

- Registro de películas
- Series
- Libros
- Música
- Videojuegos
- Calificaciones y estados

### 📅 Seguimiento de hábitos

- Registro diario
- Rachas actuales
- Mejor racha
- Métricas
- Gráficos con Chart.js

### 💰 Finanzas personales

- Registro de ingresos
- Registro de gastos
- Categorías
- Historial
- Balance

---

## Tecnologías

### Backend

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-WTF

### Base de datos

- SQLite
- MySQL
- PyMySQL

### Frontend

- HTML
- CSS
- Bootstrap 5
- JavaScript
- Chart.js

---

## Instalación

### Clonar el repositorio

```bash
git clone https://github.com/SaGG77/Project-Multi.git

cd Project-Multi
```

### Crear entorno virtual

```bash
python -m venv .venv
```

Windows

```powershell
.venv\Scripts\Activate.ps1
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

### Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Configuración

El proyecto obtiene la configuración desde un archivo `.env`.

Si no existe, utilizará SQLite por defecto.

Ejemplo:

```env
FLASK_SECRET_KEY=tu_clave_secreta

DATABASE_URL=sqlite:///app.db
```

---

## Base de datos

Para crear todas las tablas ejecuta:

```bash
flask --app app db upgrade
```

Si deseas utilizar MySQL, crea una base de datos y modifica la variable `DATABASE_URL`:

```env
DATABASE_URL=mysql+pymysql://usuario:contraseña@localhost/project_multi
```

---

## Ejecutar la aplicación

```bash
python run.py
```

Después abre:

```
http://127.0.0.1:5000
```

---

## Estructura

```text
Project-Multi/
│
├── assets/
├── models/
├── routes/
├── static/
├── templates/
├── utils/
│
├── migrations/
│
├── app.py
├── extensions.py
├── forms.py
├── run.py
├── requirements.txt
└── README.md
```

---

## Tecnologías utilizadas

- Flask
- SQLAlchemy
- Flask-Migrate
- Flask-WTF
- Bootstrap
- Chart.js
- SQLite
- MySQL

---

## Autor

**Samuel Guevara**
