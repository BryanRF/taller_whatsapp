


# Taller WhatsApp

Taller WhatsApp es un proyecto Django diseñado para gestionar talleres automotrices. Este README detalla el proceso de instalación, configuración y ejecución del proyecto.

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- Python 3.8 o superior
- pip (Gestor de paquetes de Python)
- Virtualenv (opcional, pero recomendado)


## Instalación

1. **Clona el repositorio**  
   Asegúrate de clonar este proyecto en tu máquina local:
   ```bash
   git clone https://github.com/tu_usuario/taller_whatsapp.git
   cd taller_whatsapp
   ```

2. **Crea un entorno virtual**  
   (Recomendado para mantener dependencias aisladas):
   ```bash
   python -m venv venv
   ```

3. **Activa el entorno virtual**  
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Instala las dependencias**  
   Utiliza el archivo `requirements.txt` para instalar todas las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

5. **Realiza las migraciones**  
   Configura la base de datos:
   ```bash
   python manage.py migrate
   ```

---

## Creación de un Superusuario

Para acceder al panel de administración de Django, necesitas crear un superusuario:

1. Ejecuta el comando:
   ```bash
   python manage.py createsuperuser
   ```

2. Proporciona las credenciales predeterminadas:
   - **Nombre de usuario**: `admin`
   - **Correo electrónico**: `admin@gmail.com`
   - **Contraseña**: `admin`
   - **Confirmar contraseña**: `admin`

---

## Ejecutar el Servidor de Desarrollo

Inicia el servidor de desarrollo en tu máquina local con el siguiente comando:
```bash
python manage.py runserver
```

Por defecto, el servidor estará disponible en [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Estructura de Carpetas

```plaintext
taller_whatsapp/
├── api/                   # Aplicación principal con lógica de negocio
├── templates/             # Archivos HTML para renderizado
├── static/                # Archivos estáticos (CSS, JS, imágenes)
├── venv/                  # Entorno virtual (no se sube al repositorio)
├── manage.py              # Script de gestión de Django
├── requirements.txt       # Dependencias del proyecto
└── README.md              # Este archivo
```

---

## Notas

- **Panel de Administración**: Una vez que hayas creado el superusuario, accede al panel en [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).
- **Modificaciones**: Si realizas cambios en los modelos, ejecuta:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```
- **Dependencias Adicionales**: Si agregas paquetes, actualiza `requirements.txt` con:
  ```bash
  pip freeze > requirements.txt
  ```

---

## Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).

```

### Explicación de los pasos:
1. **Instalación detallada:** Proporcioné los comandos para clonar, crear un entorno virtual, activar el entorno y configurar las dependencias.
2. **Creación de superusuario:** Especifica exactamente cómo ingresar los datos (`admin`, `admin@gmail.com`, `admin`).
3. **Ejecución del servidor:** Incluye el enlace al servidor local.
4. **Estructura de carpetas:** Ayuda a los usuarios a entender el diseño del proyecto.
5. **Notas útiles:** Explica pasos para migraciones y cómo manejar dependencias adicionales.