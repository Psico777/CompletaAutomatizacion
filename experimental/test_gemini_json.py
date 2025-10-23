"""
TEST 5: Salida JSON Estructurada con Pydantic
Objetivo: Probar generación de datos estructurados para el proyecto
"""

import sys
sys.path.append('..')

from google import genai
from google.genai import types
from config import Config
from pydantic import BaseModel
from typing import List, Optional
from enum import Enum
import json

def test_1_extraccion_pago_basica():
    """Test 1: Extraer datos básicos de pago"""
    print("\n" + "=" * 60)
    print("TEST 1: Extracción de Datos de Pago")
    print("=" * 60)
    
    class DatosPago(BaseModel):
        monto: float
        nombre_pagador: str
        fecha: str
        hora: str
        numero_operacion: str
    
    client = genai.Client(api_key=Config.GEMINI_API_KEY)
    
    texto_voucher = """
    Yape realizado con éxito
    Monto: S/ 250.50
    De: María García López
    Fecha: 22/10/2025
    Hora: 15:45
    Nro. Operación: 123456789
    """
    
    print(f"\n📄 Texto del voucher:")
    print(texto_voucher)
    
    response = client.models.generate_content(
        model=Config.MODEL_VISION,
        contents=f"Extrae los datos de este voucher de pago: {texto_voucher}",
        config={
            "response_mime_type": "application/json",
            "response_schema": DatosPago,
        },
    )
    
    print(f"\n📊 JSON generado:")
    print(response.text)
    
    if response.parsed:
        pago = response.parsed
        print(f"\n✅ Datos parseados:")
        print(f"   💰 Monto: S/ {pago.monto}")
        print(f"   👤 Pagador: {pago.nombre_pagador}")
        print(f"   📅 Fecha: {pago.fecha}")
        print(f"   🕐 Hora: {pago.hora}")
        print(f"   🔢 Operación: {pago.numero_operacion}")

def test_2_clasificacion_mensaje():
    """Test 2: Clasificar intención de mensajes de clientes"""
    print("\n" + "=" * 60)
    print("TEST 2: Clasificación de Mensajes")
    print("=" * 60)
    
    class TipoConsulta(str, Enum):
        PRECIO = "precio"
        ENVIO = "envio"
        DISPONIBILIDAD = "disponibilidad"
        PAGO = "pago"
        QUEJA = "queja"
        OTRO = "otro"
    
    class ClasificacionMensaje(BaseModel):
        tipo: TipoConsulta
        urgencia: str  # "alta", "media", "baja"
        requiere_atencion_humana: bool
    
    client = genai.Client(api_key=Config.GEMINI_API_KEY)
    
    mensajes = [
        "Hola, ¿cuánto cuestan las zapatillas Nike?",
        "¡Urgente! Mi pedido no ha llegado y ya pasó una semana",
        "¿Hacen envíos a provincia?",
        "Ya realicé el pago, adjunto voucher"
    ]
    
    for mensaje in mensajes:
        print(f"\n💬 Mensaje: \"{mensaje}\"")
        
        response = client.models.generate_content(
            model=Config.MODEL_LITE,  # Lite para clasificación rápida
            contents=f"Clasifica este mensaje de cliente: {mensaje}",
            config={
                "response_mime_type": "application/json",
                "response_schema": ClasificacionMensaje,
            },
        )
        
        if response.parsed:
            clase = response.parsed
            print(f"   📋 Tipo: {clase.tipo.value}")
            print(f"   ⚡ Urgencia: {clase.urgencia}")
            print(f"   👨‍💼 Requiere humano: {'Sí' if clase.requiere_atencion_humana else 'No'}")

def test_3_lista_productos():
    """Test 3: Generar lista estructurada de productos"""
    print("\n" + "=" * 60)
    print("TEST 3: Lista de Productos Estructurada")
    print("=" * 60)
    
    class Producto(BaseModel):
        nombre: str
        precio: float
        categoria: str
        disponible: bool
    
    client = genai.Client(api_key=Config.GEMINI_API_KEY)
    
    prompt = """
    Genera 5 productos de ejemplo para una tienda de ropa juvenil.
    Incluye nombre, precio en soles, categoría y disponibilidad.
    """
    
    response = client.models.generate_content(
        model=Config.MODEL_CHAT,
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": List[Producto],
        },
    )
    
    print(f"\n📦 Productos generados:")
    print(response.text)
    
    if response.parsed:
        productos = response.parsed
        print(f"\n✅ Lista parseada ({len(productos)} productos):")
        for i, prod in enumerate(productos, 1):
            disponibilidad = "✅ Disponible" if prod.disponible else "❌ Agotado"
            print(f"\n   {i}. {prod.nombre}")
            print(f"      💰 S/ {prod.precio}")
            print(f"      🏷️  {prod.categoria}")
            print(f"      📦 {disponibilidad}")

