# 🤖 Sistema de Automatización Completo con IA

## 🎯 Descripción del Proyecto

Sistema integral de automatización para gestión de redes sociales, atención al cliente y verificación de pagos usando **Gemini AI**, **Python** y **Selenium**.

### Características Principales

- ✅ **Bot de WhatsApp** con respuestas inteligentes usando Gemini 2.5 Pro
- ✅ **Verificación automática de pagos Yape** con OCR y Vision AI
- ✅ **Bot de Facebook Messenger** para atención multicanal
- ✅ **Publicación automática de estados** con contenido generado por IA
- ✅ **Generación de imágenes promocionales** con Gemini Image
- ✅ **Sistema de logging y monitoreo** completo

---

## 📚 Documentación

- 📖 **[PLAN_DESARROLLO.md](PLAN_DESARROLLO.md)** - Guía completa paso a paso del proyecto
- 📖 **[apis.md](apis.md)** - Documentación de la API de Gemini
- 🧪 **experimental/** - Ejemplos y pruebas de cada funcionalidad

---

## 🚀 Instalación Rápida

### 1. Requisitos Previos

- Python 3.8 o superior
- Git
- Google Chrome
- Tesseract OCR

### 2. Clonar Repositorio

```powershell
git clone git@github.com:Psico777/CompletaAutomatizacion.git
cd CompletaAutomatizacion
```

### 3. Crear Entorno Virtual

```powershell
python -m venv venv
.\venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
```

### 4. Instalar Dependencias

```powershell
pip install -r requirements.txt
```

### 5. Configurar Variables de Entorno

```powershell
# Copiar template de configuración
copy .env.example .env

# Editar .env y agregar tu API key de Gemini
# GEMINI_API_KEY=TU_API_KEY_AQUI
```

### 6. Instalar Tesseract OCR

**Windows:**
- Descargar desde: https://github.com/UB-Mannheim/tesseract/wiki
- Instalar en: `C:\Program Files\Tesseract-OCR\`
- Verificar: `tesseract --version`

**Linux:**
```bash
sudo apt install tesseract-ocr
```

**Mac:**
```bash
brew install tesseract
```

---

## 🧪 Probar Instalación

```powershell
# Verificar configuración
python config.py

# Probar Gemini con texto
python experimental/test_gemini_text.py
```

---

## 📁 Estructura del Proyecto

```
CompletaAutomatizacion/
├── core/                      # Módulos principales
│   ├── ai_manager.py         # Gestor de Gemini AI
│   ├── logger.py             # Sistema de logging
│   └── utils.py              # Utilidades
├── whatsapp/                  # Bot de WhatsApp
│   ├── bot.py
│   └── message_handler.py
├── facebook/                  # Bot de Facebook
│   ├── bot.py
│   └── message_handler.py
├── payment/                   # Verificación de pagos
│   ├── verifier.py
│   ├── ocr_processor.py
│   └── validators.py
├── experimental/              # Pruebas y ejemplos
│   ├── test_gemini_text.py
│   ├── test_gemini_vision.py
│   └── test_gemini_image.py
├── downloads/                 # Vouchers descargados
├── logs/                      # Archivos de log
├── config.py                  # Configuración central
├── main.py                    # Orchestador principal
└── requirements.txt           # Dependencias
```

---

## 🤖 Modelos de Gemini Utilizados

| Modelo | Uso | Características |
|--------|-----|----------------|
| **gemini-2.5-pro** | Chat con clientes | Pensamiento profundo, mejor conversación |
| **gemini-2.5-flash** | OCR y visión | Rápido, preciso para imágenes |
| **gemini-2.5-flash-lite** | Tareas simples | Ultra rápido, eficiente |
| **gemini-2.5-flash-image** | Generación de imágenes | Creación de contenido visual |
| **gemini-2.5-flash-preview-tts** | Texto a voz | 30 voces, 24 idiomas |

---

## 📖 Guía de Uso

### Experimentación (Fase 1)

Antes de usar el sistema completo, prueba cada funcionalidad:

```powershell
# Probar generación de texto
python experimental/test_gemini_text.py

# Probar visión y OCR (requiere imagen de prueba)
python experimental/test_gemini_vision.py

# Probar generación de imágenes
python experimental/test_gemini_image.py

# Probar texto a voz
python experimental/test_gemini_tts.py
```

### Bot de WhatsApp (Fase 2)

```powershell
python main.py
# Seleccionar opción 1: Iniciar Bot de WhatsApp
```

### Verificar Pago Manual

```powershell
python main.py
# Seleccionar opción 3: Verificar Voucher Manual
```

---

## ⚙️ Configuración

Edita el archivo `.env` para personalizar:

```env
# API de Gemini
GEMINI_API_KEY=TU_API_KEY_AQUI

# Modelos a usar
MODEL_CHAT=gemini-2.5-pro
MODEL_VISION=gemini-2.5-flash
MODEL_IMAGE=gemini-2.5-flash-image

# Instrucción del sistema
SYSTEM_INSTRUCTION=Eres un asistente de ventas amable...

# Temperatura (creatividad)
CHAT_TEMPERATURE=0.7

# Modo desarrollo
DEV_MODE=True
```

---

## 🔥 Roadmap del Proyecto

### ✅ Completado
- [x] Estructura del proyecto
- [x] Configuración de dependencias
- [x] Plan de desarrollo completo
- [x] Tests de experimentación con Gemini

### 🚧 En Progreso
- [ ] Bot de WhatsApp básico
- [ ] Integración con Gemini AI
- [ ] Sistema de OCR para vouchers

### 📋 Pendiente
- [ ] Bot de Facebook Messenger
- [ ] Publicación automática de estados
- [ ] Sistema de programación de tareas
- [ ] Dashboard de monitoreo
- [ ] Tests unitarios completos

---

## 📝 Desarrollo Paso a Paso

Consulta **[PLAN_DESARROLLO.md](PLAN_DESARROLLO.md)** para la guía completa con:

- ✅ Checklist detallado de cada fase
- 💻 Ejemplos de código completos
- 🎯 Objetivos de cada módulo
- 📚 Documentación de APIs
- 🐛 Troubleshooting

---

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un Pull Request

---

## 📄 Licencia

Este proyecto es privado y de uso interno.

---

## 🆘 Soporte

- 📧 Reportar issues en GitHub
- 📖 Consultar documentación en `docs/`
- 🧪 Revisar ejemplos en `experimental/`

---

## 🎓 Recursos

- [Documentación oficial de Gemini](https://ai.google.dev/gemini-api/docs)
- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [Python Tesseract](https://github.com/madmaze/pytesseract)

---

**Última actualización**: 22 de Octubre, 2025  
**Versión**: 1.0.0  
**Estado**: 🚧 En desarrollo activo

---

¡Excelente! Vamos a trazar un plan de batalla concreto y detallado. Esta es una guía paso a paso, desde la configuración inicial hasta la implementación de cada módulo, pensada para que la desarrolles usando Python y con GitHub Copilot como tu asistente de programación.

## 📚 Documentación Original

Fase 0: Preparación y Configuración del Entorno

Antes de escribir una sola línea de automatización, necesitas una base sólida.

Paso 1: Configurar el Entorno de Desarrollo

Instala Python: Asegúrate de tener Python 3.8 o superior.

Crea un Entorno Virtual: Esto es crucial para mantener las dependencias de tu proyecto aisladas.

code
Bash
download
content_copy
expand_less
python -m venv mi_proyecto_bot
source mi_proyecto_bot/bin/activate  # En Windows: mi_proyecto_bot\Scripts\activate

Instala las Bibliotecas Necesarias:

code
Bash
download
content_copy
expand_less
pip install selenium google-generativeai python-dotenv opencv-python pytesseract

Instala Tesseract OCR: pytesseract es solo un "conector". Necesitas el motor de OCR real. Busca "install Tesseract" para tu sistema operativo (Windows, macOS o Linux) y sigue las instrucciones.

Instala un WebDriver: Descarga el WebDriver correspondiente a tu navegador (ej. ChromeDriver para Google Chrome) y asegúrate de que esté en tu PATH o en la carpeta del proyecto.

Configura tu IDE y GitHub Copilot: Instala Visual Studio Code y la extensión de GitHub Copilot. Inicia sesión para activarlo.

Paso 2: Estructura del Proyecto y Credenciales Seguras

Crea una estructura de carpetas clara:

code
Code
download
content_copy
expand_less
mi_proyecto_bot/
├── main.py             # El script principal que orquesta todo
├── whatsapp_bot.py     # Lógica específica de WhatsApp
├── facebook_bot.py     # Lógica específica de Facebook
├── payment_verifier.py # Lógica para verificar pagos con OCR
├── ai_manager.py       # Interacciones con la API de Gemini
├── downloads/          # Donde se guardarán los vouchers
├── .env                # Archivo para guardar tus claves de API
└── .gitignore          # Para ignorar archivos sensibles
```2.  **Guarda tus credenciales de forma segura:** Crea un archivo `.env` y añade tu clave de la API de Gemini.

GEMINI_API_KEY="TU_API_KEY_AQUI"

code
Code
download
content_copy
expand_less
En tu código Python, usarás la biblioteca `dotenv` para cargar esta clave de forma segura.
Fase 1: Módulo de Comunicación - Bot de WhatsApp

Este es el corazón de tu operación. Nos enfocaremos en leer y responder.

Paso 3: Conexión y Control Básico con Selenium

Objetivo: Abrir WhatsApp Web y mantener la sesión activa.

En whatsapp_bot.py:

Escribe el código para iniciar Selenium, abrir Chrome y navegar a https://web.whatsapp.com.

Usa Copilot: Escribe un comentario como # python selenium function to open whatsapp web and wait for user to scan qr code y Copilot te sugerirá el código.

Añade una espera explícita (WebDriverWait) para un elemento que solo aparece cuando la sesión está iniciada (ej. el campo de búsqueda de chats). Esto asegura que tu script no continúe hasta que hayas iniciado sesión.

Paso 4: Leer Mensajes No Leídos

Objetivo: Encontrar chats con mensajes nuevos y extraer el último mensaje.

En whatsapp_bot.py:

Identificar Notificaciones: El XPath es tu mejor amigo aquí. Abre WhatsApp Web, inspecciona el elemento de un chat no leído (el que tiene un círculo verde con un número). Copia su XPath.

Usa Copilot: Pídele: # python selenium find all elements with a class name that indicates an unread chat.

Crea un bucle que periódicamente busque estos elementos.

Cuando encuentre uno, haz clic en él para abrir el chat.

Extraer el Mensaje: Identifica el XPath de los mensajes entrantes (suelen estar dentro de divs con roles o clases específicas). Extrae el texto del último mensaje.

Paso 5: Integrar IA para Generar Respuestas

Objetivo: Enviar el mensaje leído a Gemini y obtener una respuesta inteligente.

En ai_manager.py:

Crea una función, por ejemplo generar_respuesta(mensaje_cliente, historial_chat).

Usa Copilot: Escribe # python function using google-generativeai to get a response for a customer message.

Prompt Engineering: Diseña un prompt efectivo. Dile a Gemini cuál es su rol: "Eres un asistente de ventas para [Nombre de tu negocio], especialista en [tus productos]. Eres amable, directo y servicial. Un cliente ha escrito: '{mensaje_cliente}'. Responde a su pregunta."

Llama a esta función desde whatsapp_bot.py después de leer un mensaje.

Paso 6: Enviar la Respuesta

Objetivo: Escribir la respuesta de la IA en el chat y enviarla.

En whatsapp_bot.py:

Encuentra el XPath del cuadro de texto para escribir mensajes.

Usa el método .send_keys() para escribir la respuesta generada por Gemini.

Encuentra el XPath del botón de enviar y haz clic en él.

Humaniza el Bot: Usa time.sleep() con tiempos aleatorios entre acciones para evitar ser detectado.

Fase 2: Módulo de Verificación de Pagos Yape

Esta es la parte más compleja pero que te ahorrará más tiempo.

Paso 7: Detectar y Descargar Vouchers

Objetivo: Identificar cuando un mensaje contiene una imagen y guardarla.

En whatsapp_bot.py:

Modifica el detector de mensajes para que también busque etiquetas <img> dentro de los mensajes.

Cuando encuentre una imagen, obtén su URL (suele estar en el atributo src).

Descarga la imagen a tu carpeta downloads/. Pide a Copilot: # python function to download an image from a url.

Paso 8: Procesar la Imagen y Extraer Texto (OCR)

Objetivo: Convertir la imagen del voucher en texto plano.

En payment_verifier.py:

Crea una función extraer_texto_de_voucher(ruta_imagen).

Pre-procesamiento (Crucial): Usa OpenCV para leer la imagen, convertirla a escala de grises y aplicar un umbral binario para maximizar el contraste entre el texto y el fondo. Pide a Copilot: # python opencv function to preprocess an image for OCR.

OCR: Usa pytesseract.image_to_string() sobre la imagen pre-procesada para extraer todo el texto posible.

Paso 9: Validar la Información del Pago

Objetivo: Analizar el texto extraído para confirmar el pago.

En payment_verifier.py:

Usa expresiones regulares (Regex) para buscar patrones. Esto es súper poderoso.

Pide a Copilot:

# python regex to find a monetary amount like S/ 150.00

# python regex to find a date in dd/mm/yyyy format

# python regex to find a time in hh:mm pm format

Crea una función que reciba el texto y devuelva un diccionario con los datos extraídos: {'monto': 150.00, 'nombre': 'Juan Perez', 'fecha': '...'}.

Implementa tu lógica de negocio: ¿El monto es el correcto? ¿El pago es reciente?

Paso 10: Enviar Confirmación al Cliente

Objetivo: Notificar al cliente si el pago fue exitoso o no.

Llama a la función de validación desde tu bot principal.

Basado en el resultado, genera un mensaje ("¡Pago confirmado, gracias por tu compra!") o uno de error ("No pudimos verificar tu pago. Por favor, asegúrate de que la captura sea clara.").

Usa la función de envío de mensajes de la Fase 1 para enviar esta notificación.

Fase 3: Módulos Adicionales y Puesta en Producción

Paso 11: Automatizar Estados de WhatsApp

Sigue la misma lógica de Selenium:

Usa Gemini para generar una imagen o un texto promocional (ai_manager.py).

En whatsapp_bot.py, crea una función publicar_estado().

Usa Selenium para hacer clic en la pestaña "Estados".

Localiza el botón para añadir un nuevo estado y haz clic.

Manejo de la Ventana de Archivos: La subida de archivos es complicada con Selenium. Una solución robusta es usar la biblioteca pyautogui para controlar el cursor y el teclado para seleccionar el archivo y aceptar.

Paso 12: Adaptación para Facebook

Crea facebook_bot.py.

La lógica es idéntica a la de WhatsApp, pero todos los XPaths y selectores CSS serán diferentes.

El proceso es: Iniciar sesión en messenger.com, buscar notificaciones de mensajes no leídos, hacer clic, extraer texto, generar respuesta y enviarla.

Paso 13: Unificación y Robustez

En main.py, crea un menú o un sistema para decidir qué bot ejecutar.

Manejo de Errores: Envuelve cada acción riesgosa (como encontrar un elemento) en un bloque try...except. Si un XPath falla, regístralo en un log y continúa, no dejes que el script se caiga.

Logging: En lugar de print(), usa el módulo logging de Python para guardar un registro de todas las acciones en un archivo. Esto es invaluable para depurar problemas.

Este plan te llevará de cero a tener un sistema de automatización increíblemente potente. Recuerda que la clave es ir módulo por módulo y probar exhaustivamente cada paso. ¡Mucho éxito en este proyecto