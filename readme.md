# Project Multitarea

Aplicación web construida con **Flask** para organizar en un solo lugar tres áreas clave de tu día a día:

- 🎬 **Seguimiento de contenido** (películas, series, música, libros y juegos).
- ⏱️ **Hábitos y tiempo** con rachas, métricas y visualizaciones.
- 💰 **Finanzas personales** con categorías, historial y balance.

---

## Tecnologías principales

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-WTF (CSRF + formularios)
- Bootstrap 5
- Chart.js

---

## Requisitos

- Python **3.10+** recomendado
- `pip`

---

## Instalación rápida

1. Clona el repositorio:

```bash
git clone <URL_DEL_REPO>
cd Project-Washed
```

2. Crea y activa un entorno virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

> En Windows (PowerShell):
>
> ```powershell
> .venv\Scripts\Activate.ps1
> ```

3. Instala dependencias:

```bash
pip install -r requirements.txt
```

4. Configura variables de entorno en un archivo `.env`:

```env
FLASK_SECRET_KEY=tu_clave_secreta
DATABASE_URL=sqlite:///app.db
```

5. Ejecuta la aplicación:

```bash
python run.py
```

La app quedará disponible en `http://127.0.0.1:5000`.

---

## Migraciones de base de datos (opcional)

Si necesitas crear o actualizar el esquema:

```bash
flask db init
flask db migrate -m "init"
flask db upgrade
```

> Si ya existe carpeta de migraciones, omite `flask db init`.

---

## Módulos principales

### 1) Media
Permite registrar y administrar contenido consumido:

- Tipo de media.
- Estado (planeado, en proceso, terminado, abandonado).
- Calificación y notas.

### 2) Hábitos
Permite crear hábitos y llevar seguimiento diario:

- Marcar/desmarcar cumplimiento del día.
- Rachas actuales y mejores rachas.
- Gráficos de progreso, distribución semanal y heatmap.

### 3) Finanzas
Permite registrar ingresos y gastos:

- Categorías por tipo (ingreso/gasto).
- Historial filtrable.
- Resumen reciente con balance.

---

## Estructura del proyecto

```text
Project-Washed/
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

## Autor

Samuel Guevara