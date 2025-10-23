"""
TEST 4: Texto a Voz (TTS) con Gemini 2.5 Flash TTS
Objetivo: Probar generación de audio desde texto
"""

import sys
sys.path.append('..')

from google import genai
from google.genai import types
from config import Config
import wave
import os

def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
    """Guardar audio en formato WAV"""
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)

def test_1_voz_simple():
    """Test 1: Generar audio simple"""
    print("\n" + "=" * 60)
    print("TEST 1: Texto a Voz Simple")
    print("=" * 60)
    
    client = genai.Client(api_key=Config.GEMINI_API_KEY)
    
    texto = "¡Bienvenido a nuestra tienda! Tenemos las mejores ofertas para ti."
    
    print(f"\n📝 Texto: {texto}")
    print("🎤 Generando audio...")
    
    response = client.models.generate_content(
        model=Config.MODEL_TTS,
        contents=f"Di con entusiasmo: {texto}",
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Kore',  # Voz brillante
                    )
                )
            ),
        )
    )
    
    data = response.candidates[0].content.parts[0].inline_data.data
    filename = 'audio_bienvenida.wav'
    wave_file(filename, data)
    print(f"✅ Audio guardado: {filename}")

def test_2_diferentes_voces():
    """Test 2: Probar diferentes voces"""
    print("\n" + "=" * 60)
    print("TEST 2: Diferentes Voces")
    print("=" * 60)
    
    client = genai.Client(api_key=Config.GEMINI_API_KEY)
    
    voces = ['Kore', 'Puck', 'Charon', 'Fenrir', 'Aoede']
    texto = "Hola, esta es una prueba de voz"
    
    for voz in voces:
        print(f"\n🎤 Generando con voz: {voz}")
        
        response = client.models.generate_content(
            model=Config.MODEL_TTS,
            contents=texto,
            config=types.GenerateContentConfig(
                response_modalities=["AUDIO"],
                speech_config=types.SpeechConfig(
                    voice_config=types.VoiceConfig(
                        prebuilt_voice_config=types.PrebuiltVoiceConfig(
                            voice_name=voz,
                        )
                    )
                ),
            )
        )
        
        data = response.candidates[0].content.parts[0].inline_data.data
        filename = f'audio_voz_{voz.lower()}.wav'
        wave_file(filename, data)
        print(f"   ✅ Guardado: {filename}")

def test_3_diferentes_estilos():
    """Test 3: Diferentes estilos de habla"""
    print("\n" + "=" * 60)
    print("TEST 3: Diferentes Estilos de Habla")
    print("=" * 60)
    
    client = genai.Client(api_key=Config.GEMINI_API_KEY)
    
    estilos = [
        ("alegre", "Di con mucha alegría y energía: ¡Tenemos promociones increíbles!"),
        ("susurro", "Di en un susurro misterioso: Por tiempo limitado..."),
        ("serio", "Di de forma seria y profesional: Atención a nuestros clientes"),
        ("emocionado", "Di muy emocionado: ¡No te lo puedes perder!")
    ]
    
    for nombre_estilo, prompt in estilos:
        print(f"\n🎭 Estilo: {nombre_estilo}")
        print(f"   Prompt: {prompt}")
        
        response = client.models.generate_content(
            model=Config.MODEL_TTS,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=["AUDIO"],
                speech_config=types.SpeechConfig(
                    voice_config=types.VoiceConfig(
                        prebuilt_voice_config=types.PrebuiltVoiceConfig(
                            voice_name='Kore',
                        )
                    )
                ),
            )
        )
        
        data = response.candidates[0].content.parts[0].inline_data.data
        filename = f'audio_estilo_{nombre_estilo}.wav'
        wave_file(filename, data)
        print(f"   ✅ Guardado: {filename}")

