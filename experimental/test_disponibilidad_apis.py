"""
TEST: Verificación de Disponibilidad de APIs Adicionales
- Generación de imágenes (gemini-2.5-flash-image)
- Text-to-Speech (gemini-2.5-flash-preview-tts)
"""

import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai

# Configurar encoding UTF-8
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

# Cargar variables de entorno
load_dotenv()

# Configurar API
api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=api_key)

def listar_modelos_disponibles():
    """Lista todos los modelos disponibles en la API"""
    print("\n" + "=" * 70)
    print("MODELOS DISPONIBLES EN GEMINI API")
    print("=" * 70)
    
    modelos_encontrados = []
    
    for modelo in genai.list_models():
        nombre = modelo.name
        modelos_encontrados.append(nombre)
        
        # Mostrar solo modelos relevantes
        if any(x in nombre.lower() for x in ['gemini', '2.5', '2.0']):
            print(f"\n[MODELO]: {nombre}")
            print(f"  Display Name: {modelo.display_name}")
            print(f"  Description: {modelo.description}")
            
            if hasattr(modelo, 'supported_generation_methods'):
                print(f"  Methods: {modelo.supported_generation_methods}")
    
    return modelos_encontrados

def test_modelo_existe(nombre_modelo):
    """Verifica si un modelo específico existe"""
    print(f"\n[*] Buscando modelo: {nombre_modelo}")
    
    try:
        modelo_info = genai.get_model(f"models/{nombre_modelo}")
        print(f"  [OK] Modelo encontrado!")
        print(f"  Display Name: {modelo_info.display_name}")
        print(f"  Description: {modelo_info.description}")
        return True
    except Exception as e:
        print(f"  [X] Modelo no disponible: {e}")
        return False

def main():
    print("\n" + "=" * 70)
    print("   VERIFICACION DE APIS ADICIONALES")
    print("=" * 70)
    
    # Listar todos los modelos
    modelos = listar_modelos_disponibles()
    
    print("\n" + "=" * 70)
    print("VERIFICACION DE MODELOS ESPECIFICOS")
    print("=" * 70)
    
    # Modelos que queremos verificar
    modelos_objetivo = [
        "gemini-2.5-pro",
        "gemini-2.5-flash",
        "gemini-2.5-flash-image",
        "gemini-2.5-flash-preview-tts",
        "gemini-2.0-flash-exp",
        "gemini-1.5-pro",
        "gemini-1.5-flash"
    ]
    
    resultados = {}
    
    for modelo in modelos_objetivo:
        disponible = test_modelo_existe(modelo)
        resultados[modelo] = disponible
    
    # Resumen
    print("\n" + "=" * 70)
    print("RESUMEN DE DISPONIBILIDAD")
    print("=" * 70)
    
    print("\n[MODELOS PRINCIPALES]:")
    print(f"  gemini-2.5-pro: {'[OK] DISPONIBLE' if resultados.get('gemini-2.5-pro') else '[X] NO DISPONIBLE'}")
    print(f"  gemini-2.5-flash: {'[OK] DISPONIBLE' if resultados.get('gemini-2.5-flash') else '[X] NO DISPONIBLE'}")
    
    print("\n[MODELOS ESPECIALES]:")
    print(f"  gemini-2.5-flash-image: {'[OK] DISPONIBLE' if resultados.get('gemini-2.5-flash-image') else '[X] NO DISPONIBLE - Generación de imágenes no soportada en API pública'}")
    print(f"  gemini-2.5-flash-preview-tts: {'[OK] DISPONIBLE' if resultados.get('gemini-2.5-flash-preview-tts') else '[X] NO DISPONIBLE - TTS puede requerir acceso especial'}")
    
    print("\n[MODELOS ALTERNATIVOS]:")
    print(f"  gemini-2.0-flash-exp: {'[OK] DISPONIBLE' if resultados.get('gemini-2.0-flash-exp') else '[X] NO DISPONIBLE'}")
    print(f"  gemini-1.5-pro: {'[OK] DISPONIBLE' if resultados.get('gemini-1.5-pro') else '[X] NO DISPONIBLE'}")
    print(f"  gemini-1.5-flash: {'[OK] DISPONIBLE' if resultados.get('gemini-1.5-flash') else '[X] NO DISPONIBLE'}")
    
    print("\n[NOTA]:")
    print("  - Generación de imágenes: Actualmente no disponible en Gemini API")
    print("  - Usa servicios externos: Imagen.ai, DALL-E, Stable Diffusion")
    print("  - TTS: Puede estar disponible solo para usuarios enterprise")
    print("  - Alternativa TTS: Google Cloud Text-to-Speech API")
    print("")
    
    return True

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n[X] ERROR: {e}")
        import traceback
        traceback.print_exc()
