"""
TEST SIMPLE: Verificación rápida de Gemini API
Objetivo: Confirmar que la API funciona correctamente
NOTA: Incluye delays automáticos para evitar rate limit (10 RPM free tier)
"""

import os
import time
from dotenv import load_dotenv
import google.generativeai as genai

# Cargar variables de entorno
load_dotenv()

# Delay entre requests para evitar rate limit (6 segundos = 10 RPM)
DELAY_BETWEEN_TESTS = 7

def wait_for_rate_limit():
    """Espera para evitar rate limit"""
    print(f"\n⏳ Esperando {DELAY_BETWEEN_TESTS}s para evitar rate limit...", end="", flush=True)
    time.sleep(DELAY_BETWEEN_TESTS)
    print(" ✓")

def main():
    print("\n" + "=" * 70)
    print("   TEST DE VERIFICACIÓN GEMINI API")
    print("=" * 70)
    
    # Configurar API
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key or api_key == "TU_API_KEY_AQUI":
        print("\n❌ ERROR: GEMINI_API_KEY no configurada en .env")
        return False
    
    genai.configure(api_key=api_key)
    print(f"\n✅ API Key configurada: {api_key[:20]}...")
    
    # TEST 1: Texto simple
    print("\n" + "-" * 70)
    print("TEST 1: Generación de Texto Simple")
    print("-" * 70)
    
    try:
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        response = model.generate_content("Di 'Hola, estoy funcionando correctamente'")
        print(f"\n📝 Respuesta:")
        print(f"   {response.text}")
        print(f"\n✅ TEST 1 PASADO")
    except Exception as e:
        print(f"\n❌ TEST 1 FALLIDO: {e}")
        return False
    
    wait_for_rate_limit()  # Esperar antes del siguiente test
    
    # TEST 2: Conversación con contexto
    print("\n" + "-" * 70)
    print("TEST 2: Chat con System Instruction")
    print("-" * 70)
    
    try:
        model = genai.GenerativeModel(
            'gemini-2.0-flash-exp',
            system_instruction="Eres un asistente de ventas. Responde en español de forma amigable."
        )
        
        response = model.generate_content("¿Qué productos vendes?")
        print(f"\n📝 Respuesta:")
        print(f"   {response.text}")
        print(f"\n✅ TEST 2 PASADO")
    except Exception as e:
        print(f"\n❌ TEST 2 FALLIDO: {e}")
        return False
    
    wait_for_rate_limit()  # Esperar antes del siguiente test
    
    # TEST 3: Chat multi-turno
    print("\n" + "-" * 70)
    print("TEST 3: Conversación Multi-Turno")
    print("-" * 70)
    
    try:
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        chat = model.start_chat(history=[])
        
        # Turno 1
        print("\n👤 Usuario: Hola")
        response1 = chat.send_message("Hola")
        print(f"🤖 Bot: {response1.text}")
        
        time.sleep(DELAY_BETWEEN_TESTS)  # Delay entre mensajes
        
        # Turno 2
        print("\n👤 Usuario: ¿Recuerdas lo que te dije?")
        response2 = chat.send_message("¿Recuerdas lo que te dije?")
        print(f"🤖 Bot: {response2.text}")
        
        print(f"\n✅ TEST 3 PASADO")
    except Exception as e:
        print(f"\n❌ TEST 3 FALLIDO: {e}")
        return False
    
    wait_for_rate_limit()  # Esperar antes del siguiente test
    
    # TEST 4: Respuesta con parámetros
    print("\n" + "-" * 70)
    print("TEST 4: Respuesta con Temperatura")
    print("-" * 70)
    
    try:
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        
        # Creativa (temperatura alta)
        print("\n🔥 Con temperatura 1.0 (creativa):")
        response_creative = model.generate_content(
            "Dame 3 nombres para una tienda de ropa",
            generation_config=genai.types.GenerationConfig(
                temperature=1.0,
            )
        )
        print(f"   {response_creative.text}")
        
        time.sleep(DELAY_BETWEEN_TESTS)  # Delay entre las dos llamadas del mismo test
        
        # Conservadora (temperatura baja)
        print("\n❄️  Con temperatura 0.1 (precisa):")
        response_precise = model.generate_content(
            "Dame 3 nombres para una tienda de ropa",
            generation_config=genai.types.GenerationConfig(
                temperature=0.1,
            )
        )
        print(f"   {response_precise.text}")
        
        print(f"\n✅ TEST 4 PASADO")
    except Exception as e:
        print(f"\n❌ TEST 4 FALLIDO: {e}")
        return False
    
    wait_for_rate_limit()  # Esperar antes del último test
    
    # TEST 5: Streaming
    print("\n" + "-" * 70)
    print("TEST 5: Respuesta en Streaming")
    print("-" * 70)
    
    try:
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        
        print("\n📡 Recibiendo respuesta en tiempo real:")
        print("   ", end="", flush=True)
        
        response = model.generate_content(
            "Cuenta del 1 al 10 lentamente",
            stream=True
        )
        
        for chunk in response:
            if chunk.text:
                print(chunk.text, end="", flush=True)
        
        print("\n\n✅ TEST 5 PASADO")
    except Exception as e:
        print(f"\n❌ TEST 5 FALLIDO: {e}")
        return False
    
    # Resumen final
    print("\n" + "=" * 70)
    print("   ✨ TODOS LOS TESTS PASARON EXITOSAMENTE ✨")
    print("=" * 70)
    print("\n📌 PRÓXIMOS PASOS:")
    print("   1. Probar test_gemini_vision.py (imágenes)")
    print("   2. Probar test_gemini_json.py (salida estructurada)")
    print("   3. Continuar con desarrollo del bot de WhatsApp")
    print("")
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Test interrumpido por el usuario")
        exit(1)
    except Exception as e:
        print(f"\n\n❌ ERROR INESPERADO: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
