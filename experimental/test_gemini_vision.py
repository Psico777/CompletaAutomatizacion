"""
TEST 2: Comprensión de Imágenes y OCR con Gemini Vision
Objetivo: Probar capacidades de visión y extracción de texto de imágenes
"""

import sys
sys.path.append('..')

from google import genai
from google.genai import types
from config import Config
from PIL import Image, ImageDraw, ImageFont
import io

def crear_imagen_prueba_voucher():
    """Crear una imagen de prueba que simula un voucher Yape"""
    # Crear imagen
    img = Image.new('RGB', (400, 600), color='white')
    draw = ImageDraw.Draw(img)
    
    # Simular diseño de voucher Yape
    # Fondo morado arriba
    draw.rectangle([(0, 0), (400, 150)], fill='#722F95')
    
    # Texto en el voucher
    try:
        font_large = ImageFont.truetype("arial.ttf", 40)
        font_medium = ImageFont.truetype("arial.ttf", 24)
        font_small = ImageFont.truetype("arial.ttf", 18)
    except:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Título
    draw.text((150, 50), "Yape", fill='white', font=font_large)
    
    # Monto
    draw.text((120, 180), "S/ 150.00", fill='black', font=font_large)
    draw.text((130, 230), "Transferencia exitosa", fill='green', font=font_small)
    
    # Detalles
    y_pos = 280
    detalles = [
        "De: Juan Pérez",
        "Fecha: 22/10/2025",
        "Hora: 14:30",
        "Nro. Operación: 987654321",
        "Tipo: Yape"
    ]
    
    for detalle in detalles:
        draw.text((50, y_pos), detalle, fill='black', font=font_small)
        y_pos += 35
    
    # Guardar
    img.save('voucher_prueba.jpg')
    return 'voucher_prueba.jpg'

def test_1_imagen_local():
    """Test 1: Analizar imagen local"""
    print("\n" + "=" * 60)
    print("TEST 1: Comprensión de Imagen Local")
    print("=" * 60)
    
    # Crear voucher de prueba
    print("\n📸 Creando imagen de voucher de prueba...")
    ruta_imagen = crear_imagen_prueba_voucher()
    print(f"✅ Imagen creada: {ruta_imagen}")
    
    client = genai.Client(api_key=Config.GEMINI_API_KEY)
    
    with open(ruta_imagen, 'rb') as f:
        image_bytes = f.read()
    
    response = client.models.generate_content(
        model=Config.MODEL_VISION,
        contents=[
            types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg'),
            "Describe todo lo que ves en esta imagen"
        ]
    )
    
    print(f"\n🤖 Descripción de la imagen:")
    print(response.text)

def test_2_ocr_voucher():
    """Test 2: Extraer datos de voucher con OCR"""
    print("\n" + "=" * 60)
    print("TEST 2: OCR de Voucher Yape")
    print("=" * 60)
    
    client = genai.Client(api_key=Config.GEMINI_API_KEY)
    
    with open('voucher_prueba.jpg', 'rb') as f:
        image_bytes = f.read()
    
    response = client.models.generate_content(
        model=Config.MODEL_VISION,
        contents=[
            types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg'),
            """
            Extrae la siguiente información de este voucher:
            - Monto pagado
            - Nombre del pagador
            - Fecha de la transacción
            - Hora de la transacción
            - Número de operación
            - Tipo de pago (Yape, Plin, etc)
            
            Proporciona la información de forma clara y estructurada.
            """
        ]
    )
    
    print(f"\n📋 Datos extraídos del voucher:")
    print(response.text)

def test_3_ocr_json_estructurado():
    """Test 3: Extraer datos como JSON estructurado"""
    print("\n" + "=" * 60)
    print("TEST 3: OCR con Salida JSON Estructurada")
    print("=" * 60)
    
    from pydantic import BaseModel
    
    class DatosVoucher(BaseModel):
        monto: float
        nombre_pagador: str
        fecha: str
        hora: str
        numero_operacion: str
        tipo_pago: str
    
    client = genai.Client(api_key=Config.GEMINI_API_KEY)
    
    with open('voucher_prueba.jpg', 'rb') as f:
        image_bytes = f.read()
    
    response = client.models.generate_content(
        model=Config.MODEL_VISION,
        contents=[
            types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg'),
            "Extrae los datos de este voucher de pago"
        ],
        config={
            "response_mime_type": "application/json",
            "response_schema": DatosVoucher,
        },
    )
    
    print(f"\n📊 JSON estructurado:")
    print(response.text)
    
    # Usar objeto parseado
    if response.parsed:
        datos = response.parsed
        print(f"\n✅ Datos parseados:")
        print(f"   Monto: S/ {datos.monto}")
        print(f"   Pagador: {datos.nombre_pagador}")
        print(f"   Fecha: {datos.fecha}")
        print(f"   Hora: {datos.hora}")
        print(f"   Operación: {datos.numero_operacion}")
        print(f"   Tipo: {datos.tipo_pago}")