def test_4_analisis_conversacion():
    """Test 4: Analizar conversación completa"""
    print("\n" + "=" * 60)
    print("TEST 4: Análisis de Conversación")
    print("=" * 60)
    
    class Sentimiento(str, Enum):
        POSITIVO = "positivo"
        NEUTRAL = "neutral"
        NEGATIVO = "negativo"
    
    class AnalisisConversacion(BaseModel):
        sentimiento_general: Sentimiento
        temas_principales: List[str]
        cliente_satisfecho: bool
        resumen: str
    
    client = genai.Client(api_key=Config.GEMINI_API_KEY)
    
    conversacion = """
    Cliente: Hola, compré unas zapatillas hace 3 días
    Bot: ¡Hola! ¿En qué puedo ayudarte con tu pedido?
    Cliente: Aún no me llega, estoy preocupado
    Bot: Entiendo tu preocupación. ¿Podrías darme tu número de pedido?
    Cliente: Es el #12345
    Bot: Gracias. Veo que está en camino, llegará mañana.
    Cliente: Ah perfecto, gracias por la información
    """
    
    print(f"\n💬 Conversación:")
    print(conversacion)
    
    response = client.models.generate_content(
        model=Config.MODEL_CHAT,
        contents=f"Analiza esta conversación: {conversacion}",
        config={
            "response_mime_type": "application/json",
            "response_schema": AnalisisConversacion,
        },
    )
    
    print(f"\n📊 Análisis JSON:")
    print(response.text)
    
    if response.parsed:
        analisis = response.parsed
        print(f"\n✅ Resultado:")
        print(f"   😊 Sentimiento: {analisis.sentimiento_general.value}")
        print(f"   📝 Temas: {', '.join(analisis.temas_principales)}")
        print(f"   ✅ Cliente satisfecho: {'Sí' if analisis.cliente_satisfecho else 'No'}")
        print(f"   💭 Resumen: {analisis.resumen}")

def test_5_validacion_pago_completa():
    """Test 5: Validación completa de pago con enums"""
    print("\n" + "=" * 60)
    print("TEST 5: Validación Completa de Pago")
    print("=" * 60)
    
    class TipoPago(str, Enum):
        YAPE = "yape"
        PLIN = "plin"
        TRANSFERENCIA = "transferencia"
        OTRO = "otro"
    
    class EstadoValidacion(str, Enum):
        VALIDO = "valido"
        MONTO_INCORRECTO = "monto_incorrecto"
        FECHA_ANTIGUA = "fecha_antigua"
        DUPLICADO = "duplicado"
        NO_LEGIBLE = "no_legible"
    
    class ValidacionPago(BaseModel):
        tipo_pago: TipoPago
        monto: float
        nombre_pagador: str
        fecha: str
        hora: str
        numero_operacion: str
        estado_validacion: EstadoValidacion
        mensaje_validacion: str
    
    client = genai.Client(api_key=Config.GEMINI_API_KEY)
    
    texto = """
    Yape - Transferencia exitosa
    S/ 150.00
    De: Juan Pérez Rodríguez
    22/10/2025 - 14:30
    Op: 987654321
    """
    
    print(f"\n📄 Datos del pago:")
    print(texto)
    print("\nℹ️  Monto esperado: S/ 150.00")
    
    response = client.models.generate_content(
        model=Config.MODEL_VISION,
        contents=f"Valida este pago. Monto esperado: S/ 150.00. Datos: {texto}",
        config={
            "response_mime_type": "application/json",
            "response_schema": ValidacionPago,
        },
    )
    
    print(f"\n📊 Validación JSON:")
    print(response.text)
    
    if response.parsed:
        validacion = response.parsed
        print(f"\n✅ Resultado de Validación:")
        print(f"   💳 Tipo: {validacion.tipo_pago.value.upper()}")
        print(f"   💰 Monto: S/ {validacion.monto}")
        print(f"   👤 Pagador: {validacion.nombre_pagador}")
        print(f"   📅 Fecha: {validacion.fecha} a las {validacion.hora}")
        print(f"   🔢 Operación: {validacion.numero_operacion}")
        print(f"   ⚠️  Estado: {validacion.estado_validacion.value.upper()}")
        print(f"   💬 Mensaje: {validacion.mensaje_validacion}")

def main():
    """Ejecutar todos los tests"""
    print("\n" + "=" * 60)
    print("  🧪 SUITE DE TESTS - JSON ESTRUCTURADO")
    print("=" * 60)
    print(f"API Key: {'✅ Configurada' if Config.GEMINI_API_KEY else '❌ NO configurada'}")
    
    if not Config.GEMINI_API_KEY:
        print("\n❌ ERROR: Configura GEMINI_API_KEY en el archivo .env")
        return
    
    try:
        test_1_extraccion_pago_basica()
        input("\nPresiona Enter para continuar...")
        
        test_2_clasificacion_mensaje()
        input("\nPresiona Enter para continuar...")
        
        test_3_lista_productos()
        input("\nPresiona Enter para continuar...")
        
        test_4_analisis_conversacion()
        input("\nPresiona Enter para continuar...")
        
        test_5_validacion_pago_completa()
        
        print("\n" + "=" * 60)
        print("  ✅ TODOS LOS TESTS DE JSON COMPLETADOS")
        print("=" * 60)
        print("\n💡 Casos de uso demostrados:")
        print("   ✅ Extracción de datos de pagos")
        print("   ✅ Clasificación de mensajes")
        print("   ✅ Generación de listas estructuradas")
        print("   ✅ Análisis de conversaciones")
        print("   ✅ Validación completa con enums")
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
