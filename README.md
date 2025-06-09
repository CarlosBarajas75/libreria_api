# API REST - Gestión de Librería Digital

Sistema de gestión para una librería digital desarrollado con Django y MongoDB. Permite registrar usuarios, autenticarlos mediante JWT y gestionar un catálogo de libros.

## Funcionalidades Implementadas

**Endpoints de autenticación:**
- `POST /auth/register` - Registro de nuevos usuarios
- `POST /auth/login` - Autenticación con JWT

**Gestión de libros:**
- `GET /books` - Listar todos los libros con información del usuario que los registró
- `POST /books` - Agregar nuevos libros (requiere autenticación)
- `DELETE /books/:id` - Eliminar libros (requiere autenticación)

**Características de seguridad:**
- Encriptación de contraseñas con PBKDF2
- Tokens JWT con expiración de 24 horas
- Validación de ISBN único
- Protección de rutas sensibles

## Tecnologías Utilizadas

- **Python 3.10+**
- **Django 3.2** - Framework web
- **Django REST Framework** - API REST
- **MongoDB** - Base de datos No Relacional
- **djongo** - ORM para Django + MongoDB
- **PyJWT** - Autenticación JWT
- **djangorestframework-simplejwt** - JWT para DRF

---

## 📋 **REQUISITOS PREVIOS**

Antes de ejecutar el proyecto, asegúrate de tener instalado:

1. **Python 3.10 o superior**
2. **MongoDB** (local o remoto)
3. **Git** (para clonar el repositorio)

---

## 🚀 **INSTRUCCIONES DE INSTALACIÓN Y EJECUCIÓN**

### 1. **Clonar el repositorio**
```bash
git clone [URL_DEL_REPOSITORIO]
cd libreria_api
```

### 2. **Crear entorno virtual**
```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

### 4. **Configurar MongoDB**
Asegúrate de que MongoDB esté ejecutándose en tu sistema:
- **Local**: MongoDB corriendo en `localhost:27017`
- **Remoto**: Actualizar la configuración en `bookstore/settings.py`

### 5. **Aplicar migraciones**
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. **Ejecutar el servidor**
```bash
python manage.py runserver
```

El servidor estará disponible en: `http://127.0.0.1:8000`

---

## 📡 **ENDPOINTS DE LA API**

### **Autenticación**

#### `POST /auth/register`
Registra un nuevo usuario.

**Body:**
```json
{
    "name": "Juan Pérez",
    "email": "juan@example.com",
    "password": "password123"
}
```

**Respuesta exitosa:**
```json
{
    "success": true
}
```

#### `POST /auth/login`
Inicia sesión y obtiene token JWT.

**Body:**
```json
{
    "email": "juan@example.com",
    "password": "password123"
}
```

**Respuesta exitosa:**
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIs...",
    "access": "eyJhbGciOiJIUzI1NiIs...",
    "user_id": 1,
    "user_email": "juan@example.com"
}
```

### **Gestión de Libros**

#### `GET /books`
Obtiene todos los libros con información del usuario registrador.

**Respuesta:**
```json
[
    {
        "id": 1,
        "isbn": "9780123456789",
        "title": "El Quijote",
        "author": "Miguel de Cervantes",
        "release_date": "2025-06-09",
        "registered_by_user": {
            "id": 1,
            "name": "Juan Pérez",
            "email": "juan@example.com"
        }
    }
]
```

#### `POST /books`
Crea un nuevo libro (requiere autenticación).

**Headers:**
```
Authorization: Bearer YOUR_JWT_TOKEN
Content-Type: application/json
```

**Body:**
```json
{
    "isbn": "9780123456789",
    "title": "El Quijote",
    "author": "Miguel de Cervantes",
    "release_date": "2025-06-09"
}
```

**Respuesta exitosa:**
```json
{
    "id": "1"
}
```

#### `DELETE /books/:id`
Elimina un libro por ID (requiere autenticación).

**Headers:**
```
Authorization: Bearer YOUR_JWT_TOKEN
```

**Respuesta exitosa:**
```json
{
    "success": true
}
```

---

## 🧪 **PRUEBAS**

Para ejecutar las pruebas completas de la API:

```bash
python test_complete_api.py
```

Este script probará todos los endpoints automáticamente y mostrará un reporte completo.

---

## 📁 **ESTRUCTURA DEL PROYECTO**

```
libreria_api/
├── manage.py                 # Comando principal de Django
├── requirements.txt          # Dependencias del proyecto
├── database_export.sql       # Exportación de la base de datos
├── test_complete_api.py      # Suite de pruebas completa
├── README.md                # Documentación del proyecto
├── .gitignore               # Archivos ignorados por Git
├── bookstore/               # Configuración principal
│   ├── settings.py          # Configuración de Django
│   ├── urls.py              # URLs principales
│   └── wsgi.py              # Configuración WSGI
└── library/                 # Aplicación principal
    ├── models.py            # Modelos de datos (User, Book)
    ├── serializers.py       # Serializers para la API
    ├── views.py             # Vistas de la API REST
    ├── managers.py          # UserManager personalizado
    └── migrations/          # Migraciones de la base de datos
```

---

## ⚙️ **CONFIGURACIÓN**

### Variables de entorno importantes:

- **DATABASES**: Configurada para MongoDB con djongo
- **JWT**: Tokens con expiración de 24 horas
- **SECRET_KEY**: Clave secreta de Django
- **DEBUG**: True para desarrollo

### Base de datos:
- **Motor**: MongoDB con djongo
- **Nombre**: libreria_db
- **Colecciones**: library_user, library_book

---

## 🔒 **SEGURIDAD**

- ✅ Contraseñas encriptadas con PBKDF2
- ✅ Autenticación JWT obligatoria para endpoints protegidos
- ✅ Validación de datos en todos los endpoints
- ✅ Protección contra duplicación de ISBN
- ✅ Tokens con expiración automática (24 horas)

---

## 📊 **CÓDIGOS DE ESTADO HTTP**

| Código | Descripción |
|--------|-------------|
| 200 | Operación exitosa |
| 201 | Recurso creado exitosamente |
| 400 | Datos inválidos o ISBN duplicado |
| 401 | No autorizado (token faltante/inválido) |
| 404 | Recurso no encontrado |
| 500 | Error interno del servidor |

---

## 🚨 **SOLUCIÓN DE PROBLEMAS**

### MongoDB no se conecta:
1. Verificar que MongoDB esté ejecutándose
2. Comprobar la configuración en `settings.py`
3. Instalar pymongo: `pip install pymongo==3.12.3`

### Error de migraciones:
```bash
python manage.py migrate library zero
python manage.py makemigrations library
python manage.py migrate
```

### Token JWT inválido:
- Verificar que el token no haya expirado (24 horas)
- Confirmar formato: `Authorization: Bearer TOKEN`
- Hacer login nuevamente para obtener un token fresco

---

## 👨‍💻 **DESARROLLADO POR**

**Nombre**: [Tu Nombre]  
**Email**: [Tu Email]  
**Fecha**: 9 de junio de 2025  
**Assessment**: Backend Trainee - Digital Ignition  

---

## 📄 **LICENCIA**

Este proyecto fue desarrollado como parte de un assessment técnico para Digital Ignition.

---

## 📞 **CONTACTO**

Para cualquier duda o consulta sobre el proyecto:

- **jose.esparza@digitalignition.com.mx**
- **angel.arreola@digitalignition.com.mx**  
- **roberto@digitalignition.com.mx**

---

**¡Gracias por revisar mi assessment técnico!** 🚀
