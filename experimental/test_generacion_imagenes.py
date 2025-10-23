"""
TEST: Generación de Imágenes con Gemini 2.5 Flash Image e Imagen 4.0
Objetivo: Validar generación de imágenes desde texto
Modelos: gemini-2.5-flash-image, imagen-4.0-ultra-generate-001
"""

import os
import sys
import base64
import mimetypes
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Configurar encoding UTF-8
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

# Cargar variables de entorno
load_dotenv()

# Crear directorio para imágenes generadas
os.makedirs("experimental/imagenes_generadas", exist_ok=True)

DELAY = 10  # Delay más largo para generación de imágenes

def save_binary_file(file_name, data):
    """Guarda archivo binario"""
    with open(file_name, "wb") as f:
        f.write(data)
    print(f"  [OK] Archivo guardado: {file_name}")
    print(f"  [INFO] Tamaño: {len(data)} bytes")
    return file_name

def test_1_gemini_flash_image():
    """Test 1: Generación con gemini-2.5-flash-image (streaming)"""
    print("\n" + "=" * 70)
    print("TEST 1: Gemini 2.5 Flash Image (Streaming)")
    print("=" * 70)
    
    try:
        client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
        
        model = "gemini-2.5-flash-image"
        prompt = "Una zapatilla deportiva Nike Air Max azul y blanca, fondo blanco, estilo producto de catálogo"
        
        print(f"\n[PROMPT]: {prompt}")
        print(f"[MODELO]: {model}")
        print(f"[GENERANDO...]")
        
        contents = [
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=prompt)],
            ),
        ]
        
        generate_content_config = types.GenerateContentConfig(
            response_modalities=["IMAGE", "TEXT"],
        )
        
        file_index = 0
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        ):
            if (
                chunk.candidates is None
                or chunk.candidates[0].content is None
                or chunk.candidates[0].content.parts is None
            ):
                continue
            
            if chunk.candidates[0].content.parts[0].inline_data and chunk.candidates[0].content.parts[0].inline_data.data:
                file_name = f"experimental/imagenes_generadas/zapatilla_gemini_{file_index}"
                file_index += 1
                inline_data = chunk.candidates[0].content.parts[0].inline_data
                data_buffer = inline_data.data
                file_extension = mimetypes.guess_extension(inline_data.mime_type)
                save_binary_file(f"{file_name}{file_extension}", data_buffer)
            else:
                if hasattr(chunk, 'text') and chunk.text:
                    print(f"  [TEXTO]: {chunk.text}")
        
        print(f"\n[OK] TEST 1 PASADO ✅")
        return True
        
    except Exception as e:
        print(f"\n[X] ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_2_imagen_4_ultra():
    """Test 2: Generación con Imagen 4.0 Ultra"""
    print("\n" + "=" * 70)
    print("TEST 2: Imagen 4.0 Ultra")
    print("=" * 70)
    
    try:
        client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
        
        prompt = "Logo moderno para tienda de ropa llamada 'Esencia Urbana', colores azul y blanco, estilo minimalista, alta calidad"
        
        print(f"\n[PROMPT]: {prompt}")
        print(f"[MODELO]: imagen-4.0-ultra-generate-001")
        print(f"[GENERANDO...]")
        
        result = client.models.generate_images(
            model="imagen-4.0-ultra-generate-001",
            prompt=prompt,
            config=dict(
                number_of_images=1,
                output_mime_type="image/jpeg",
                person_generation="ALLOW_ALL",
                aspect_ratio="1:1",
                image_size="1K",
            ),
        )
        
        if not result.generated_images:
            print("  [X] No se generaron imágenes")
            return False
        
        for n, generated_image in enumerate(result.generated_images):
            filepath = f"experimental/imagenes_generadas/logo_tienda_{n}.jpg"
            generated_image.image.save(filepath)
            print(f"  [OK] Imagen guardada: {filepath}")
        
        print(f"\n[OK] TEST 2 PASADO ✅")
        return True
        
    except Exception as e:
        print(f"\n[X] ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_3_imagen_4_fast():
    """Test 3: Generación con Imagen 4.0 Fast (más rápido)"""
    print("\n" + "=" * 70)
    print("TEST 3: Imagen 4.0 Fast")
    print("=" * 70)
    
    try:
        client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
        
        prompt = "Banner promocional de venta de zapatillas, texto 'DESCUENTO 30%', colores vibrantes azul y rojo, estilo moderno, alta resolución"
        
        print(f"\n[PROMPT]: {prompt}")
        print(f"[MODELO]: imagen-4.0-fast-generate-001")
        print(f"[GENERANDO...]")
        
        result = client.models.generate_images(
            model="imagen-4.0-fast-generate-001",
            prompt=prompt,
            config=dict(
                number_of_images=1,
                output_mime_type="image/jpeg",
                person_generation="ALLOW_ALL",
                aspect_ratio="16:9",  # Banner horizontal
                image_size="1K",
            ),
        )
        
        if not result.generated_images:
            print("  [X] No se generaron imágenes")
            return False
        
        for n, generated_image in enumerate(result.generated_images):
            filepath = f"experimental/imagenes_generadas/banner_promo_{n}.jpg"
            generated_image.image.save(filepath)
            print(f"  [OK] Imagen guardada: {filepath}")
        
        print(f"\n[OK] TEST 3 PASADO ✅")
        return True
        
    except Exception as e:
        print(f"\n[X] ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    print("\n" + "=" * 70)
    print("   TEST GENERACION DE IMAGENES")
    print("   gemini-2.5-flash-image + imagen-4.0")
    print("=" * 70)
    
    print("\n[NOTA]: Probando diferentes modelos de generación")
    print("[NOTA]: imagen-4.0 puede requerir permisos del tier de pago")
    
    try:
        results = []
        
        # Test 1: Gemini 2.5 Flash Image
        result1 = test_1_gemini_flash_image()
        results.append(("Gemini 2.5 Flash Image", result1))
        
        print(f"\n[*] Esperando {DELAY}s...")
        time.sleep(DELAY)
        
        # Test 2: Imagen 4.0 Ultra
        result2 = test_2_imagen_4_ultra()
        results.append(("Imagen 4.0 Ultra", result2))
        
        print(f"\n[*] Esperando {DELAY}s...")
        time.sleep(DELAY)
        
        # Test 3: Imagen 4.0 Fast
        result3 = test_3_imagen_4_fast()
        results.append(("Imagen 4.0 Fast", result3))
        
        # Resumen
        print("\n" + "=" * 70)
        print("   RESUMEN DE TESTS")
        print("=" * 70)
        
        tests_pasados = sum([r[1] for r in results])
        print(f"\n[RESULTADO]: {tests_pasados}/{len(results)} tests pasados")
        
        for nombre, resultado in results:
            estado = "✅ PASADO" if resultado else "❌ FALLIDO"
            print(f"  - {nombre}: {estado}")
        
        print("\n[OBSERVACIONES]:")
        print("  - gemini-2.5-flash-image: Requiere response_modalities=['IMAGE', 'TEXT']")
        print("  - imagen-4.0-ultra: Mayor calidad, puede requerir tier de pago")
        print("  - imagen-4.0-fast: Más rápido, buena calidad")
        
        print("\n[ALTERNATIVAS SI NO FUNCIONAN]:")
        print("  - DALL-E 3 (OpenAI) - Excelente calidad")
        print("  - Stable Diffusion XL - Open source")
        print("  - Midjourney API - Calidad artística")
        print("  - Leonardo.ai - Buena relación precio/calidad")
        print("")
        
        return True
        
    except Exception as e:
        print(f"\n[X] ERROR GENERAL: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Test interrumpido")
