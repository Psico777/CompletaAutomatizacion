"""
WhatsApp Web Connector
Módulo para conectar y gestionar la sesión de WhatsApp Web usando Selenium
"""

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

load_dotenv()

class WhatsAppConnector:
    """Gestor de conexión a WhatsApp Web"""
    
    def __init__(self, headless=False):
        """
        Inicializa el conector de WhatsApp
        
        Args:
            headless: Si True, ejecuta Chrome en modo headless (sin interfaz gráfica)
        """
        self.driver = None
        self.headless = headless
        self.timeout = int(os.getenv('WHATSAPP_QR_TIMEOUT', 60))
        
    def setup_driver(self):
        """Configura el driver de Chrome con las opciones necesarias"""
        chrome_options = Options()
        
        # Opciones para mejor rendimiento y estabilidad
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        # Mantener sesión (perfil de usuario)
        user_data_dir = os.path.join(os.getcwd(), 'whatsapp_session')
        chrome_options.add_argument(f'--user-data-dir={user_data_dir}')
        
        # Modo headless si se especifica
        if self.headless:
            chrome_options.add_argument('--headless=new')
        
        # Crear servicio con ChromeDriver automático
        service = Service(ChromeDriverManager().install())
        
        # Crear driver
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.maximize_window()
        
        print(f"[OK] Chrome Driver configurado")
        return self.driver
    
    def connect(self):
        """
        Conecta a WhatsApp Web
        
        Returns:
            bool: True si conectó exitosamente, False si falló
        """
        try:
            print("\n" + "=" * 70)
            print("   CONECTANDO A WHATSAPP WEB")
            print("=" * 70)
            
            # Configurar driver
            self.setup_driver()
            
            # Navegar a WhatsApp Web
            print("\n[*] Navegando a WhatsApp Web...")
            self.driver.get('https://web.whatsapp.com')
            
            # Esperar a que cargue
            time.sleep(3)
            
            # Verificar si ya está logueado (sesión guardada)
            if self._is_logged_in():
                print("\n[OK] Sesión activa detectada - Ya estás conectado!")
                return True
            
            # Si no está logueado, esperar escaneo de QR
            print("\n[!] ESCANEA EL CÓDIGO QR CON TU TELÉFONO")
            print(f"[!] Tienes {self.timeout} segundos...")
            
            # Esperar a que aparezca el código QR
            try:
                qr_code = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "canvas[aria-label='Scan this QR code to link a device!']"))
                )
                print("[OK] Código QR detectado")
            except:
                print("[!] No se detectó el código QR, pero continuando...")
            
            # Esperar a que se complete el login
            if self._wait_for_login():
                print("\n[OK] ¡Conectado exitosamente a WhatsApp Web!")
                return True
            else:
                print("\n[X] Timeout: No se completó el login")
                return False
                
        except Exception as e:
            print(f"\n[X] Error al conectar: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def _is_logged_in(self):
        """
        Verifica si ya hay una sesión activa
        
        Returns:
            bool: True si está logueado
        """
        try:
            # Buscar elemento que solo aparece cuando está logueado
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label='Chat list']"))
            )
            return True
        except:
            return False
    
    def _wait_for_login(self):
        """
        Espera a que se complete el login (escaneo de QR)
        
        Returns:
            bool: True si login exitoso, False si timeout
        """
        try:
            # Esperar a que aparezca la lista de chats (señal de login exitoso)
            WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label='Chat list']"))
            )
            return True
        except:
            return False
    
    def get_chats(self):
        """
        Obtiene la lista de chats disponibles
        
        Returns:
            list: Lista de elementos de chat
        """
        try:
            # Esperar a que cargue la lista de chats
            chat_list = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label='Chat list']"))
            )
            
            # Obtener todos los chats
            chats = chat_list.find_elements(By.CSS_SELECTOR, "div[role='listitem']")
            
            print(f"\n[OK] {len(chats)} chats encontrados")
            return chats
            
        except Exception as e:
            print(f"[X] Error al obtener chats: {e}")
            return []
    
    def get_unread_chats(self):
        """
        Obtiene solo los chats con mensajes no leídos
        
        Returns:
            list: Lista de chats no leídos
        """
        try:
            chats = self.get_chats()
            unread_chats = []
            
            for chat in chats:
                try:
                    # Buscar badge de mensajes no leídos
                    badge = chat.find_element(By.CSS_SELECTOR, "span[aria-label*='unread message']")
                    if badge:
                        unread_chats.append(chat)
                except:
                    continue
            
            print(f"[OK] {len(unread_chats)} chats no leídos")
            return unread_chats
            
        except Exception as e:
            print(f"[X] Error al obtener chats no leídos: {e}")
            return []
    
    def keep_alive(self):
        """Mantiene la sesión activa"""
        try:
            # Verificar que el driver sigue activo
            self.driver.current_url
            return True
        except:
            return False
    
    def disconnect(self):
        """Cierra la conexión y el navegador"""
        if self.driver:
            print("\n[*] Cerrando conexión...")
            self.driver.quit()
            print("[OK] Desconectado")

def main():
    """Función de prueba del conector"""
    print("\n" + "=" * 70)
    print("   TEST: WHATSAPP WEB CONNECTOR")
    print("=" * 70)
    
    connector = WhatsAppConnector(headless=False)
    
    try:
        # Conectar
        if not connector.connect():
            print("\n[X] No se pudo conectar")
            return False
        
        # Esperar un momento
        print("\n[*] Esperando 5 segundos...")
        time.sleep(5)
        
        # Obtener chats
        connector.get_chats()
        
        # Obtener chats no leídos
        connector.get_unread_chats()
        
        # Mantener abierto por 30 segundos para inspección
        print("\n[*] Manteniendo conexión abierta por 30 segundos...")
        print("[!] Verifica que puedas ver WhatsApp Web en el navegador")
        time.sleep(30)
        
        print("\n[OK] Test completado exitosamente")
        return True
        
    except KeyboardInterrupt:
        print("\n\n[!] Test interrumpido por usuario")
        return False
        
    except Exception as e:
        print(f"\n[X] Error en test: {e}")
        import traceback
        traceback.print_exc()
        return False
        
    finally:
        connector.disconnect()

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
