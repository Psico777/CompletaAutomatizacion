"""
TEST 3: Generación de Imágenes con Gemini 2.5 Flash Image
Objetivo: Probar generación de imágenes desde texto
"""

import sys
sys.path.append('..')

from google import genai
from google.genai import types
from config import Config
from PIL import Image
from io import BytesIO
import os

def test_1_imagen_simple():
    """Test 1: Generar imagen simple desde texto"""
    print("\n" + "=" * 60)
    print("TEST 1: Generación de Imagen Simple")
    print("=" * 60)
    
    client = genai.Client(api_key=Config.GEMINI_API_KEY)
    
    prompt = "Crea una imagen moderna y minimalista de una tienda de ropa con colores vibrantes"
    
    print(f"\n📝 Prompt: {prompt}")
    print("🎨 Generando imagen...")
    
    response = client.models.generate_content(
        model=Config.MODEL_IMAGE,
        contents=[prompt],
    )
    
    # Guardar imagen
    for i, part in enumerate(response.candidates[0].content.parts):
        if part.text is not None:
            print(f"📄 Texto: {part.text}")
        elif part.inline_data is not None:
            image = Image.open(BytesIO(part.inline_data.data))
            filename = f"generated_tienda_{i}.png"
            image.save(filename)
            print(f"✅ Imagen guardada: {filename}")
            print(f"   Tamaño: {image.size}")

def test_2_imagen_especifica():
    """Test 2: Imagen con descripción detallada"""
    print("\n" + "=" * 60)
    print("TEST 2: Imagen con Descripción Detallada")
    print("=" * 60)
    
    client = genai.Client(api_key=Config.GEMINI_API_KEY)
    
    prompt = """
    Crea una imagen profesional para redes sociales de:
    - Un banner promocional para Black Friday
    - Fondo oscuro elegante con detalles dorados
    - Texto grande que diga "50% OFF"
    - Estilo moderno y llamativo
    - Formato horizontal
    """
    
    print(f"\n📝 Prompt detallado: {prompt.strip()}")
    print("🎨 Generando imagen...")
    
    response = client.models.generate_content(
        model=Config.MODEL_IMAGE,
        contents=[prompt],
        config=types.GenerateContentConfig(
            response_modalities=['Image'],  # Solo imagen, sin texto
            image_config=types.ImageConfig(
                aspect_ratio="16:9",  # Formato horizontal
            )
        )
    )
    
    # Guardar imagen
    for i, part in enumerate(response.candidates[0].content.parts):
        if part.inline_data is not None:
            image = Image.open(BytesIO(part.inline_data.data))
            filename = f"generated_promo_blackfriday.png"
            image.save(filename)
            print(f"✅ Imagen guardada: {filename}")
            print(f"   Tamaño: {image.size}")
            print(f"   Aspect Ratio: 16:9")

def test_3_diferentes_estilos():
    """Test 3: Generar la misma imagen en diferentes estilos"""
    print("\n" + "=" * 60)
    print("TEST 3: Diferentes Estilos Artísticos")
    print("=" * 60)
    
    client = genai.Client(api_key=Config.GEMINI_API_KEY)
    
    estilos = [
        "fotorrealista profesional",
        "ilustración kawaii colorida",
        "minimalista moderno",
        "pixel art retro"
    ]
    
    concepto = "una taza de café en una mesa de madera"
    
    for estilo in estilos:
        prompt = f"Crea una imagen en estilo {estilo} de {concepto}"
        print(f"\n🎨 Generando: {prompt}")
        
        response = client.models.generate_content(
            model=Config.MODEL_IMAGE,
            contents=[prompt],
            config=types.GenerateContentConfig(
                response_modalities=['Image']
            )
        )
        
        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                image = Image.open(BytesIO(part.inline_data.data))
                filename = f"generated_cafe_{estilo.replace(' ', '_')}.png"
                image.save(filename)
                print(f"   ✅ Guardado: {filename}")

def test_4_logo_empresa():
    """Test 4: Generar logo para empresa"""
    print("\n" + "=" * 60)
    print("TEST 4: Generación de Logo")
    print("=" * 60)
    
    client = genai.Client(api_key=Config.GEMINI_API_KEY)
    
    prompt = """
    Crea un logotipo moderno y minimalista para una empresa de tecnología llamada "TechFlow".
    - Debe incluir el texto "TechFlow"
    - Usar colores azul y blanco
    - Diseño limpio y profesional
    - Icono abstracto que represente flujo y tecnología
    - Fondo transparente o blanco
    """
    
    print(f"\n📝 Generando logo profesional...")
    
    response = client.models.generate_content(
        model=Config.MODEL_IMAGE,
        contents=[prompt],
        config=types.GenerateContentConfig(
            response_modalities=['Image'],
            image_config=types.ImageConfig(
                aspect_ratio="1:1",  # Cuadrado
            )
        )
    )
    
    for part in response.candidates[0].content.parts:
        if part.inline_data is not None:
            image = Image.open(BytesIO(part.inline_data.data))
            filename = "generated_logo_techflow.png"
            image.save(filename)
            print(f"✅ Logo guardado: {filename}")

