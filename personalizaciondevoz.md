# En tu script principal del bot...
import ai_manager
import local_voice_manager # ¡Importamos nuestro nuevo módulo local!
from tu_modulo_de_selenium import enviar_archivo_audio
import os
import time

# ... (lógica para leer mensaje del cliente) ...
mensaje_cliente = "hola, qué tal"

# 1. Gemini genera la respuesta en texto
texto_respuesta_ia = ai_manager.generar_respuesta(mensaje_cliente)

if texto_respuesta_ia:
    # 2. Nuestro pipeline local convierte el texto a audio CON TU VOZ
    nombre_audio = f"respuesta_local_{int(time.time())}.wav"
    ruta_del_audio = local_voice_manager.generar_audio_local_con_voz_clonada(
        texto_respuesta_ia,
        nombre_audio
    )

    if ruta_del_audio:
        # 3. Selenium/PyAutoGUI envía el archivo generado
        ruta_absoluta = os.path.abspath(ruta_del_audio)
        enviar_archivo_audio(driver, ruta_absoluta)