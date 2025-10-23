"""
Configuración central del sistema
Carga y gestiona todas las variables de entorno y configuraciones
"""

import os
from dotenv import load_dotenv
from pathlib import Path

# Cargar variables de entorno
load_dotenv()

class Config:
    """Clase de configuración central"""
    
    # ====== API KEYS ======
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')
    
    # ====== TESSERACT ======
    TESSERACT_CMD = os.getenv('TESSERACT_CMD', 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe')
    
    # ====== WHATSAPP ======
    WHATSAPP_QR_TIMEOUT = int(os.getenv('WHATSAPP_QR_TIMEOUT', '60'))
    WHATSAPP_CHECK_INTERVAL = int(os.getenv('WHATSAPP_CHECK_INTERVAL', '5'))
    
    # ====== FACEBOOK ======
    FACEBOOK_CHECK_INTERVAL = int(os.getenv('FACEBOOK_CHECK_INTERVAL', '5'))
    
    # ====== PAGOS ======
    MONTO_ESPERADO = float(os.getenv('MONTO_ESPERADO', '0.00'))
    MAX_DIAS_VOUCHER = int(os.getenv('MAX_DIAS_VOUCHER', '7'))
    
    # ====== LOGGING ======
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_MAX_SIZE_MB = int(os.getenv('LOG_MAX_SIZE_MB', '10'))
    LOG_BACKUP_COUNT = int(os.getenv('LOG_BACKUP_COUNT', '5'))
    
    # ====== MODELOS GEMINI ======
    MODEL_CHAT = os.getenv('MODEL_CHAT', 'gemini-2.5-pro')
    MODEL_VISION = os.getenv('MODEL_VISION', 'gemini-2.5-flash')
    MODEL_LITE = os.getenv('MODEL_LITE', 'gemini-2.5-flash-lite')
    MODEL_IMAGE = os.getenv('MODEL_IMAGE', 'gemini-2.5-flash-image')
    MODEL_TTS = os.getenv('MODEL_TTS', 'gemini-2.5-flash-preview-tts')
    
    # ====== TEMPERATURA ======
    CHAT_TEMPERATURE = float(os.getenv('CHAT_TEMPERATURE', '0.7'))
    
    # ====== INSTRUCCIONES DEL SISTEMA ======
    SYSTEM_INSTRUCTION = os.getenv(
        'SYSTEM_INSTRUCTION',
        'Eres un asistente de ventas amable y profesional. '
        'Respondes preguntas sobre productos, precios y envíos. '
        'Sé breve y directo. Usa emojis ocasionalmente. '
        'Si no sabes algo, pide que contacten al equipo.'
    )
    
    # ====== DELAYS ======
    MIN_DELAY = float(os.getenv('MIN_DELAY', '0.5'))
    MAX_DELAY = float(os.getenv('MAX_DELAY', '2.0'))
    
    # ====== RUTAS ======
    BASE_DIR = Path(__file__).resolve().parent
    DOWNLOADS_DIR = BASE_DIR / os.getenv('DOWNLOADS_DIR', 'downloads')
    LOGS_DIR = BASE_DIR / os.getenv('LOGS_DIR', 'logs')
    PAYMENT_HISTORY = BASE_DIR / os.getenv('PAYMENT_HISTORY', 'payment/historial_pagos.json')
    
    # ====== CHROME DRIVER ======
    CHROMEDRIVER_PATH = os.getenv('CHROMEDRIVER_PATH', '')
    
    # ====== DESARROLLO ======
    DEV_MODE = os.getenv('DEV_MODE', 'True').lower() == 'true'
    
    @classmethod
    def validate(cls):
        """Validar configuración"""
        errors = []
        
        if not cls.GEMINI_API_KEY:
            errors.append("❌ GEMINI_API_KEY no configurada en .env")
        
        if not Path(cls.TESSERACT_CMD).exists():
            errors.append(f"⚠️  Tesseract no encontrado en: {cls.TESSERACT_CMD}")
        
        # Crear directorios si no existen
        cls.DOWNLOADS_DIR.mkdir(exist_ok=True)
        cls.LOGS_DIR.mkdir(exist_ok=True)
        
        return errors
    
    @classmethod
    def print_config(cls):
        """Imprimir configuración actual"""
        print("=" * 60)
        print("  CONFIGURACIÓN DEL SISTEMA")
        print("=" * 60)
        print(f"Modo Desarrollo: {'✅ SÍ' if cls.DEV_MODE else '❌ NO'}")
        print(f"API Key Gemini: {'✅ Configurada' if cls.GEMINI_API_KEY else '❌ NO configurada'}")
        print(f"Modelo Chat: {cls.MODEL_CHAT}")
        print(f"Modelo Visión: {cls.MODEL_VISION}")
        print(f"Modelo Imagen: {cls.MODEL_IMAGE}")
        print(f"Tesseract OCR: {cls.TESSERACT_CMD}")
        print(f"Carpeta Descargas: {cls.DOWNLOADS_DIR}")
        print(f"Carpeta Logs: {cls.LOGS_DIR}")
        print("=" * 60)

# Validar configuración al importar
if __name__ == "__main__":
    Config.print_config()
    errors = Config.validate()
    if errors:
        print("\n⚠️  ADVERTENCIAS:")
        for error in errors:
            print(f"  {error}")
    else:
        print("\n✅ Configuración válida")
