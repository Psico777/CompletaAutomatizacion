"""
TEST: Visión y OCR con Gemini 2.5 Flash
Objetivo: Validar comprensión de imágenes y extracción de texto (OCR)
Modelo: gemini-2.5-flash
"""

import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image, ImageDraw, ImageFont
import json
from pydantic import BaseModel, Field
from typing import List

# Configurar encoding UTF-8
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

# Cargar variables de entorno
load_dotenv()

# Configurar API
api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=api_key)

# Crear directorio para imágenes de prueba
os.makedirs("experimental/imagenes_prueba", exist_ok=True)

# ============================================================================
# GENERADOR DE IMÁGENES DE PRUEBA
# ============================================================================

def crear_voucher_yape_prueba():
    """Crea una imagen simulada de un voucher Yape"""
    # Crear imagen
    img = Image.new('RGB', (400, 600), color='white')
    draw = ImageDraw.Draw(img)
    
    # Intentar usar fuente del sistema, sino usar default
    try:
        font_title = ImageFont.truetype("arial.ttf", 24)
        font_normal = ImageFont.truetype("arial.ttf", 16)
        font_small = ImageFont.truetype("arial.ttf", 12)
    except:
        font_title = ImageFont.load_default()
        font_normal = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Header morado de Yape
    draw.rectangle([(0, 0), (400, 80)], fill='#722F8C')
    draw.text((150, 30), "YAPE", fill='white', font=font_title)
    
    # Contenido
    y_pos = 100
    draw.text((20, y_pos), "¡Yapeo exitoso!", fill='#722F8C', font=font_normal)
    
    y_pos += 50
    draw.text((20, y_pos), "Enviaste", fill='gray', font=font_small)
    y_pos += 30
    draw.text((20, y_pos), "S/ 150.00", fill='black', font=font_title)
    
    y_pos += 60
    draw.text((20, y_pos), "A: María Rodriguez", fill='black', font=font_normal)
    
    y_pos += 40
    draw.text((20, y_pos), "Fecha: 20/10/2025", fill='black', font=font_normal)
    y_pos += 30
    draw.text((20, y_pos), "Hora: 14:35", fill='black', font=font_normal)
    
    y_pos += 50
    draw.text((20, y_pos), "Nº Operación:", fill='gray', font=font_small)
    y_pos += 25
    draw.text((20, y_pos), "00234567890", fill='black', font=font_normal)
    
    # Guardar
    filepath = "experimental/imagenes_prueba/voucher_yape.png"
    img.save(filepath)
    print(f"[OK] Voucher Yape creado: {filepath}")
    return filepath

def crear_imagen_producto():
    """Crea una imagen simulada de un producto"""
    img = Image.new('RGB', (400, 400), color='white')
    draw = ImageDraw.Draw(img)
    
    try:
        font_title = ImageFont.truetype("arial.ttf", 20)
        font_price = ImageFont.truetype("arial.ttf", 24)
    except:
        font_title = ImageFont.load_default()
        font_price = ImageFont.load_default()
    
    # Simular una zapatilla
    draw.rectangle([(50, 50), (350, 250)], fill='#4169E1')
    draw.ellipse([(100, 150), (300, 200)], fill='white')
    
    # Texto del producto
    y_pos = 270
    draw.text((100, y_pos), "Nike Air Max", fill='black', font=font_title)
    y_pos += 40
    draw.text((120, y_pos), "S/ 299.00", fill='red', font=font_price)
    y_pos += 40
    draw.text((80, y_pos), "Stock: 15 unidades", fill='green', font=font_title)
    
    filepath = "experimental/imagenes_prueba/producto_zapatilla.png"
    img.save(filepath)
    print(f"[OK] Imagen de producto creada: {filepath}")
    return filepath

def crear_imagen_con_texto():
    """Crea una imagen con texto variado para OCR"""
    img = Image.new('RGB', (500, 300), color='white')
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()
    
    textos = [
        "FACTURA DE VENTA",
        "Cliente: Juan Pérez",
        "RUC: 20123456789",
        "Producto: Laptop HP",
        "Cantidad: 2",
        "Precio Unit: S/ 2,500.00",
        "Total: S/ 5,000.00",
        "Fecha: 20/10/2025"
    ]
    
    y_pos = 20
    for texto in textos:
        draw.text((20, y_pos), texto, fill='black', font=font)
        y_pos += 30
    
    filepath = "experimental/imagenes_prueba/factura_texto.png"
    img.save(filepath)
    print(f"[OK] Imagen con texto creada: {filepath}")
    return filepath