def test_4_multiples_imagenes():
    """Test 4: Comparar múltiples imágenes"""
    print("\n" + "=" * 60)
    print("TEST 4: Análisis de Múltiples Imágenes")
    print("=" * 60)
    
    # Crear dos imágenes diferentes
    img1 = Image.new('RGB', (200, 200), color='red')
    img2 = Image.new('RGB', (200, 200), color='blue')
    
    img1.save('imagen1.jpg')
    img2.save('imagen2.jpg')
    
    client = genai.Client(api_key=Config.GEMINI_API_KEY)
    
    with open('imagen1.jpg', 'rb') as f1:
        img1_bytes = f1.read()
    
    with open('imagen2.jpg', 'rb') as f2:
        img2_bytes = f2.read()
    
    response = client.models.generate_content(
        model=Config.MODEL_VISION,
        contents=[
            "¿Qué diferencias hay entre estas dos imágenes?",
            types.Part.from_bytes(data=img1_bytes, mime_type='image/jpeg'),
            types.Part.from_bytes(data=img2_bytes, mime_type='image/jpeg')
        ]
    )
    
    print(f"\n🔍 Comparación de imágenes:")
    print(response.text)

def test_5_deteccion_objetos():
    """Test 5: Detección de objetos en imagen"""
    print("\n" + "=" * 60)
    print("TEST 5: Detección de Objetos")
    print("=" * 60)
    
    # Crear imagen con formas
    img = Image.new('RGB', (400, 400), color='white')
    draw = ImageDraw.Draw(img)
    
    # Dibujar círculo rojo
    draw.ellipse([(50, 50), (150, 150)], fill='red')
    # Dibujar rectángulo azul
    draw.rectangle([(200, 50), (350, 200)], fill='blue')
    # Dibujar triángulo verde
    draw.polygon([(200, 250), (300, 350), (100, 350)], fill='green')
    
    img.save('objetos.jpg')
    
    client = genai.Client(api_key=Config.GEMINI_API_KEY)
    
    with open('objetos.jpg', 'rb') as f:
        img_bytes = f.read()
    
    response = client.models.generate_content(
        model=Config.MODEL_VISION,
        contents=[
            types.Part.from_bytes(data=img_bytes, mime_type='image/jpeg'),
            "Identifica y describe todas las formas y colores que ves en esta imagen"
        ]
    )
    
    print(f"\n🎨 Objetos detectados:")
    print(response.text)

def main():
    """Ejecutar todos los tests"""
    print("\n" + "=" * 60)
    print("  🧪 SUITE DE TESTS - VISIÓN E IMÁGENES")
    print("=" * 60)
    print(f"Modelo: {Config.MODEL_VISION}")
    print(f"API Key: {'✅ Configurada' if Config.GEMINI_API_KEY else '❌ NO configurada'}")
    
    if not Config.GEMINI_API_KEY:
        print("\n❌ ERROR: Configura GEMINI_API_KEY en el archivo .env")
        return
    
    try:
        # Ejecutar tests
        test_1_imagen_local()
        input("\nPresiona Enter para continuar al siguiente test...")
        
        test_2_ocr_voucher()
        input("\nPresiona Enter para continuar al siguiente test...")
        
        test_3_ocr_json_estructurado()
        input("\nPresiona Enter para continuar al siguiente test...")
        
        test_4_multiples_imagenes()
        input("\nPresiona Enter para continuar al siguiente test...")
        
        test_5_deteccion_objetos()
        
        print("\n" + "=" * 60)
        print("  ✅ TODOS LOS TESTS DE VISIÓN COMPLETADOS")
        print("=" * 60)
        print("\n📁 Archivos generados:")
        print("   - voucher_prueba.jpg")
        print("   - imagen1.jpg")
        print("   - imagen2.jpg")
        print("   - objetos.jpg")
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
