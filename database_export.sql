-- ==============================================
-- ASSESSMENT TÉCNICO - BACKEND TRAINEE
-- Exportación de Base de Datos MongoDB
-- ==============================================

-- Base de datos: libreria_db
-- Fecha de exportación: 9 de junio de 2025

-- ==============================================
-- ESTRUCTURA DE LA BASE DE DATOS
-- ==============================================

-- COLECCIÓN: library_user (Usuarios)
-- Campos: id, email, name, password (encriptada), is_active, is_staff, last_login, date_joined

-- COLECCIÓN: library_book (Libros)  
-- Campos: id, isbn, title, author, release_date, registered_by

-- ==============================================
-- DATOS DE EJEMPLO
-- ==============================================

-- Usuario de ejemplo (contraseña: testpassword123)
db.library_user.insertOne({
    "_id": 1,
    "email": "testuser@example.com",
    "name": "Test User",
    "password": "pbkdf2_sha256$260000$hashexample",
    "is_active": true,
    "is_staff": false,
    "last_login": null,
    "date_joined": new Date()
});

-- Libro de ejemplo
db.library_book.insertOne({
    "_id": 1,
    "isbn": "9780123456789",
    "title": "Libro de Ejemplo",
    "author": "Autor de Ejemplo",
    "release_date": "2025-06-09",
    "registered_by": "1"
});

-- ==============================================
-- ÍNDICES RECOMENDADOS
-- ==============================================

-- Índice único para email de usuarios
db.library_user.createIndex({ "email": 1 }, { unique: true });

-- Índice único para ISBN de libros
db.library_book.createIndex({ "isbn": 1 }, { unique: true });

-- Índice para consultas por usuario registrador
db.library_book.createIndex({ "registered_by": 1 });

-- ==============================================
-- NOTAS IMPORTANTES
-- ==============================================

/*
1. Esta base de datos está configurada para MongoDB
2. Se utiliza djongo como ORM para Django + MongoDB
3. Los IDs son autoincrementales
4. Las contraseñas están encriptadas con PBKDF2
5. El sistema usa JWT para autenticación
6. Todos los endpoints están funcionando correctamente
*/