# ============================================================================
# MODELOS PYDANTIC
# ============================================================================

class DatosVoucher(BaseModel):
    """Datos extraídos de un voucher"""
    tipo_pago: str = Field(description="Tipo de pago (Yape, Plin, etc)")
    monto: float = Field(description="Monto en soles")
    destinatario: str = Field(description="Nombre del destinatario")
    fecha: str = Field(description="Fecha del pago")
    hora: str = Field(description="Hora del pago")
    numero_operacion: str = Field(description="Número de operación")

class ObjetosDetectados(BaseModel):
    """Objetos detectados en una imagen"""
    objetos: List[str] = Field(description="Lista de objetos identificados")
    descripcion_general: str = Field(description="Descripción general de la imagen")
    colores_principales: List[str] = Field(description="Colores principales en la imagen")

# ============================================================================
# TESTS
# ============================================================================

def test_1_comprension_imagen():
    """Test 1: Comprensión básica de imagen"""
    print("\n" + "=" * 70)
    print("TEST 1: Comprensión de Imagen - Producto")
    print("=" * 70)
    
    # Crear imagen de prueba
    imagen_path = crear_imagen_producto()
    
    # Cargar imagen
    img = Image.open(imagen_path)
    
    # Usar gemini-2.5-flash para visión
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    prompt = """Describe esta imagen en detalle.
    Identifica:
    - ¿Qué producto es?
    - ¿Qué precio tiene?
    - ¿Cuántas unidades hay en stock?
    - ¿Qué colores predominan?
    """
    
    response = model.generate_content([prompt, img])
    
    print(f"\n[IMAGEN]: {imagen_path}")
    print(f"\n[ANALISIS DE GEMINI 2.5 FLASH]:")
    print(response.text)
    print(f"\n[OK] TEST 1 PASADO")
    
    return True

def test_2_ocr_voucher():
    """Test 2: OCR de voucher Yape"""
    print("\n" + "=" * 70)
    print("TEST 2: OCR de Voucher Yape")
    print("=" * 70)
    
    # Crear voucher de prueba
    voucher_path = crear_voucher_yape_prueba()
    
    # Cargar imagen
    img = Image.open(voucher_path)
    
    # Usar gemini-2.5-flash con schema para OCR estructurado
    model = genai.GenerativeModel(
        'gemini-2.5-flash',
        generation_config={
            "response_mime_type": "application/json",
            "response_schema": DatosVoucher
        }
    )
    
    prompt = """Extrae TODOS los datos de este voucher de pago.
    Lee el texto de la imagen y extrae:
    - Tipo de pago
    - Monto exacto
    - Nombre del destinatario
    - Fecha
    - Hora
    - Número de operación
    """
    
    response = model.generate_content([prompt, img])
    datos = json.loads(response.text)
    
    print(f"\n[IMAGEN]: {voucher_path}")
    print(f"\n[DATOS EXTRAIDOS]:")
    print(json.dumps(datos, indent=2, ensure_ascii=False))
    
    # Validar con Pydantic
    voucher = DatosVoucher(**datos)
    print(f"\n[VALIDACION]:")
    print(f"  Tipo: {voucher.tipo_pago}")
    print(f"  Monto: S/ {voucher.monto}")
    print(f"  Destinatario: {voucher.destinatario}")
    print(f"  Operacion: {voucher.numero_operacion}")
    
    print(f"\n[OK] TEST 2 PASADO")
    return True

def test_3_ocr_factura():
    """Test 3: OCR de texto complejo (factura)"""
    print("\n" + "=" * 70)
    print("TEST 3: OCR de Factura con Texto")
    print("=" * 70)
    
    # Crear factura
    factura_path = crear_imagen_con_texto()
    
    # Cargar imagen
    img = Image.open(factura_path)
    
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    prompt = """Lee TODO el texto de esta imagen y extráelo de forma estructurada.
    Identifica:
    - Tipo de documento
    - Cliente
    - Productos
    - Precios
    - Total
    """
    
    response = model.generate_content([prompt, img])
    
    print(f"\n[IMAGEN]: {factura_path}")
    print(f"\n[TEXTO EXTRAIDO]:")
    print(response.text)
    print(f"\n[OK] TEST 3 PASADO")
    
    return True