def test_5_estado_whatsapp():
    """Test 5: Imagen para estado de WhatsApp"""
    print("\n" + "=" * 60)
    print("TEST 5: Imagen para Estado de WhatsApp")
    print("=" * 60)
    
    client = genai.Client(api_key=Config.GEMINI_API_KEY)
    
    prompt = """
    Crea una imagen atractiva para estado de WhatsApp:
    - Mensaje: "¡Nuevos productos disponibles! 🛍️"
    - Fondo degradado de colores vibrantes
    - Diseño moderno y juvenil
    - Texto grande y legible
    - Formato vertical
    """
    
    print(f"\n📝 Generando estado de WhatsApp...")
    
    response = client.models.generate_content(
        model=Config.MODEL_IMAGE,
        contents=[prompt],
        config=types.GenerateContentConfig(
            response_modalities=['Image'],
            image_config=types.ImageConfig(
                aspect_ratio="9:16",  # Vertical para stories
            )
        )
    )
    
    for part in response.candidates[0].content.parts:
        if part.inline_data is not None:
            image = Image.open(BytesIO(part.inline_data.data))
            filename = "generated_estado_whatsapp.png"
            image.save(filename)
            print(f"✅ Estado guardado: {filename}")
            print(f"   Formato: 9:16 (vertical)")

def test_6_producto_ecommerce():
    """Test 6: Foto de producto para e-commerce"""
    print("\n" + "=" * 60)
    print("TEST 6: Foto de Producto E-commerce")
    print("=" * 60)
    
    client = genai.Client(api_key=Config.GEMINI_API_KEY)
    
    prompt = """
    Una fotografía de producto profesional para e-commerce de:
    - Zapatillas deportivas modernas de color blanco y azul
    - Fondo blanco limpio
    - Iluminación de estudio profesional
    - Vista lateral con sombra suave
    - Ultra realista y de alta calidad
    - Estilo catálogo Nike/Adidas
    """
    
    print(f"\n📝 Generando foto de producto...")
    
    response = client.models.generate_content(
        model=Config.MODEL_IMAGE,
        contents=[prompt],
        config=types.GenerateContentConfig(
            response_modalities=['Image'],
            image_config=types.ImageConfig(
                aspect_ratio="1:1",
            )
        )
    )
    
    for part in response.candidates[0].content.parts:
        if part.inline_data is not None:
            image = Image.open(BytesIO(part.inline_data.data))
            filename = "generated_producto_zapatillas.png"
            image.save(filename)
            print(f"✅ Producto guardado: {filename}")

def main():
    """Ejecutar todos los tests"""
    print("\n" + "=" * 60)
    print("  🧪 SUITE DE TESTS - GENERACIÓN DE IMÁGENES")
    print("=" * 60)
    print(f"Modelo: {Config.MODEL_IMAGE}")
    print(f"API Key: {'✅ Configurada' if Config.GEMINI_API_KEY else '❌ NO configurada'}")
    
    if not Config.GEMINI_API_KEY:
        print("\n❌ ERROR: Configura GEMINI_API_KEY en el archivo .env")
        return
    
    # Crear carpeta para imágenes generadas
    os.makedirs('imagenes_generadas', exist_ok=True)
    os.chdir('imagenes_generadas')
    
    try:
        test_1_imagen_simple()
        input("\nPresiona Enter para continuar...")
        
        test_2_imagen_especifica()
        input("\nPresiona Enter para continuar...")
        
        test_3_diferentes_estilos()
        input("\nPresiona Enter para continuar...")
        
        test_4_logo_empresa()
        input("\nPresiona Enter para continuar...")
        
        test_5_estado_whatsapp()
        input("\nPresiona Enter para continuar...")
        
        test_6_producto_ecommerce()
        
        print("\n" + "=" * 60)
        print("  ✅ TODOS LOS TESTS DE GENERACIÓN COMPLETADOS")
        print("=" * 60)
        
        # Listar archivos generados
        print("\n📁 Imágenes generadas:")
        for file in os.listdir('.'):
            if file.endswith('.png'):
                print(f"   ✅ {file}")
        
        os.chdir('..')
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        os.chdir('..')

if __name__ == "__main__":
    main()
