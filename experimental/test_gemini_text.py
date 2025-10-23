"""
TEST 1: Generación de Texto con Gemini 2.5 Pro
Objetivo: Probar todas las capacidades de texto de Gemini
"""

import sys
import os
sys.path.append('..')

import google.generativeai as genai
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

def test_1_respuesta_simple():
    """Test 1: Respuesta simple sin configuración"""
    print("\n" + "=" * 60)
    print("TEST 1: Respuesta Simple")
    print("=" * 60)
    
    genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    
    response = model.generate_content(
        "¿Cómo puedo ayudar a un cliente que pregunta por envíos?"
    )
    
    print(f"\n📝 Respuesta:")
    print(response.text)
    print(f"\n✅ Tokens usados: {response.usage_metadata}")

def test_2_con_system_instruction():
    """Test 2: Respuesta con instrucciones del sistema"""
    print("\n" + "=" * 60)
    print("TEST 2: Con System Instruction")
    print("=" * 60)
    
    client = genai.Client(api_key=Config.GEMINI_API_KEY)
    
    response = client.models.generate_content(
        model=Config.MODEL_CHAT,
        config=types.GenerateContentConfig(
            system_instruction=Config.SYSTEM_INSTRUCTION,
            temperature=Config.CHAT_TEMPERATURE
        ),
        contents="Hola, ¿tienen envíos a provincia?"
    )
    
    print(f"\n📝 Respuesta con instrucciones del sistema:")
    print(response.text)

def test_3_chat_multturno():
    """Test 3: Conversación con múltiples turnos"""
    print("\n" + "=" * 60)
    print("TEST 3: Chat Multi-Turno (Contexto)")
    print("=" * 60)
    
    client = genai.Client(api_key=Config.GEMINI_API_KEY)
    
    chat = client.chats.create(
        model=Config.MODEL_CHAT,
        config=types.GenerateContentConfig(
            system_instruction=Config.SYSTEM_INSTRUCTION
        )
    )
    
    # Turno 1
    print("\n👤 Usuario: Hola, vendo zapatillas")
    response1 = chat.send_message("Hola, vendo zapatillas")
    print(f"🤖 Bot: {response1.text}")
    
    # Turno 2
    print("\n👤 Usuario: ¿Cuánto cuestan las deportivas?")
    response2 = chat.send_message("¿Cuánto cuestan las deportivas?")
    print(f"🤖 Bot: {response2.text}")
    
    # Turno 3
    print("\n👤 Usuario: ¿Hacen envíos?")
    response3 = chat.send_message("¿Hacen envíos?")
    print(f"🤖 Bot: {response3.text}")
    
    # Mostrar historial
    print("\n📜 Historial del chat:")
    for i, message in enumerate(chat.get_history()):
        role = "👤" if message.role == "user" else "🤖"
        print(f"{role} {message.role}: {message.parts[0].text[:100]}...")

def test_4_streaming():
    """Test 4: Respuesta en streaming"""
    print("\n" + "=" * 60)
    print("TEST 4: Streaming de Respuesta")
    print("=" * 60)
    
    client = genai.Client(api_key=Config.GEMINI_API_KEY)
    
    print("\n👤 Usuario: Explica en 3 párrafos cómo usar WhatsApp Business")
    print("🤖 Bot (streaming): ", end="", flush=True)
    
    response = client.models.generate_content_stream(
        model=Config.MODEL_CHAT,
        contents="Explica en 3 párrafos cómo usar WhatsApp Business"
    )
    
    for chunk in response:
        print(chunk.text, end="", flush=True)
    
    print("\n")

def test_5_diferentes_temperaturas():
    """Test 5: Comparar diferentes temperaturas"""
    print("\n" + "=" * 60)
    print("TEST 5: Comparación de Temperaturas")
    print("=" * 60)
    
    client = genai.Client(api_key=Config.GEMINI_API_KEY)
    
    pregunta = "Escribe un eslogan para una tienda de ropa juvenil"
    
    for temp in [0.0, 0.5, 1.0, 1.5]:
        print(f"\n🌡️  Temperatura: {temp}")
        response = client.models.generate_content(
            model=Config.MODEL_CHAT,
            contents=pregunta,
            config=types.GenerateContentConfig(temperature=temp)
        )
        print(f"📝 Resultado: {response.text}")

def test_6_sin_pensamiento():
    """Test 6: Desactivar pensamiento para mayor velocidad"""
    print("\n" + "=" * 60)
    print("TEST 6: Sin Pensamiento (Más Rápido)")
    print("=" * 60)
    
    client = genai.Client(api_key=Config.GEMINI_API_KEY)
    
    # Con modelo Flash y sin pensamiento
    response = client.models.generate_content(
        model=Config.MODEL_VISION,  # Flash es más rápido
        contents="¿Cuál es el resultado de 2+2?",
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0)
        )
    )
    
    print(f"\n📝 Respuesta rápida: {response.text}")

def main():
    """Ejecutar todos los tests"""
    print("\n" + "=" * 60)
    print("  🧪 SUITE DE TESTS - GENERACIÓN DE TEXTO")
    print("=" * 60)
    print(f"Modelo: {Config.MODEL_CHAT}")
    print(f"API Key: {'✅ Configurada' if Config.GEMINI_API_KEY else '❌ NO configurada'}")
    
    if not Config.GEMINI_API_KEY:
        print("\n❌ ERROR: Configura GEMINI_API_KEY en el archivo .env")
        return
    
    try:
        # Ejecutar tests
        test_1_respuesta_simple()
        input("\nPresiona Enter para continuar al siguiente test...")
        
        test_2_con_system_instruction()
        input("\nPresiona Enter para continuar al siguiente test...")
        
        test_3_chat_multturno()
        input("\nPresiona Enter para continuar al siguiente test...")
        
        test_4_streaming()
        input("\nPresiona Enter para continuar al siguiente test...")
        
        test_5_diferentes_temperaturas()
        input("\nPresiona Enter para continuar al siguiente test...")
        
        test_6_sin_pensamiento()
        
        print("\n" + "=" * 60)
        print("  ✅ TODOS LOS TESTS COMPLETADOS")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