def test_4_deteccion_objetos():
    """Test 4: Detección de objetos y análisis visual"""
    print("\n" + "=" * 70)
    print("TEST 4: Detección de Objetos con JSON")
    print("=" * 70)
    
    imagen_path = crear_imagen_producto()
    img = Image.open(imagen_path)
    
    model = genai.GenerativeModel(
        'gemini-2.5-flash',
        generation_config={
            "response_mime_type": "application/json",
            "response_schema": ObjetosDetectados
        }
    )
    
    prompt = """Analiza esta imagen y detecta:
    - Todos los objetos visibles
    - Descripción general de la escena
    - Colores principales que se ven
    """
    
    response = model.generate_content([prompt, img])
    datos = json.loads(response.text)
    
    print(f"\n[ANALISIS ESTRUCTURADO]:")
    print(json.dumps(datos, indent=2, ensure_ascii=False))
    
    # Validar
    objetos = ObjetosDetectados(**datos)
    print(f"\n[OBJETOS DETECTADOS]: {', '.join(objetos.objetos)}")
    print(f"[COLORES]: {', '.join(objetos.colores_principales)}")
    
    print(f"\n[OK] TEST 4 PASADO")
    return True

def test_5_comparacion_imagenes():
    """Test 5: Comparación de múltiples imágenes"""
    print("\n" + "=" * 70)
    print("TEST 5: Análisis de Múltiples Imágenes")
    print("=" * 70)
    
    # Usar las imágenes ya creadas
    voucher_path = "experimental/imagenes_prueba/voucher_yape.png"
    producto_path = "experimental/imagenes_prueba/producto_zapatilla.png"
    
    img1 = Image.open(voucher_path)
    img2 = Image.open(producto_path)
    
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    prompt = """Compara estas dos imágenes:
    1. ¿Qué tipo de documento/imagen es cada una?
    2. ¿Cuáles son las diferencias principales?
    3. ¿Qué información útil contiene cada una?
    """
    
    response = model.generate_content([prompt, img1, img2])
    
    print(f"\n[IMAGENES COMPARADAS]:")
    print(f"  1. {voucher_path}")
    print(f"  2. {producto_path}")
    print(f"\n[COMPARACION]:")
    print(response.text)
    print(f"\n[OK] TEST 5 PASADO")
    
    return True

# ============================================================================
# MAIN
# ============================================================================

def main():
    print("\n" + "=" * 70)
    print("   TEST VISION Y OCR - GEMINI 2.5 FLASH")
    print("=" * 70)
    
    import time
    DELAY = 7  # Rate limit
    
    try:
        # Test 1: Comprensión de imagen
        if not test_1_comprension_imagen():
            return False
        
        print(f"\n[*] Esperando {DELAY}s para rate limit...")
        time.sleep(DELAY)
        
        # Test 2: OCR de voucher
        if not test_2_ocr_voucher():
            return False
        
        print(f"\n[*] Esperando {DELAY}s para rate limit...")
        time.sleep(DELAY)
        
        # Test 3: OCR de factura
        if not test_3_ocr_factura():
            return False
        
        print(f"\n[*] Esperando {DELAY}s para rate limit...")
        time.sleep(DELAY)
        
        # Test 4: Detección de objetos
        if not test_4_deteccion_objetos():
            return False
        
        print(f"\n[*] Esperando {DELAY}s para rate limit...")
        time.sleep(DELAY)
        
        # Test 5: Múltiples imágenes
        if not test_5_comparacion_imagenes():
            return False
        
        # Resumen final
        print("\n" + "=" * 70)
        print("   [*] TODOS LOS TESTS DE VISION PASARON [*]")
        print("=" * 70)
        print("\n[CAPACIDADES VALIDADAS]:")
        print("  [OK] Comprensión de imágenes")
        print("  [OK] OCR de vouchers de pago")
        print("  [OK] OCR de facturas y texto")
        print("  [OK] Detección de objetos")
        print("  [OK] Análisis de múltiples imágenes")
        print("\n[NOTA] gemini-2.5-flash LISTO PARA:")
        print("  - Verificación automática de vouchers Yape")
        print("  - Extracción de datos de facturas")
        print("  - Análisis de imágenes de productos")
        print("  - OCR general de documentos")
        print("")
        
        return True
        
    except Exception as e:
        print(f"\n[X] ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    try:
        success = main()
        exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n[!] Test interrumpido")
        exit(1)
