"""
TEST MAESTRO: Verificación Completa del Sistema
Objetivo: Verificar que todo esté configurado y funcionando
"""

import sys
import os

# Agregar path parent
sys.path.append('..')

def verificar_python():
    """Verificar versión de Python"""
    print("\n🐍 Verificando Python...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"   ✅ Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"   ❌ Python {version.major}.{version.minor} - Se requiere 3.8+")
        return False

def verificar_dependencias():
    """Verificar que las dependencias estén instaladas"""
    print("\n📦 Verificando dependencias...")
    
    dependencias = {
        'google.generativeai': 'google-generativeai',
        'pydantic': 'pydantic',
        'selenium': 'selenium',
        'PIL': 'Pillow',
        'pytesseract': 'pytesseract',
        'cv2': 'opencv-python',
        'dotenv': 'python-dotenv',
        'requests': 'requests',
    }
    
    faltantes = []
    instaladas = []
    
    for modulo, nombre_paquete in dependencias.items():
        try:
            __import__(modulo)
            instaladas.append(nombre_paquete)
            print(f"   ✅ {nombre_paquete}")
        except ImportError:
            faltantes.append(nombre_paquete)
            print(f"   ❌ {nombre_paquete} - NO INSTALADO")
    
    return len(faltantes) == 0, faltantes

def verificar_config():
    """Verificar archivo de configuración"""
    print("\n⚙️  Verificando configuración...")
    
    try:
        from config import Config
        
        # Verificar API key
        if Config.GEMINI_API_KEY:
            print(f"   ✅ API Key de Gemini configurada")
            api_ok = True
        else:
            print(f"   ❌ API Key de Gemini NO configurada")
            api_ok = False
        
        # Verificar modelos
        print(f"   ℹ️  Modelo Chat: {Config.MODEL_CHAT}")
        print(f"   ℹ️  Modelo Visión: {Config.MODEL_VISION}")
        print(f"   ℹ️  Modelo Imagen: {Config.MODEL_IMAGE}")
        print(f"   ℹ️  Modelo TTS: {Config.MODEL_TTS}")
        
        # Verificar Tesseract
        if os.path.exists(Config.TESSERACT_CMD):
            print(f"   ✅ Tesseract OCR encontrado")
            tesseract_ok = True
        else:
            print(f"   ⚠️  Tesseract OCR no encontrado en: {Config.TESSERACT_CMD}")
            tesseract_ok = False
        
        # Verificar carpetas
        if Config.DOWNLOADS_DIR.exists():
            print(f"   ✅ Carpeta downloads: {Config.DOWNLOADS_DIR}")
        if Config.LOGS_DIR.exists():
            print(f"   ✅ Carpeta logs: {Config.LOGS_DIR}")
        
        return api_ok, tesseract_ok
        
    except Exception as e:
        print(f"   ❌ Error al cargar config: {e}")
        return False, False

def test_gemini_conexion():
    """Probar conexión con Gemini"""
    print("\n🤖 Probando conexión con Gemini...")
    
    try:
        from google import genai
        from config import Config
        
        client = genai.Client(api_key=Config.GEMINI_API_KEY)
        
        # Test simple
        response = client.models.generate_content(
            model=Config.MODEL_LITE,  # Usar modelo más rápido
            contents="Di solo: OK"
        )
        
        print(f"   ✅ Conexión exitosa")
        print(f"   📝 Respuesta: {response.text}")
        return True
        
    except Exception as e:
        print(f"   ❌ Error de conexión: {e}")
        return False

def mostrar_tests_disponibles():
    """Mostrar tests disponibles"""
    print("\n📋 Tests disponibles:")
    print("   1. test_gemini_text.py      - Generación de texto")
    print("   2. test_gemini_vision.py    - Comprensión de imágenes y OCR")
    print("   3. test_gemini_image.py     - Generación de imágenes")
    print("   4. test_gemini_tts.py       - Texto a voz")
    print("   5. test_gemini_json.py      - Salida JSON estructurada")

def main():
    """Ejecutar verificación completa"""
    print("=" * 70)
    print("  🔍 VERIFICACIÓN COMPLETA DEL SISTEMA")
    print("=" * 70)
    
    errores = []
    advertencias = []
    
    # 1. Verificar Python
    if not verificar_python():
        errores.append("Versión de Python incompatible")
    
    # 2. Verificar dependencias
    deps_ok, faltantes = verificar_dependencias()
    if not deps_ok:
        errores.append(f"Dependencias faltantes: {', '.join(faltantes)}")
    
    # 3. Verificar configuración
    api_ok, tesseract_ok = verificar_config()
    if not api_ok:
        errores.append("API Key de Gemini no configurada")
    if not tesseract_ok:
        advertencias.append("Tesseract OCR no encontrado (necesario para OCR)")
    
    # 4. Test de conexión
    if api_ok and deps_ok:
        if not test_gemini_conexion():
            errores.append("No se pudo conectar con Gemini API")
    
    # Mostrar tests disponibles
    mostrar_tests_disponibles()
    
    # Resumen final
    print("\n" + "=" * 70)
    print("  📊 RESUMEN DE VERIFICACIÓN")
    print("=" * 70)
    
    if not errores and not advertencias:
        print("\n✅ ¡TODO PERFECTO! El sistema está listo para usar.")
        print("\n🚀 Próximos pasos:")
        print("   1. Ejecuta: python test_gemini_text.py")
        print("   2. Luego prueba los demás tests")
        print("   3. Consulta PLAN_DESARROLLO.md para seguir las fases")
        return True
    
    if errores:
        print("\n❌ ERRORES CRÍTICOS:")
        for error in errores:
            print(f"   • {error}")
        
        print("\n🔧 Soluciones:")
        if "API Key" in str(errores):
            print("   1. Edita el archivo .env")
            print("   2. Agrega: GEMINI_API_KEY=TU_API_KEY_AQUI")
        
        if "Dependencias" in str(errores):
            print("   1. Activa el entorno virtual: .\\venv\\Scripts\\activate")
            print("   2. Ejecuta: pip install -r requirements.txt")
    
    if advertencias:
        print("\n⚠️  ADVERTENCIAS:")
        for adv in advertencias:
            print(f"   • {adv}")
        
        if "Tesseract" in str(advertencias):
            print("\n   Para instalar Tesseract OCR:")
            print("   1. Descarga: https://github.com/UB-Mannheim/tesseract/wiki")
            print("   2. Instala en: C:\\Program Files\\Tesseract-OCR\\")
            print("   3. Actualiza la ruta en .env si es diferente")
    
    return len(errores) == 0

if __name__ == "__main__":
    exito = main()
    
    if not exito:
        print("\n⚠️  Corrige los errores antes de continuar")
        sys.exit(1)
    else:
        print("\n")
        respuesta = input("¿Deseas ejecutar el test de texto ahora? (s/n): ")
        if respuesta.lower() in ['s', 'si', 'sí', 'yes', 'y']:
            print("\n🚀 Ejecutando test de texto...")
            os.system("python test_gemini_text.py")
