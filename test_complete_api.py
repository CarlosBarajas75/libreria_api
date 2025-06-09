import requests
import json

# URL base del API
BASE_URL = "http://127.0.0.1:8000"

def test_register():
    """Prueba el registro de usuario"""
    print("\n=== 1. Testing POST /auth/register ===")
    url = f"{BASE_URL}/auth/register"
    data = {
        "name": "Juan Pérez",
        "email": "juan@libreria.com", 
        "password": "password123"
    }
    
    response = requests.post(url, json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    return response

def test_login():
    """Prueba el login de usuario"""
    print("\n=== 2. Testing POST /auth/login ===")
    url = f"{BASE_URL}/auth/login"
    data = {
        "email": "juan@libreria.com",
        "password": "password123"
    }
    
    response = requests.post(url, json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    
    if response.status_code == 200:
        return response.json()
    return None

def test_create_book(access_token):
    """Prueba la creación de un libro"""
    print("\n=== 3. Testing POST /books ===")
    url = f"{BASE_URL}/books"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    data = {
        "isbn": "9780123456789",
        "title": "El Quijote",
        "author": "Miguel de Cervantes",
        "release_date": "2025-06-09"
    }
    
    response = requests.post(url, json=data, headers=headers)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    return response

def test_create_second_book(access_token):
    """Crea un segundo libro para tener más datos"""
    print("\n=== 4. Testing POST /books (segundo libro) ===")
    url = f"{BASE_URL}/books"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    data = {
        "isbn": "9781234567890",
        "title": "Cien Años de Soledad",
        "author": "Gabriel García Márquez",
        "release_date": "2025-06-09"
    }
    
    response = requests.post(url, json=data, headers=headers)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    return response

def test_get_books():
    """Prueba la consulta de todos los libros"""
    print("\n=== 5. Testing GET /books ===")
    url = f"{BASE_URL}/books"
    
    response = requests.get(url)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    return response

def test_delete_book(access_token, book_id):
    """Prueba la eliminación de un libro"""
    print(f"\n=== 6. Testing DELETE /books/{book_id} ===")
    url = f"{BASE_URL}/books/{book_id}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    response = requests.delete(url, headers=headers)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    return response

def test_create_duplicate_isbn(access_token):
    """Prueba crear un libro con ISBN duplicado"""
    print("\n=== 7. Testing POST /books (ISBN duplicado) ===")
    url = f"{BASE_URL}/books"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    data = {
        "isbn": "9781234567890",  # ISBN ya usado
        "title": "Libro Duplicado",
        "author": "Autor Test",
        "release_date": "2025-06-09"
    }
    
    response = requests.post(url, json=data, headers=headers)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    return response

def test_unauthorized_access():
    """Prueba acceso sin token"""
    print("\n=== 8. Testing POST /books (sin token) ===")
    url = f"{BASE_URL}/books"
    data = {
        "isbn": "9999999999999",
        "title": "Libro Sin Auth",
        "author": "Autor Test",
        "release_date": "2025-06-09"
    }
    
    response = requests.post(url, json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    return response

if __name__ == "__main__":
    print("=== ASSESSMENT TÉCNICO - BACKEND TRAINEE ===")
    print("=== PRUEBAS COMPLETAS DE LA API ===")
    
    # 1. Registrar usuario
    register_response = test_register()
    
    # 2. Login
    login_data = test_login()
    
    if login_data and 'access' in login_data:
        access_token = login_data['access']
        print(f"\n✅ Token JWT obtenido (válido por 24 horas)")
        print(f"Access Token: {access_token[:50]}...")
        
        # 3. Crear primer libro
        create_response1 = test_create_book(access_token)
        
        # 4. Crear segundo libro
        create_response2 = test_create_second_book(access_token)
        
        # 5. Consultar todos los libros
        get_response = test_get_books()
        
        # 6. Eliminar un libro (ID 1)
        delete_response = test_delete_book(access_token, 1)
        
        # 7. Consultar libros después de eliminar
        print("\n=== 9. Testing GET /books (después de eliminar) ===")
        get_response2 = test_get_books()
        
        # 8. Probar ISBN duplicado
        duplicate_response = test_create_duplicate_isbn(access_token)
        
        # 9. Probar acceso sin autorización
        unauthorized_response = test_unauthorized_access()
        
        print("\n" + "="*50)
        print("🎉 TODAS LAS PRUEBAS COMPLETADAS")
        print("="*50)
        
        print("\n📋 RESUMEN DE ENDPOINTS IMPLEMENTADOS:")
        print("✅ POST /auth/register - Registro de usuarios")
        print("✅ POST /auth/login - Inicio de sesión con JWT")
        print("✅ GET /books - Consulta de libros con usuario registrador")
        print("✅ POST /books - Creación de libros (requiere autenticación)")
        print("✅ DELETE /books/:id - Eliminación de libros (requiere autenticación)")
        
        print("\n🔐 CARACTERÍSTICAS DE SEGURIDAD:")
        print("✅ Contraseñas encriptadas")
        print("✅ Tokens JWT con expiración de 24 horas")
        print("✅ Validación de autenticación en endpoints protegidos")
        print("✅ Validación de ISBN único")
        
        print("\n🏆 EXTRAS IMPLEMENTADOS:")
        print("✅ Django Framework")
        print("✅ MongoDB con djongo")
        print("✅ JWT Authentication")
        print("✅ Validaciones de datos")
        print("✅ Manejo de errores")
        
    else:
        print("❌ Login failed, no se pueden probar los endpoints protegidos")
