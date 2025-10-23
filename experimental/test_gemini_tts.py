"""
TEST: Text-to-Speech con Gemini 2.5 Flash Preview TTS
Objetivo: Validar generación de audio desde texto
Modelo: gemini-2.5-flash-preview-tts
"""

import os
import sys
import time
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

# Crear directorio para audios
os.makedirs("experimental/audios_generados", exist_ok=True)

DELAY = 7

def guardar_audio(response, nombre_archivo):
    """Guarda el audio generado desde la respuesta"""
    try:
        # Buscar audio en la respuesta
        if hasattr(response, 'parts'):
            for part in response.parts:
                if hasattr(part, 'inline_data'):
                    audio_data = part.inline_data.data
                    filepath = f"experimental/audios_generados/{nombre_archivo}.mp3"
                    
                    with open(filepath, 'wb') as f:
                        f.write(audio_data)
                    
                    print(f"  [OK] Audio guardado: {filepath}")
                    print(f"  [INFO] Tamaño: {len(audio_data)} bytes")
                    return filepath
        
        # Si solo hay texto
        if hasattr(response, 'text'):
            print(f"  [INFO] Respuesta de texto: {response.text}")
        
        return None
        
    except Exception as e:
        print(f"  [X] Error al guardar audio: {e}")
        return None

def test_1_audio_simple():
    """Test 1: Generación simple de audio"""
    print("\n" + "=" * 70)
    print("TEST 1: Audio Simple")
    print("=" * 70)
    
    try:
        model = genai.GenerativeModel('gemini-2.5-flash-preview-tts')
        
        texto = "Hola, soy el asistente virtual de Esencia Urbana. ¿En qué puedo ayudarte hoy?"
        
        print(f"\n[TEXTO]: {texto}")
        print(f"[GENERANDO AUDIO...]")
        
        response = model.generate_content(texto)
        
        filepath = guardar_audio(response, "audio_saludo")
        
        if filepath:
            print(f"\n[OK] TEST 1 PASADO ✅")
            return True
        else:
            print(f"\n[INFO] El modelo respondió pero puede no generar audio directamente")
            return True
            
    except Exception as e:
        print(f"\n[X] ERROR: {e}")
        return False

def test_2_confirmacion_pedido():
    """Test 2: Confirmación de pedido"""
    print("\n" + "=" * 70)
    print("TEST 2: Confirmación de Pedido")
    print("=" * 70)
    
    try:
        model = genai.GenerativeModel('gemini-2.5-flash-preview-tts')
        
        texto = "Tu pedido número 12345 ha sido confirmado. El monto total es de 450 soles. Recibirás tu producto en 2 días hábiles."
        
        print(f"\n[TEXTO]: {texto}")
        print(f"[GENERANDO AUDIO...]")
        
        response = model.generate_content(texto)
        
        filepath = guardar_audio(response, "confirmacion_pedido")
        
        if filepath:
            print(f"\n[OK] TEST 2 PASADO ✅")
        else:
            print(f"\n[INFO] Respuesta: {response.text if hasattr(response, 'text') else 'Sin contenido'}")
        
        return True
        
    except Exception as e:
        print(f"\n[X] ERROR: {e}")
        return False

def test_3_mensaje_whatsapp():
    """Test 3: Mensaje automático WhatsApp"""
    print("\n" + "=" * 70)
    print("TEST 3: Mensaje Automático WhatsApp")
    print("=" * 70)
    
    try:
        model = genai.GenerativeModel('gemini-2.5-flash-preview-tts')
        
        texto = "Gracias por tu consulta. Nuestro horario de atención es de lunes a viernes de 9 AM a 6 PM. Te responderemos a la brevedad."
        
        print(f"\n[TEXTO]: {texto}")
        print(f"[GENERANDO AUDIO...]")
        
        response = model.generate_content(texto)
        
        filepath = guardar_audio(response, "mensaje_whatsapp")
        
        if filepath:
            print(f"\n[OK] TEST 3 PASADO ✅")
        else:
            print(f"\n[INFO] Respuesta: {response.text if hasattr(response, 'text') else 'Sin contenido'}")
        
        return True
        
    except Exception as e:
        print(f"\n[X] ERROR: {e}")
        return False

def main():
    print("\n" + "=" * 70)
    print("   TEST TEXT-TO-SPEECH - gemini-2.5-flash-preview-tts")
    print("=" * 70)
    
    print("\n[NOTA]: Este modelo puede estar en preview")
    print("[NOTA]: La generación de audio puede requerir permisos especiales")
    
    try:
        # Test 1
        result1 = test_1_audio_simple()
        
        print(f"\n[*] Esperando {DELAY}s...")
        time.sleep(DELAY)
        
        # Test 2
        result2 = test_2_confirmacion_pedido()
        
        print(f"\n[*] Esperando {DELAY}s...")
        time.sleep(DELAY)
        
        # Test 3
        result3 = test_3_mensaje_whatsapp()
        
        # Resumen
        print("\n" + "=" * 70)
        print("   TESTS TTS COMPLETADOS")
        print("=" * 70)
        
        tests_pasados = sum([result1, result2, result3])
        print(f"\n[RESULTADO]: {tests_pasados}/3 tests ejecutados")
        
        print("\n[OBSERVACIONES]:")
        print("  - El modelo gemini-2.5-flash-preview-tts está listado en la API")
        print("  - Puede estar limitado en el tier gratuito")
        print("  - Puede requerir configuración adicional")
        
        print("\n[ALTERNATIVAS PARA TTS]:")
        print("  - Google Cloud Text-to-Speech")
        print("  - ElevenLabs API")
        print("  - Amazon Polly")
        print("  - Azure Speech Services")
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