def test_4_conversacion_dos_personas():
    """Test 4: Conversación entre dos personas"""
    print("\n" + "=" * 60)
    print("TEST 4: Conversación Multi-Hablante")
    print("=" * 60)
    
    client = genai.Client(api_key=Config.GEMINI_API_KEY)
    
    prompt = """TTS la siguiente conversación entre Ana y Carlos:
    Ana: Hola Carlos, ¿cómo estás?
    Carlos: ¡Muy bien Ana! ¿Y tú?
    Ana: Genial, quería preguntarte sobre los nuevos productos.
    Carlos: Claro, tenemos varias novedades interesantes."""
    
    print(f"\n🎭 Generando conversación...")
    
    response = client.models.generate_content(
        model=Config.MODEL_TTS,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
                    speaker_voice_configs=[
                        types.SpeakerVoiceConfig(
                            speaker='Ana',
                            voice_config=types.VoiceConfig(
                                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                    voice_name='Aoede',  # Voz femenina
                                )
                            )
                        ),
                        types.SpeakerVoiceConfig(
                            speaker='Carlos',
                            voice_config=types.VoiceConfig(
                                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                    voice_name='Charon',  # Voz masculina
                                )
                            )
                        ),
                    ]
                )
            )
        )
    )
    
    data = response.candidates[0].content.parts[0].inline_data.data
    filename = 'audio_conversacion.wav'
    wave_file(filename, data)
    print(f"✅ Conversación guardada: {filename}")

def test_5_mensaje_promocional():
    """Test 5: Mensaje promocional profesional"""
    print("\n" + "=" * 60)
    print("TEST 5: Mensaje Promocional")
    print("=" * 60)
    
    client = genai.Client(api_key=Config.GEMINI_API_KEY)
    
    mensaje = """
    Di de forma profesional y entusiasta:
    Estimados clientes, les informamos que por tiempo limitado
    tenemos un 50 por ciento de descuento en toda nuestra línea
    de productos. No pierdan esta oportunidad única.
    Visítenos hoy mismo. ¡Los esperamos!
    """
    
    print(f"\n📢 Generando mensaje promocional...")
    
    response = client.models.generate_content(
        model=Config.MODEL_TTS,
        contents=mensaje,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Kore',
                    )
                )
            ),
        )
    )
    
    data = response.candidates[0].content.parts[0].inline_data.data
    filename = 'audio_promo_profesional.wav'
    wave_file(filename, data)
    print(f"✅ Promoción guardada: {filename}")

def main():
    """Ejecutar todos los tests"""
    print("\n" + "=" * 60)
    print("  🧪 SUITE DE TESTS - TEXTO A VOZ (TTS)")
    print("=" * 60)
    print(f"Modelo: {Config.MODEL_TTS}")
    print(f"API Key: {'✅ Configurada' if Config.GEMINI_API_KEY else '❌ NO configurada'}")
    
    if not Config.GEMINI_API_KEY:
        print("\n❌ ERROR: Configura GEMINI_API_KEY en el archivo .env")
        return
    
    # Crear carpeta para audios
    os.makedirs('audios_generados', exist_ok=True)
    os.chdir('audios_generados')
    
    try:
        test_1_voz_simple()
        input("\nPresiona Enter para continuar...")
        
        test_2_diferentes_voces()
        input("\nPresiona Enter para continuar...")
        
        test_3_diferentes_estilos()
        input("\nPresiona Enter para continuar...")
        
        test_4_conversacion_dos_personas()
        input("\nPresiona Enter para continuar...")
        
        test_5_mensaje_promocional()
        
        print("\n" + "=" * 60)
        print("  ✅ TODOS LOS TESTS DE TTS COMPLETADOS")
        print("=" * 60)
        
        # Listar archivos generados
        print("\n🎵 Audios generados:")
        for file in os.listdir('.'):
            if file.endswith('.wav'):
                size_kb = os.path.getsize(file) / 1024
                print(f"   ✅ {file} ({size_kb:.1f} KB)")
        
        os.chdir('..')
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        os.chdir('..')

if __name__ == "__main__":
    main()
