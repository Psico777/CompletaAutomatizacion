api gemini : 
AIzaSyDiyBs75bDIsM7kTl36DT0mccOVFFfETiI
docmentacion de imagenes crear , voz , y etc

texto :

Generación de texto

La API de Gemini puede generar texto a partir de varias entradas, como texto, imágenes, video y audio, aprovechando los modelos de Gemini.

Este es un ejemplo básico que toma una sola entrada de texto:

Python
JavaScript
Go
Java
REST
Apps Script

from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="How does AI work?"
)
print(response.text)

Pensamiento con Gemini 2.5
Los modelos 2.5 Flash y Pro tienen la "función de pensamiento" habilitada de forma predeterminada para mejorar la calidad, lo que puede tardar más en ejecutarse y aumentar el uso de tokens.

Cuando usas Flash 2.5, puedes inhabilitar el pensamiento configurando el presupuesto de pensamiento en cero.

Para obtener más detalles, consulta la guía de pensamiento.

Python
JavaScript
Go
Java
REST
Apps Script

from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="How does AI work?",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking
    ),
)
print(response.text)
Instrucciones del sistema y otros parámetros de configuración
Puedes guiar el comportamiento de los modelos de Gemini con instrucciones del sistema. Para ello, pasa un objeto GenerateContentConfig.

Python
JavaScript
Go
Java
REST
Apps Script

from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction="You are a cat. Your name is Neko."),
    contents="Hello there"
)

print(response.text)
El objeto GenerateContentConfig también te permite anular los parámetros de generación predeterminados, como la temperatura.

Python
JavaScript
Go
Java
REST
Apps Script

from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=["Explain how AI works"],
    config=types.GenerateContentConfig(
        temperature=0.1
    )
)
print(response.text)
Consulta GenerateContentConfig en nuestra referencia de la API para obtener una lista completa de los parámetros configurables y sus descripciones.

Entradas multimodales
La API de Gemini admite entradas multimodales, lo que te permite combinar texto con archivos multimedia. En el siguiente ejemplo, se muestra cómo proporcionar una imagen:

Python
JavaScript
Go
Java
REST
Apps Script

from PIL import Image
from google import genai

client = genai.Client()

image = Image.open("/path/to/organ.png")
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[image, "Tell me about this instrument"]
)
print(response.text)
Para conocer otros métodos para proporcionar imágenes y obtener información sobre el procesamiento de imágenes más avanzado, consulta nuestra guía de comprensión de imágenes. La API también admite entradas y comprensión de documentos, videos y audios.

Respuestas de transmisión
De forma predeterminada, el modelo devuelve una respuesta solo después de que se completa todo el proceso de generación.

Para lograr interacciones más fluidas, usa la transmisión para recibir instancias de GenerateContentResponse de forma incremental a medida que se generan.

Python
JavaScript
Go
Java
REST
Apps Script

from google import genai

client = genai.Client()

response = client.models.generate_content_stream(
    model="gemini-2.5-flash",
    contents=["Explain how AI works"]
)
for chunk in response:
    print(chunk.text, end="")
Conversaciones de varios turnos (chat)
Nuestros SDKs proporcionan funciones para recopilar varias rondas de instrucciones y respuestas en un chat, lo que te brinda una forma sencilla de hacer un seguimiento del historial de conversaciones.

Nota: La funcionalidad de chat solo se implementa como parte de los SDKs. En segundo plano, sigue usando la API de generateContent. En el caso de las conversaciones de varios turnos, el historial completo de la conversación se envía al modelo con cada turno de seguimiento.
Python
JavaScript
Go
Java
REST
Apps Script

from google import genai

client = genai.Client()
chat = client.chats.create(model="gemini-2.5-flash")

response = chat.send_message("I have 2 dogs in my house.")
print(response.text)

response = chat.send_message("How many paws are in my house?")
print(response.text)

for message in chat.get_history():
    print(f'role - {message.role}',end=": ")
    print(message.parts[0].text)
La transmisión también se puede usar para conversaciones de varios turnos.

Python
JavaScript
Go
Java
REST
Apps Script

from google import genai

client = genai.Client()
chat = client.chats.create(model="gemini-2.5-flash")

response = chat.send_message_stream("I have 2 dogs in my house.")
for chunk in response:
    print(chunk.text, end="")

response = chat.send_message_stream("How many paws are in my house?")
for chunk in response:
    print(chunk.text, end="")

for message in chat.get_history():
    print(f'role - {message.role}', end=": ")
    print(message.parts[0].text)

api de imagen : 
Generación de imágenes (texto a imagen)
En el siguiente código, se muestra cómo generar una imagen a partir de una instrucción descriptiva.

Python
JavaScript
Go
REST

from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

client = genai.Client()

prompt = (
    "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"
)

response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents=[prompt],
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = Image.open(BytesIO(part.inline_data.data))
        image.save("generated_image.png")
Imagen generada por IA de un plato de nano banana
Imagen generada por IA de un plato de nano banana en un restaurante temático de Gemini
Edición de imágenes (de texto y de imagen a imagen)
Recordatorio: Asegúrate de tener los derechos necesarios de las imágenes que subas. No generes contenido que infrinja los derechos de otras personas, incluidos videos o imágenes que engañen, hostiguen o dañen. El uso de este servicio de IA generativa está sujeto a nuestra Política de Uso Prohibido.

En el siguiente ejemplo, se muestra cómo subir imágenes codificadas en Base64. Para obtener información sobre varias imágenes, cargas útiles más grandes y tipos de MIME admitidos, consulta la página Comprensión de imágenes.

Python
JavaScript
Go
REST

from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

client = genai.Client()

prompt = (
    "Create a picture of my cat eating a nano-banana in a "
    "fancy restaurant under the Gemini constellation",
)

image = Image.open("/path/to/cat_image.png")

response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents=[prompt, image],
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = Image.open(BytesIO(part.inline_data.data))
        image.save("generated_image.png")
Imagen generada por IA de un gato comiendo una banana
Imagen generada por IA de un gato comiendo un plátano nano
Otros modos de generación de imágenes
Gemini admite otros modos de interacción con imágenes según la estructura y el contexto de la instrucción, incluidos los siguientes:

Texto a imágenes y texto (intercalado): Genera imágenes con texto relacionado.
Ejemplo de instrucción: "Genera una receta ilustrada para hacer paella".
Imágenes y texto a imágenes y texto (intercalado): Usa imágenes y texto de entrada para crear imágenes y texto relacionados nuevos.
Ejemplo de instrucción: (Con una imagen de una habitación amueblada) "¿Qué otros colores de sofás funcionarían en mi espacio? ¿Puedes actualizar la imagen?".
Edición de imágenes de varios turnos (chat): Sigue generando y editando imágenes de forma conversacional.
Ejemplos de instrucciones: [Carga una imagen de un auto azul]. "Convierte este auto en un convertible", "Ahora cambia el color a amarillo".
Guía y estrategias de instrucciones
Para dominar la generación de imágenes con Gemini 2.5 Flash, primero debes comprender un principio fundamental:

Describe la escena, no solo enumere palabras clave. La principal fortaleza del modelo es su profunda comprensión del lenguaje. Un párrafo narrativo y descriptivo casi siempre producirá una imagen mejor y más coherente que una lista de palabras desconectadas.

Instrucciones para generar imágenes
Las siguientes estrategias te ayudarán a crear instrucciones eficaces para generar exactamente las imágenes que buscas.

1. Escenas fotorrealistas
Para obtener imágenes realistas, usa términos fotográficos. Menciona los ángulos de la cámara, los tipos de lentes, la iluminación y los detalles sutiles para guiar al modelo hacia un resultado fotorrealista.

Plantilla
Instrucción
Python
JavaScript
Go
REST

A photorealistic [shot type] of [subject], [action or expression], set in
[environment]. The scene is illuminated by [lighting description], creating
a [mood] atmosphere. Captured with a [camera/lens details], emphasizing
[key textures and details]. The image should be in a [aspect ratio] format.
Un primer plano fotorrealista de un ceramista japonés de edad avanzada…
Un retrato de primer plano fotorrealista de una ceramista japonesa anciana…
2. Ilustraciones y calcomanías estilizadas
Para crear calcomanías, íconos o recursos, sé explícito sobre el estilo y solicita un fondo transparente.

Plantilla
Instrucción
Python
JavaScript
Go
REST

A [style] sticker of a [subject], featuring [key characteristics] and a
[color palette]. The design should have [line style] and [shading style].
The background must be transparent.
Una calcomanía de estilo kawaii de un...
Un sticker de estilo kawaii de un panda rojo feliz…
3. Texto preciso en imágenes
Gemini se destaca en el procesamiento de texto. Sé claro sobre el texto, el estilo de la fuente (de forma descriptiva) y el diseño general.

Plantilla
Instrucción
Python
JavaScript
Go
REST

Create a [image type] for [brand/concept] with the text "[text to render]"
in a [font style]. The design should be [style description], with a
[color scheme].
Crea un logotipo moderno y minimalista para una cafetería llamada &quot;The Daily Grind&quot;…
Crea un logotipo moderno y minimalista para una cafetería llamada "The Daily Grind"…
4. Simulaciones de productos y fotografía comercial
Es ideal para crear tomas de productos limpias y profesionales para el comercio electrónico, la publicidad o la marca.

Plantilla
Instrucción
Python
JavaScript
Go
REST

A high-resolution, studio-lit product photograph of a [product description]
on a [background surface/description]. The lighting is a [lighting setup,
e.g., three-point softbox setup] to [lighting purpose]. The camera angle is
a [angle type] to showcase [specific feature]. Ultra-realistic, with sharp
focus on [key detail]. [Aspect ratio].
Una fotografía de producto de alta resolución y con iluminación de estudio de una taza de café de cerámica minimalista…
Una fotografía de alta resolución y con iluminación de estudio de una taza de café de cerámica minimalista…
5. Diseño minimalista y de espacio negativo
Es excelente para crear fondos para sitios web, presentaciones o materiales de marketing en los que se superpondrá texto.

Plantilla
Instrucción
Python
JavaScript
Go
REST

A minimalist composition featuring a single [subject] positioned in the
[bottom-right/top-left/etc.] of the frame. The background is a vast, empty
[color] canvas, creating significant negative space. Soft, subtle lighting.
[Aspect ratio].
Una composición minimalista con una sola hoja de arce rojo delicada…
Una composición minimalista con una sola hoja de arce rojo delicada…
6. Arte secuencial (panel de cómic o storyboard)
Se basa en la coherencia del personaje y la descripción de la escena para crear paneles de narración visual.

Plantilla
Instrucción
Python
JavaScript
Go
REST

A single comic book panel in a [art style] style. In the foreground,
[character description and action]. In the background, [setting details].
The panel has a [dialogue/caption box] with the text "[Text]". The lighting
creates a [mood] mood. [Aspect ratio].
Un solo panel de cómic con un estilo de arte noir y crudo…
Un solo panel de un cómic con un estilo artístico noir y crudo…
Instrucciones para editar imágenes
En estos ejemplos, se muestra cómo proporcionar imágenes junto con tus instrucciones de texto para la edición, la composición y la transferencia de estilo.

1. Cómo agregar y quitar elementos
Proporciona una imagen y describe el cambio. El modelo coincidirá con el estilo, la iluminación y la perspectiva de la imagen original.

Plantilla
Instrucción
Python
JavaScript
Go
REST

Using the provided image of [subject], please [add/remove/modify] [element]
to/from the scene. Ensure the change is [description of how the change should
integrate].
Entrada

Salida

Una imagen fotorrealista de un gato peludo de color jengibre.
Una imagen fotorrealista de un gato peludo de color jengibre…
Con la imagen de mi gato que te proporciono, agrega un pequeño sombrero de mago tejido…
Con la imagen proporcionada de mi gato, agrega un pequeño sombrero de mago tejido…
2. Reconstrucción (enmascaramiento semántico)
Define de forma conversacional una "máscara" para editar una parte específica de una imagen sin modificar el resto.

Plantilla
Instrucción
Python
JavaScript
Go
REST

Using the provided image, change only the [specific element] to [new
element/description]. Keep everything else in the image exactly the same,
preserving the original style, lighting, and composition.
Entrada

Salida

Plano general de una sala de estar moderna y bien iluminada…
Un plano general de una sala de estar moderna y bien iluminada…
Usando la imagen proporcionada de una sala de estar, cambia solo el sofá azul por un sofá Chesterfield de cuero marrón vintage…
Con la imagen proporcionada de una sala de estar, cambia solo el sofá azul por un sofá Chesterfield de cuero marrón antiguo…
3. Transferencia de estilo
Proporciona una imagen y pídele al modelo que recree su contenido con un estilo artístico diferente.

Plantilla
Instrucción
Python
JavaScript
Go
REST

Transform the provided photograph of [subject] into the artistic style of [artist/art style]. Preserve the original composition but render it with [description of stylistic elements].
Entrada

Salida

Una fotografía fotorrealista de alta resolución de una calle concurrida de la ciudad…
Una fotografía fotorrealista de alta resolución de una calle concurrida de la ciudad…
Transforma la fotografía proporcionada de una calle moderna de la ciudad por la noche…
Transforma la fotografía proporcionada de una calle moderna de la ciudad por la noche…
4. Composición avanzada: combinación de varias imágenes
Proporciona varias imágenes como contexto para crear una escena compuesta nueva. Es ideal para simulaciones de productos o collages creativos.

Plantilla
Instrucción
Python
JavaScript
Go
REST

Create a new image by combining the elements from the provided images. Take
the [element from image 1] and place it with/on the [element from image 2].
The final image should be a [description of the final scene].
Entrada 1

Entrada 2

Salida

Una foto profesional de un vestido de verano azul con flores…
Una foto profesional de un vestido de verano azul con estampado floral…
Toma de cuerpo entero de una mujer con el cabello recogido en un moño…
Toma de cuerpo completo de una mujer con el cabello recogido en un moño…
Crea una foto profesional de moda para comercio electrónico…
Crea una foto profesional de moda para comercio electrónico…
5. Conservación de detalles de alta fidelidad
Para asegurarte de que se conserven los detalles importantes (como un rostro o un logotipo) durante la edición, descríbelos con gran detalle junto con tu solicitud de edición.

Plantilla
Instrucción
Python
JavaScript
Go
REST

Using the provided images, place [element from image 2] onto [element from
image 1]. Ensure that the features of [element from image 1] remain
completely unchanged. The added element should [description of how the
element should integrate].
Entrada 1

Entrada 2

Salida

Un retrato profesional de una mujer con cabello castaño y ojos azules…
Un retrato profesional de una mujer con cabello castaño y ojos azules…
Un logotipo moderno y sencillo con las letras &quot;G&quot; y &quot;A&quot;…
Un logotipo moderno y sencillo con las letras "G" y "A"…
Toma la primera imagen de la mujer con cabello castaño, ojos azules y expresión neutra…
Toma la primera imagen de la mujer con cabello castaño, ojos azules y expresión neutra…
Prácticas recomendadas
Para mejorar tus resultados, incorpora estas estrategias profesionales en tu flujo de trabajo.

Sé hiperespecífico: Cuanto más detalles proporciones, más control tendrás. En lugar de "armadura de fantasía", descríbela: "armadura de placas élfica ornamentada, grabada con patrones de hojas de plata, con un cuello alto y hombreras con forma de alas de halcón".
Proporciona contexto y explica la intención: Explica el propósito de la imagen. La comprensión del contexto por parte del modelo influirá en el resultado final. Por ejemplo, "Crea un logotipo para una marca de cuidado de la piel minimalista y de alta gama" generará mejores resultados que solo "Crea un logotipo".
Itera y define mejor: No esperes obtener una imagen perfecta en el primer intento. Usa la naturaleza conversacional del modelo para realizar pequeños cambios. Haz un seguimiento con instrucciones como "Eso es genial, pero ¿puedes hacer que la iluminación sea un poco más cálida?" o "Mantén todo igual, pero cambia la expresión del personaje para que sea más seria".
Usa instrucciones paso a paso: Para escenas complejas con muchos elementos, divide la instrucción en pasos. "Primero, crea un fondo de un bosque sereno y brumoso al amanecer. Luego, en primer plano, agrega un antiguo altar de piedra cubierto de musgo. Por último, coloca una sola espada brillante sobre el altar".
Usa "instrucciones negativas semánticas": En lugar de decir "sin autos", describe la escena deseada de forma positiva: "una calle vacía y desierta sin señales de tráfico".
Controla la cámara: Usa el lenguaje fotográfico y cinematográfico para controlar la composición. Términos como wide-angle shot, macro shot y low-angle perspective
Limitaciones
Para obtener el mejor rendimiento, usa los siguientes idiomas: EN, es-MX, ja-JP, zh-CN y hi-IN.
La generación de imágenes no admite entradas de audio o video.
El modelo no siempre seguirá la cantidad exacta de imágenes que el usuario solicite explícitamente.
El modelo funciona mejor con hasta 3 imágenes como entrada.
Cuando generas texto para una imagen, Gemini funciona mejor si primero generas el texto y, luego, pides una imagen con el texto.
Por el momento, no se pueden subir imágenes de niños en el EEE, Suiza ni el Reino Unido.
Todas las imágenes generadas incluyen una marca de agua de SynthID.
Configuración opcional
De manera opcional, puedes configurar las modalidades de respuesta y la relación de aspecto del resultado del modelo en el campo config de las llamadas a generate_content.

Tipos de salida
De forma predeterminada, el modelo devuelve respuestas de texto y de imagen (es decir, response_modalities=['Text', 'Image']). Puedes configurar la respuesta para que solo devuelva imágenes sin texto con response_modalities=['Image'].

Python
JavaScript
Go
REST

response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents=[prompt],
    config=types.GenerateContentConfig(
        response_modalities=['Image']
    )
)
Relaciones de aspecto
De forma predeterminada, el modelo hace coincidir el tamaño de la imagen de salida con el de la imagen de entrada o, de lo contrario, genera cuadrados 1:1. Puedes controlar la relación de aspecto de la imagen de salida con el campo aspect_ratio en image_config en la solicitud de respuesta, como se muestra aquí:

Python
JavaScript
Go
REST

response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents=[prompt],
    config=types.GenerateContentConfig(
        image_config=types.ImageConfig(
            aspect_ratio="16:9",
        )
    )
)
En esta tabla, se indican las diferentes proporciones disponibles y el tamaño de la imagen generada:

Relación de aspecto	Solución	Tokens
1:1	1024x1024	1290
2:3	832 x 1248	1290
3:2	1248 × 832	1290
3:4	864 x 1184	1290
4:3	1184 x 864	1290
4:5	896 × 1,152	1290
5:4	1152 × 896	1290
9:16	768 × 1,344	1290
16:9	1344 x 768	1290
21:9	1536 x 672	1290

api documentos : 

Cómo pasar datos de PDF intercalados
Puedes pasar datos de PDF intercalados en la solicitud a generateContent. En el caso de las cargas útiles en PDF de menos de 20 MB, puedes elegir entre subir documentos codificados en base64 o subir directamente archivos almacenados de forma local.

En el siguiente ejemplo, se muestra cómo recuperar un PDF de una URL y convertirlo en bytes para su procesamiento:

Python
JavaScript
Go
REST

from google import genai
from google.genai import types
import httpx

client = genai.Client()

doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"

# Retrieve and encode the PDF byte
doc_data = httpx.get(doc_url).content

prompt = "Summarize this document"
response = client.models.generate_content(
  model="gemini-2.5-flash",
  contents=[
      types.Part.from_bytes(
        data=doc_data,
        mime_type='application/pdf',
      ),
      prompt])
print(response.text)
También puedes leer un PDF desde un archivo local para su procesamiento:

Python
JavaScript
Go

from google import genai
from google.genai import types
import pathlib

client = genai.Client()

# Retrieve and encode the PDF byte
filepath = pathlib.Path('file.pdf')

prompt = "Summarize this document"
response = client.models.generate_content(
  model="gemini-2.5-flash",
  contents=[
      types.Part.from_bytes(
        data=filepath.read_bytes(),
        mime_type='application/pdf',
      ),
      prompt])
print(response.text)
Cómo subir archivos PDF con la API de File
Puedes usar la API de File para subir documentos más grandes. Siempre usa la API de File cuando el tamaño total de la solicitud (incluidos los archivos, la instrucción de texto, las instrucciones del sistema, etcétera) sea superior a 20 MB.

Nota: La API de File te permite almacenar hasta 50 MB de archivos PDF. Los archivos se almacenan durante 48 horas. Puedes acceder a ellos durante ese período con tu clave de API, pero no puedes descargarlos desde la API. La API de File está disponible sin costo en todas las regiones en las que está disponible la API de Gemini.
Llama a media.upload para subir un archivo con la API de File. El siguiente código sube un archivo de documento y, luego, lo usa en una llamada a models.generateContent.

Archivos PDF grandes desde URLs
Usa la API de File para simplificar la carga y el procesamiento de archivos PDF grandes desde URLs:

Python
JavaScript
Go
REST

from google import genai
from google.genai import types
import io
import httpx

client = genai.Client()

long_context_pdf_path = "https://www.nasa.gov/wp-content/uploads/static/history/alsj/a17/A17_FlightPlan.pdf"

# Retrieve and upload the PDF using the File API
doc_io = io.BytesIO(httpx.get(long_context_pdf_path).content)

sample_doc = client.files.upload(
  # You can pass a path or a file-like object here
  file=doc_io,
  config=dict(
    mime_type='application/pdf')
)

prompt = "Summarize this document"

response = client.models.generate_content(
  model="gemini-2.5-flash",
  contents=[sample_doc, prompt])
print(response.text)
PDFs grandes almacenados de forma local
Python
JavaScript
Go
REST

from google import genai
from google.genai import types
import pathlib
import httpx

client = genai.Client()

# Retrieve and encode the PDF byte
file_path = pathlib.Path('large_file.pdf')

# Upload the PDF using the File API
sample_file = client.files.upload(
  file=file_path,
)

prompt="Summarize this document"

response = client.models.generate_content(
  model="gemini-2.5-flash",
  contents=[sample_file, "Summarize this document"])
print(response.text)
Puedes verificar que la API haya almacenado correctamente el archivo subido y obtener sus metadatos llamando a files.get. Solo el name (y, por extensión, el uri) son únicos.

Python
REST

from google import genai
import pathlib

client = genai.Client()

fpath = pathlib.Path('example.txt')
fpath.write_text('hello')

file = client.files.upload(file='example.txt')

file_info = client.files.get(name=file.name)
print(file_info.model_dump_json(indent=4))
Cómo pasar varios PDFs
La API de Gemini puede procesar varios documentos PDF (hasta 1,000 páginas) en una sola solicitud, siempre que el tamaño combinado de los documentos y la instrucción de texto permanezca dentro de la ventana de contexto del modelo.

Python
JavaScript
Go
REST

from google import genai
import io
import httpx

client = genai.Client()

doc_url_1 = "https://arxiv.org/pdf/2312.11805"
doc_url_2 = "https://arxiv.org/pdf/2403.05530"

# Retrieve and upload both PDFs using the File API
doc_data_1 = io.BytesIO(httpx.get(doc_url_1).content)
doc_data_2 = io.BytesIO(httpx.get(doc_url_2).content)

sample_pdf_1 = client.files.upload(
  file=doc_data_1,
  config=dict(mime_type='application/pdf')
)
sample_pdf_2 = client.files.upload(
  file=doc_data_2,
  config=dict(mime_type='application/pdf')
)

prompt = "What is the difference between each of the main benchmarks between these two papers? Output these in a table."

response = client.models.generate_content(
  model="gemini-2.5-flash",
  contents=[sample_pdf_1, sample_pdf_2, prompt])
print(response.text)

Generación de voz (texto a voz)

La API de Gemini puede transformar la entrada de texto en audio de un solo orador o varios oradores con capacidades nativas de generación de texto a voz (TTS). La generación de texto a voz (TTS) es controlable, lo que significa que puedes usar el lenguaje natural para estructurar las interacciones y guiar el estilo, el acento, el ritmo y el tono del audio.

La capacidad de TTS difiere de la generación de voz que se proporciona a través de la API en vivo, que está diseñada para audio interactivo y no estructurado, y entradas y salidas multimodales. Si bien la API de Live se destaca en contextos conversacionales dinámicos, la API de Gemini ofrece TTS diseñado para situaciones que requieren una recitación de texto exacta con un control detallado sobre el estilo y el sonido, como la generación de podcasts o audiolibros.

En esta guía, se muestra cómo generar audio de un solo interlocutor y de varios interlocutores a partir de texto.

Vista previa: La función de texto a voz (TTS) nativa está en vista previa.
Antes de comenzar
Asegúrate de usar una variante del modelo Gemini 2.5 con capacidades nativas de texto a voz (TTS), como se indica en la sección Modelos compatibles. Para obtener resultados óptimos, considera qué modelo se adapta mejor a tu caso de uso específico.

Antes de comenzar a compilar, te recomendamos que pruebes los modelos de TTS de Gemini 2.5 en AI Studio.

Nota: Los modelos de TTS aceptan entradas solo de texto y producen salidas solo de audio. Para obtener una lista completa de las restricciones específicas de los modelos de TTS, consulta la sección Limitaciones.
Texto a voz con un solo interlocutor
Para convertir texto en audio de un solo orador, establece la modalidad de respuesta en "audio" y pasa un objeto SpeechConfig con VoiceConfig establecido. Deberás elegir un nombre de voz de las voces de salida prediseñadas.

En este ejemplo, se guarda el audio de salida del modelo en un archivo wave:

Python
JavaScript
REST

from google import genai
from google.genai import types
import wave

# Set up the wave file to save the output:
def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)

client = genai.Client()

response = client.models.generate_content(
   model="gemini-2.5-flash-preview-tts",
   contents="Say cheerfully: Have a wonderful day!",
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

file_name='out.wav'
wave_file(file_name, data) # Saves the file to current directory
Para obtener más muestras de código, consulta el archivo "TTS - Get Started" en el repositorio de recetas:

Ver en GitHub

Texto a voz con varios oradores
Para el audio con varios oradores, necesitarás un objeto MultiSpeakerVoiceConfig con cada orador (hasta 2) configurado como un SpeakerVoiceConfig. Deberás definir cada speaker con los mismos nombres que se usan en la instrucción:

Python
JavaScript
REST

from google import genai
from google.genai import types
import wave

# Set up the wave file to save the output:
def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)

client = genai.Client()

prompt = """TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?"""

response = client.models.generate_content(
   model="gemini-2.5-flash-preview-tts",
   contents=prompt,
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
            speaker_voice_configs=[
               types.SpeakerVoiceConfig(
                  speaker='Joe',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Kore',
                     )
                  )
               ),
               types.SpeakerVoiceConfig(
                  speaker='Jane',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Puck',
                     )
                  )
               ),
            ]
         )
      )
   )
)

data = response.candidates[0].content.parts[0].inline_data.data

file_name='out.wav'
wave_file(file_name, data) # Saves the file to current directory
Cómo controlar el estilo de voz con instrucciones
Puedes controlar el estilo, el tono, el acento y el ritmo con instrucciones en lenguaje natural para la función de TTS de un solo orador y de varios oradores. Por ejemplo, en una instrucción de un solo orador, puedes decir lo siguiente:


Say in an spooky whisper:
"By the pricking of my thumbs...
Something wicked this way comes"
En una instrucción con varios oradores, proporciona al modelo el nombre de cada orador y la transcripción correspondiente. También puedes proporcionar orientación para cada orador de forma individual:


Make Speaker1 sound tired and bored, and Speaker2 sound excited and happy:

Speaker1: So... what's on the agenda today?
Speaker2: You're never going to guess!
Intenta usar una opción de voz que corresponda al estilo o la emoción que quieres transmitir para enfatizarlo aún más. En la instrucción anterior, por ejemplo, la respiración de Encélado podría enfatizar "cansado" y "aburrido", mientras que el tono alegre de Puck podría complementar "emocionado" y "feliz".

Generar una instrucción para convertirla en audio
Los modelos de TTS solo generan audio, pero puedes usar otros modelos para generar primero una transcripción y, luego, pasarla al modelo de TTS para que la lea en voz alta.

Python
JavaScript

from google import genai
from google.genai import types

client = genai.Client()

transcript = client.models.generate_content(
   model="gemini-2.0-flash",
   contents="""Generate a short transcript around 100 words that reads
            like it was clipped from a podcast by excited herpetologists.
            The hosts names are Dr. Anya and Liam.""").text

response = client.models.generate_content(
   model="gemini-2.5-flash-preview-tts",
   contents=transcript,
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
            speaker_voice_configs=[
               types.SpeakerVoiceConfig(
                  speaker='Dr. Anya',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Kore',
                     )
                  )
               ),
               types.SpeakerVoiceConfig(
                  speaker='Liam',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Puck',
                     )
                  )
               ),
            ]
         )
      )
   )
)

# ...Code to stream or save the output
Opciones de voz
Los modelos de TTS admiten las siguientes 30 opciones de voz en el campo voice_name:

Zephyr: Brillante	Puck: Optimista	Charon: Informativa
Kore, Firme	Fenrir: Excitabilidad	Leda: Juvenil
Orus, Firme	Aoede: Breezy	Callirrhoe: Voz tranquila
Autonoe: Brillo	Enceladus: Respiración	Iapetus: Claro
Umbriel: Relajado	Algieba: Suave	Despina: Suave
Erinome: Despejado	Algenib: Arenoso	Rasalgethi: Informativa
Laomedeia: Optimista	Achernar: Suave	Alnilam: Firme
Schedar: Par	Gacrux: Contenido para mayores	Pulcherrima: Hacia adelante
Achird: Amistoso	Zubenelgenubi: Casual	Vindemiatrix: Suave
Sadachbia: Animada	Sadaltager: Conocimiento	Sulafat: Cálida
Puedes escuchar todas las opciones de voz en AI Studio.

Idiomas admitidos
Los modelos de TTS detectan automáticamente el idioma de entrada. Admiten los siguientes 24 idiomas:

Idioma	Código BCP-47	Idioma	Código BCP-47
Árabe (Egipto)	ar-EG	Alemán (Alemania)	de-DE
Inglés (EE.UU.)	en-US	Español (EE.UU.)	es-US
Francés (Francia)	fr-FR	Hindi (India)	hi-IN
Indonesio (Indonesia)	id-ID	Italiano (Italia)	it-IT
Japonés (Japón)	ja-JP	Coreano (Corea)	ko-KR
Portugués (Brasil)	pt-BR	Ruso (Rusia)	ru-RU
Neerlandés (Países Bajos)	nl-NL	Polaco (Polonia)	pl-PL
Tailandés (Tailandia)	th-TH	Turco (Türkiye)	tr-TR
Vietnamita (Vietnam)	vi-VN	Rumano (Rumania)	ro-RO
Ucraniano (Ucrania)	uk-UA	Bengalí (Bangladés)	bn-BD
Inglés (India)	Paquete de en-IN y hi-IN	Maratí (India)	mr-IN
Tamil (India)	ta-IN	Telugu (India)	te-IN
Modelos compatibles
Modelo	Interlocutor único	Varios oradores
Gemini 2.5 Flash Preview TTS	✔️	✔️
TTS de la versión preliminar de Gemini 2.5 Pro	✔️	✔️
Limitaciones
Los modelos de TTS solo pueden recibir entradas de texto y generar salidas de audio.
Una sesión de TTS tiene un límite de ventana de contexto de 32,000 tokens.
Revisa la sección Idiomas para conocer los idiomas admitidos.

Comprensión de audio

Gemini puede analizar y comprender la entrada de audio, lo que permite casos de uso como los siguientes:

Describir, resumir o responder preguntas sobre el contenido de audio
Proporciona una transcripción del audio.
Analiza segmentos específicos del audio.
En esta guía, se muestra cómo usar la API de Gemini para generar una respuesta de texto a la entrada de audio.

Antes de comenzar
Antes de llamar a la API de Gemini, asegúrate de tener instalado el SDK que elijas y de que una clave de API de Gemini esté configurada y lista para usar.

Audio de entrada
Puedes proporcionar datos de audio a Gemini de las siguientes maneras:

Sube un archivo de audio antes de realizar una solicitud a generateContent.
Pasa datos de audio intercalados con la solicitud a generateContent.
Sube un archivo de audio
Puedes usar la API de Files para subir un archivo de audio. Usa siempre la API de Files cuando el tamaño total de la solicitud (incluidos los archivos, el mensaje de texto, las instrucciones del sistema, etcétera) sea superior a 20 MB.

El siguiente código sube un archivo de audio y, luego, lo usa en una llamada a generateContent.

Python
JavaScript
Go
REST

from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp3")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents=["Describe this audio clip", myfile]
)

print(response.text)
Para obtener más información sobre cómo trabajar con archivos multimedia, consulta la API de Files.

Pasa datos de audio intercalados
En lugar de subir un archivo de audio, puedes pasar datos de audio intercalados en la solicitud a generateContent:

Python
JavaScript
Go

from google import genai
from google.genai import types

with open('path/to/small-sample.mp3', 'rb') as f:
    audio_bytes = f.read()

client = genai.Client()
response = client.models.generate_content(
  model='gemini-2.5-flash',
  contents=[
    'Describe this audio clip',
    types.Part.from_bytes(
      data=audio_bytes,
      mime_type='audio/mp3',
    )
  ]
)

print(response.text)
Ten en cuenta lo siguiente sobre los datos de audio intercalados:

El tamaño máximo de la solicitud es de 20 MB, lo que incluye instrucciones de texto, instrucciones del sistema y archivos proporcionados intercalados. Si el tamaño de tu archivo hará que el tamaño total de la solicitud supere los 20 MB, usa la API de Files para subir un archivo de audio que se usará en la solicitud.
Si usas un sample de audio varias veces, es más eficiente subir un archivo de audio.
Cómo obtener una transcripción
Para obtener una transcripción de los datos de audio, simplemente solicítala en la instrucción:

Python
JavaScript
Go

from google import genai

client = genai.Client()
myfile = client.files.upload(file='path/to/sample.mp3')
prompt = 'Generate a transcript of the speech.'

response = client.models.generate_content(
  model='gemini-2.5-flash',
  contents=[prompt, myfile]
)

print(response.text)
Consulta las marcas de tiempo
Puedes hacer referencia a secciones específicas de un archivo de audio con marcas de tiempo del formato MM:SS. Por ejemplo, la siguiente instrucción solicita una transcripción que

Comienza a los 2 minutos y 30 segundos desde el principio del archivo.
Finaliza a los 3 minutos y 29 segundos desde el principio del archivo.

Python
JavaScript
Go

# Create a prompt containing timestamps.
prompt = "Provide a transcript of the speech from 02:30 to 03:29."
Cuenta tokens
Llama al método countTokens para obtener un recuento de la cantidad de tokens en un archivo de audio. Por ejemplo:

Python
JavaScript
Go

from google import genai

client = genai.Client()
response = client.models.count_tokens(
  model='gemini-2.5-flash',
  contents=[myfile]
)

print(response)
Formatos de audio compatibles
Gemini admite los siguientes tipos de MIME de formato de audio:

WAV - audio/wav
MP3 - audio/mp3
AIFF: audio/aiff
AAC - audio/aac
OGG Vorbis: audio/ogg
FLAC - audio/flac
Detalles técnicos sobre el audio
Gemini representa cada segundo de audio como 32 tokens. Por ejemplo, un minuto de audio se representa como 1,920 tokens.
Gemini puede “entender” componentes que no son de voz, como cantos de pájaros o sirenas.
La duración máxima admitida de los datos de audio en una sola instrucción es de 9.5 horas. Gemini no limita la cantidad de archivos de audio en una sola instrucción. Sin embargo, la duración total combinada de todos los archivos de audio en una sola instrucción no puede exceder las 9.5 horas.
Gemini reduce la muestra de los archivos de audio a una resolución de datos de 16 Kbps.
Si la fuente de audio contiene varios canales, Gemini los combina en uno solo.

Comprensión de imágenes

Los modelos de Gemini se crearon para ser multimodales desde cero, lo que permite realizar una amplia variedad de tareas de procesamiento de imágenes y visión artificial, como la creación de leyendas de imágenes, la clasificación y la búsqueda de respuestas visuales, sin tener que entrenar modelos de AA especializados.

Nota: Además de sus capacidades multimodales generales, los modelos de Gemini (2.0 y versiones posteriores) ofrecen una mayor precisión para casos de uso específicos, como la detección de objetos y la segmentación, a través de entrenamiento adicional. Consulta la sección Funciones para obtener más detalles.
Cómo pasar imágenes a Gemini
Puedes proporcionar imágenes como entrada a Gemini de dos maneras:

Paso de datos de imágenes intercaladas: Ideal para archivos más pequeños (tamaño total de la solicitud inferior a 20 MB, incluidas las instrucciones).
Cómo subir imágenes con la API de File: Se recomienda para archivos más grandes o para reutilizar imágenes en varias solicitudes.
Cómo pasar datos de imágenes intercaladas
Puedes pasar datos de imágenes intercaladas en la solicitud a generateContent. Puedes proporcionar datos de imagen como cadenas codificadas en Base64 o leyendo archivos locales directamente (según el lenguaje).

En el siguiente ejemplo, se muestra cómo leer una imagen de un archivo local y pasarla a la API de generateContent para su procesamiento.

Python
JavaScript
Go
REST

  from google.genai import types

  with open('path/to/small-sample.jpg', 'rb') as f:
      image_bytes = f.read()

  response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[
      types.Part.from_bytes(
        data=image_bytes,
        mime_type='image/jpeg',
      ),
      'Caption this image.'
    ]
  )

  print(response.text)
También puedes recuperar una imagen de una URL, convertirla en bytes y pasarla a generateContent, como se muestra en los siguientes ejemplos.

Python
JavaScript
Go
REST

from google import genai
from google.genai import types

import requests

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(
  data=image_bytes, mime_type="image/jpeg"
)

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=["What is this image?", image],
)

print(response.text)
Nota: Los datos de imágenes intercaladas limitan el tamaño total de la solicitud (instrucciones de texto, instrucciones del sistema y bytes intercalados) a 20 MB. Para solicitudes más grandes, sube archivos de imagen con la API de File. La API de Files también es más eficiente para las situaciones en las que se usa la misma imagen varias veces.
Cómo subir imágenes con la API de File
Para archivos grandes o para poder usar el mismo archivo de imagen varias veces, usa la API de Files. El siguiente código sube un archivo de imagen y, luego, lo usa en una llamada a generateContent. Consulta la guía de la API de Files para obtener más información y ejemplos.

Python
JavaScript
Go
REST

from google import genai

client = genai.Client()

my_file = client.files.upload(file="path/to/sample.jpg")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[my_file, "Caption this image."],
)

print(response.text)
Instrucciones con varias imágenes
Puedes proporcionar varias imágenes en una sola instrucción incluyendo varios objetos Part de imagen en el array contents. Pueden ser una combinación de datos intercalados (archivos locales o URLs) y referencias a la API de File.

Python
JavaScript
Go
REST

from google import genai
from google.genai import types

client = genai.Client()

# Upload the first image
image1_path = "path/to/image1.jpg"
uploaded_file = client.files.upload(file=image1_path)

# Prepare the second image as inline data
image2_path = "path/to/image2.png"
with open(image2_path, 'rb') as f:
    img2_bytes = f.read()

# Create the prompt with text and multiple images
response = client.models.generate_content(

    model="gemini-2.5-flash",
    contents=[
        "What is different between these two images?",
        uploaded_file,  # Use the uploaded file reference
        types.Part.from_bytes(
            data=img2_bytes,
            mime_type='image/png'
        )
    ]
)

print(response.text)
Detección de objetos
A partir de Gemini 2.0, los modelos se entrenan aún más para detectar objetos en una imagen y obtener las coordenadas de sus cuadros delimitadores. Las coordenadas, relativas a las dimensiones de la imagen, se ajustan a una escala de [0, 1000]. Debes ajustar estas coordenadas según el tamaño de tu imagen original.

Python

from google import genai
from google.genai import types
from PIL import Image
import json

client = genai.Client()
prompt = "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000."

image = Image.open("/path/to/image.png")

config = types.GenerateContentConfig(
  response_mime_type="application/json"
  )

response = client.models.generate_content(model="gemini-2.5-flash",
                                          contents=[image, prompt],
                                          config=config
                                          )

width, height = image.size
bounding_boxes = json.loads(response.text)

converted_bounding_boxes = []
for bounding_box in bounding_boxes:
    abs_y1 = int(bounding_box["box_2d"][0]/1000 * height)
    abs_x1 = int(bounding_box["box_2d"][1]/1000 * width)
    abs_y2 = int(bounding_box["box_2d"][2]/1000 * height)
    abs_x2 = int(bounding_box["box_2d"][3]/1000 * width)
    converted_bounding_boxes.append([abs_x1, abs_y1, abs_x2, abs_y2])

print("Image size: ", width, height)
print("Bounding boxes:", converted_bounding_boxes)

Nota: El modelo también admite la generación de cuadros de límite basados en instrucciones personalizadas, como "Muestra los cuadros de límite de todos los objetos verdes en esta imagen". También admite etiquetas personalizadas, como "etiqueta los artículos con los alérgenos que pueden contener".
Para obtener más ejemplos, consulta los siguientes notebooks en la guía de soluciones de Gemini:

Notebook de comprensión espacial 2D
Notebook experimental de apuntado en 3D
Segmentación
A partir de Gemini 2.5, los modelos no solo detectan elementos, sino que también los segmentan y proporcionan sus máscaras de contorno.

El modelo predice una lista JSON, en la que cada elemento representa una máscara de segmentación. Cada elemento tiene un cuadro de límite (“box_2d”) en el formato [y0, x0, y1, x1] con coordenadas normalizadas entre 0 y 1,000, una etiqueta (“label”) que identifica el objeto y, por último, la máscara de segmentación dentro del cuadro de límite, como un PNG codificado en base64 que es un mapa de probabilidad con valores entre 0 y 255. La máscara debe cambiar de tamaño para que coincida con las dimensiones del cuadro delimitador y, luego, se debe binarizar en el umbral de confianza (127 para el punto medio).

Nota: Para obtener mejores resultados, inhabilita la función de pensamiento estableciendo el presupuesto de pensamiento en 0. Consulta el siguiente ejemplo de código.
Python

from google import genai
from google.genai import types
from PIL import Image, ImageDraw
import io
import base64
import json
import numpy as np
import os

client = genai.Client()

def parse_json(json_output: str):
  # Parsing out the markdown fencing
  lines = json_output.splitlines()
  for i, line in enumerate(lines):
    if line == "```json":
      json_output = "\n".join(lines[i+1:])  # Remove everything before "```json"
      output = json_output.split("```")[0]  # Remove everything after the closing "```"
      break  # Exit the loop once "```json" is found
  return json_output

def extract_segmentation_masks(image_path: str, output_dir: str = "segmentation_outputs"):
  # Load and resize image
  im = Image.open(image_path)
  im.thumbnail([1024, 1024], Image.Resampling.LANCZOS)

  prompt = """
  Give the segmentation masks for the wooden and glass items.
  Output a JSON list of segmentation masks where each entry contains the 2D
  bounding box in the key "box_2d", the segmentation mask in key "mask", and
  the text label in the key "label". Use descriptive labels.
  """

  config = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(thinking_budget=0) # set thinking_budget to 0 for better results in object detection
  )

  response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[prompt, im], # Pillow images can be directly passed as inputs (which will be converted by the SDK)
    config=config
  )

  # Parse JSON response
  items = json.loads(parse_json(response.text))

  # Create output directory
  os.makedirs(output_dir, exist_ok=True)

  # Process each mask
  for i, item in enumerate(items):
      # Get bounding box coordinates
      box = item["box_2d"]
      y0 = int(box[0] / 1000 * im.size[1])
      x0 = int(box[1] / 1000 * im.size[0])
      y1 = int(box[2] / 1000 * im.size[1])
      x1 = int(box[3] / 1000 * im.size[0])

      # Skip invalid boxes
      if y0 >= y1 or x0 >= x1:
          continue

      # Process mask
      png_str = item["mask"]
      if not png_str.startswith("data:image/png;base64,"):
          continue

      # Remove prefix
      png_str = png_str.removeprefix("data:image/png;base64,")
      mask_data = base64.b64decode(png_str)
      mask = Image.open(io.BytesIO(mask_data))

      # Resize mask to match bounding box
      mask = mask.resize((x1 - x0, y1 - y0), Image.Resampling.BILINEAR)

      # Convert mask to numpy array for processing
      mask_array = np.array(mask)

      # Create overlay for this mask
      overlay = Image.new('RGBA', im.size, (0, 0, 0, 0))
      overlay_draw = ImageDraw.Draw(overlay)

      # Create overlay for the mask
      color = (255, 255, 255, 200)
      for y in range(y0, y1):
          for x in range(x0, x1):
              if mask_array[y - y0, x - x0] > 128:  # Threshold for mask
                  overlay_draw.point((x, y), fill=color)

      # Save individual mask and its overlay
      mask_filename = f"{item['label']}_{i}_mask.png"
      overlay_filename = f"{item['label']}_{i}_overlay.png"

      mask.save(os.path.join(output_dir, mask_filename))

      # Create and save overlay
      composite = Image.alpha_composite(im.convert('RGBA'), overlay)
      composite.save(os.path.join(output_dir, overlay_filename))
      print(f"Saved mask and overlay for {item['label']} to {output_dir}")

# Example usage
if __name__ == "__main__":
  extract_segmentation_masks("path/to/image.png")

Consulta el ejemplo de segmentación en la guía de recetas para ver un ejemplo más detallado.

Una mesa con cupcakes, con los objetos de madera y vidrio destacados
Un ejemplo de resultado de segmentación con objetos y máscaras de segmentación
Formatos de imagen compatibles
Gemini admite los siguientes tipos de MIME de formato de imagen:

PNG - image/png
JPEG - image/jpeg
WEBP - image/webp
HEIC: image/heic
HEIF - image/heif
Funciones
Todas las versiones del modelo de Gemini son multimodales y se pueden utilizar en una amplia variedad de tareas de procesamiento de imágenes y visión artificial, como el subtitulado de imágenes, la búsqueda de respuestas visuales, la clasificación de imágenes, la detección de objetos y la segmentación.

Gemini puede reducir la necesidad de usar modelos de AA especializados según tus requisitos de calidad y rendimiento.

Algunas versiones posteriores del modelo se entrenan específicamente para mejorar la precisión de las tareas especializadas, además de las capacidades genéricas:

Los modelos de Gemini 2.0 se entrenan aún más para admitir la detección de objetos mejorada.

Los modelos de Gemini 2.5 se entrenan aún más para admitir una segmentación mejorada, además de la detección de objetos.

Limitaciones e información técnica clave
Límite de archivos
Gemini 2.5 Pro/Flash, 2.0 Flash, 1.5 Pro y 1.5 Flash admiten un máximo de 3,600 archivos de imagen por solicitud.

Cálculo de tokens
Gemini 1.5 Flash y Gemini 1.5 Pro: 258 tokens si ambas dimensiones son menores o iguales a 384 píxeles Las imágenes más grandes se dividen en mosaicos (mín. 256 px, máx. 768 px, cambio de tamaño a 768 x 768), y cada mosaico cuesta 258 tokens.
Gemini 2.0 Flash y Gemini 2.5 Flash/Pro: 258 tokens si ambas dimensiones son menores o iguales a 384 píxeles Las imágenes más grandes se dividen en mosaicos de 768 x 768 píxeles, y cada uno cuesta 258 tokens.
La siguiente es una fórmula aproximada para calcular la cantidad de mosaicos:

Calcula el tamaño de la unidad de recorte, que es aproximadamente floor(min(ancho, alto) / 1.5).
Divide cada dimensión por el tamaño de la unidad de recorte y multiplícalas para obtener la cantidad de mosaicos.
Por ejemplo, una imagen de 960 x 540 tendría un tamaño de unidad de recorte de 360. Divide cada dimensión por 360, y la cantidad de mosaicos es 3 * 2 = 6.

Sugerencias y prácticas recomendadas
Verifica que las imágenes se roten correctamente.
Usa imágenes claras y no borrosas.
Cuando uses una sola imagen con texto, coloca la instrucción de texto después de la parte de la imagen en el array contents.
¿Qué sigue?
En esta guía, se muestra cómo subir archivos de imagen y generar resultados de texto a partir de entradas de imágenes. Para obtener más información, consulta los siguientes recursos:

API de Files: Obtén más información para subir y administrar archivos para usarlos con Gemini.
Instrucciones del sistema: Las instrucciones del sistema te permiten dirigir el comportamiento del modelo según tus necesidades y casos de uso específicos.
Estrategias de instrucciones con archivos: La API de Gemini admite instrucciones con datos de texto, imagen, audio y video, también conocidas como instrucciones multimodales.
Orientación sobre seguridad: A veces, los modelos de IA generativa producen resultados inesperados, como resultados inexactos, sesgados u ofensivos. El procesamiento posterior y la evaluación humana son fundamentales para limitar el riesgo de daño que pueden causar estos resultados.

Resultados estructurados

Puedes configurar Gemini para que genere resultados estructurados en lugar de texto no estructurado, lo que permite extraer y estandarizar información con precisión para su posterior procesamiento. Por ejemplo, puedes usar la salida estructurada para extraer información de currículums vitae y estandarizarlos para crear una base de datos estructurada.

Gemini puede generar JSON o valores de enumeración como resultado estructurado.

Cómo generar JSON
Para restringir el modelo a generar JSON, configura un responseSchema. Luego, el modelo responderá a cualquier instrucción con un resultado en formato JSON.

Python
JavaScript
Go
REST

from google import genai
from pydantic import BaseModel

class Recipe(BaseModel):
    recipe_name: str
    ingredients: list[str]

client = genai.Client()
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="List a few popular cookie recipes, and include the amounts of ingredients.",
    config={
        "response_mime_type": "application/json",
        "response_schema": list[Recipe],
    },
)
# Use the response as a JSON string.
print(response.text)

# Use instantiated objects.
my_recipes: list[Recipe] = response.parsed
Nota: Aún no se admiten los validadores de Pydantic. Si se produce un pydantic.ValidationError, se suprime y .parsed puede estar vacío o ser nulo.
El resultado podría verse de la siguiente manera:


[
  {
    "recipeName": "Chocolate Chip Cookies",
    "ingredients": [
      "1 cup (2 sticks) unsalted butter, softened",
      "3/4 cup granulated sugar",
      "3/4 cup packed brown sugar",
      "1 teaspoon vanilla extract",
      "2 large eggs",
      "2 1/4 cups all-purpose flour",
      "1 teaspoon baking soda",
      "1 teaspoon salt",
      "2 cups chocolate chips"
    ]
  },
  ...
]
Cómo generar valores de enumeración
En algunos casos, es posible que desees que el modelo elija una sola opción de una lista. Para implementar este comportamiento, puedes pasar un enum en tu esquema. Puedes usar una opción de enumeración en cualquier lugar en el que puedas usar un string en el responseSchema, ya que una enumeración es un array de cadenas. Al igual que un esquema JSON, un enum te permite restringir el resultado del modelo para que cumpla con los requisitos de tu aplicación.

Por ejemplo, supongamos que estás desarrollando una aplicación para clasificar instrumentos musicales en una de cinco categorías: "Percussion", "String", "Woodwind", "Brass" o ""Keyboard"". Podrías crear un enum para ayudarte con esta tarea.

En el siguiente ejemplo, pasas una enumeración como responseSchema, lo que restringe el modelo para que elija la opción más adecuada.

Python
JavaScript
REST

from google import genai
import enum

class Instrument(enum.Enum):
  PERCUSSION = "Percussion"
  STRING = "String"
  WOODWIND = "Woodwind"
  BRASS = "Brass"
  KEYBOARD = "Keyboard"

client = genai.Client()
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='What type of instrument is an oboe?',
    config={
        'response_mime_type': 'text/x.enum',
        'response_schema': Instrument,
    },
)

print(response.text)
# Woodwind
La biblioteca de Python traducirá las declaraciones de tipo para la API. Sin embargo, la API acepta un subconjunto del esquema de OpenAPI 3.0 (Schema).

Existen otras dos formas de especificar una enumeración. Puedes usar un Literal: ```

Python

Literal["Percussion", "String", "Woodwind", "Brass", "Keyboard"]
También puedes pasar el esquema como JSON:

Python

from google import genai

client = genai.Client()
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='What type of instrument is an oboe?',
    config={
        'response_mime_type': 'text/x.enum',
        'response_schema': {
            "type": "STRING",
            "enum": ["Percussion", "String", "Woodwind", "Brass", "Keyboard"],
        },
    },
)

print(response.text)
# Woodwind
Además de los problemas básicos de opción múltiple, puedes usar una enumeración en cualquier parte de un esquema JSON. Por ejemplo, podrías pedirle al modelo una lista de títulos de recetas y usar un enum Grade para asignarle a cada título una calificación de popularidad:

Python

from google import genai

import enum
from pydantic import BaseModel

class Grade(enum.Enum):
    A_PLUS = "a+"
    A = "a"
    B = "b"
    C = "c"
    D = "d"
    F = "f"

class Recipe(BaseModel):
  recipe_name: str
  rating: Grade

client = genai.Client()
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='List 10 home-baked cookie recipes and give them grades based on tastiness.',
    config={
        'response_mime_type': 'application/json',
        'response_schema': list[Recipe],
    },
)

print(response.text)
La respuesta podría verse de la siguiente manera:


[
  {
    "recipe_name": "Chocolate Chip Cookies",
    "rating": "a+"
  },
  {
    "recipe_name": "Peanut Butter Cookies",
    "rating": "a"
  },
  {
    "recipe_name": "Oatmeal Raisin Cookies",
    "rating": "b"
  },
  ...
]
Acerca de los esquemas JSON
La configuración del modelo para la salida JSON con el parámetro responseSchema se basa en el objeto Schema para definir su estructura. Este objeto representa un subconjunto selecto del objeto de esquema de OpenAPI 3.0 y también agrega un campo propertyOrdering.

Nota: En Python, cuando usas un modelo de Pydantic, no necesitas trabajar directamente con objetos Schema, ya que se convierte automáticamente al esquema JSON correspondiente. Para obtener más información, consulta Esquemas JSON en Python.
Esta es una representación pseudo-JSON de todos los campos de Schema:


{
  "type": enum (Type),
  "format": string,
  "description": string,
  "nullable": boolean,
  "enum": [
    string
  ],
  "maxItems": integer,
  "minItems": integer,
  "properties": {
    string: {
      object (Schema)
    },
    ...
  },
  "required": [
    string
  ],
  "propertyOrdering": [
    string
  ],
  "items": {
    object (Schema)
  }
}
El Type del esquema debe ser uno de los tipos de datos de OpenAPI o una unión de esos tipos (con anyOf). Solo un subconjunto de campos es válido para cada Type. En la siguiente lista, se asigna cada Type a un subconjunto de los campos que son válidos para ese tipo:

string -> enum, format, nullable
integer -> format, minimum, maximum, enum, nullable
number -> format, minimum, maximum, enum, nullable
boolean -> nullable
array -> minItems, maxItems, items, nullable
object -> properties, required, propertyOrdering, nullable
A continuación, se muestran algunos esquemas de ejemplo que muestran combinaciones válidas de tipo y campo:


{ "type": "string", "enum": ["a", "b", "c"] }

{ "type": "string", "format": "date-time" }

{ "type": "integer", "format": "int64" }

{ "type": "number", "format": "double" }

{ "type": "boolean" }

{ "type": "array", "minItems": 3, "maxItems": 3, "items": { "type": ... } }

{ "type": "object",
  "properties": {
    "a": { "type": ... },
    "b": { "type": ... },
    "c": { "type": ... }
  },
  "nullable": true,
  "required": ["c"],
  "propertyOrdering": ["c", "b", "a"]
}
Para obtener la documentación completa de los campos de esquema tal como se usan en la API de Gemini, consulta la referencia del esquema.

Ordenamiento de propiedades
Advertencia: Cuando configures un esquema JSON, asegúrate de establecer propertyOrdering[] y, cuando proporciones ejemplos, asegúrate de que el orden de las propiedades en los ejemplos coincida con el esquema.
Cuando trabajas con esquemas de JSON en la API de Gemini, el orden de las propiedades es importante. De forma predeterminada, la API ordena las propiedades alfabéticamente y no conserva el orden en el que se definen (aunque los SDKs de IA generativa de Google pueden conservar este orden). Si proporcionas ejemplos al modelo con un esquema configurado y el orden de las propiedades de los ejemplos no coincide con el orden de las propiedades del esquema, el resultado podría ser divagante o inesperado.

Para garantizar un orden coherente y predecible de las propiedades, puedes usar el campo opcional propertyOrdering[].


"propertyOrdering": ["recipeName", "ingredients"]
propertyOrdering[], que no es un campo estándar en la especificación de OpenAPI, es un array de cadenas que se usa para determinar el orden de las propiedades en la respuesta. Si especificas el orden de las propiedades y, luego, proporcionas ejemplos con propiedades en ese mismo orden, es posible que mejores la calidad de los resultados. propertyOrdering solo se admite cuando creas types.Schema de forma manual.

Esquemas en Python
Cuando usas la biblioteca de Python, el valor de response_schema debe ser uno de los siguientes:

Un tipo, como lo usarías en una anotación de tipo (consulta el módulo typing de Python)
Instancia de genai.types.Schema
El equivalente de dict de genai.types.Schema
La forma más sencilla de definir un esquema es con un tipo de Pydantic (como se muestra en el ejemplo anterior):

Python

config={'response_mime_type': 'application/json',
        'response_schema': list[Recipe]}
Cuando usas un tipo de Pydantic, la biblioteca de Python crea un esquema JSON para ti y lo envía a la API. Para obtener más ejemplos, consulta la documentación de la biblioteca de Python.

La biblioteca de Python admite esquemas definidos con los siguientes tipos (en los que AllowedType es cualquier tipo permitido):

int
float
bool
str
list[AllowedType]
AllowedType|AllowedType|...
Para los tipos estructurados:
dict[str, AllowedType]. Esta anotación declara que todos los valores del diccionario son del mismo tipo, pero no especifica qué claves se deben incluir.
Modelos de Pydantic definidos por el usuario. Este enfoque te permite especificar los nombres de las claves y definir diferentes tipos para los valores asociados con cada una de las claves, incluidas las estructuras anidadas.
Compatibilidad con el esquema JSON
JSON Schema es una especificación más reciente que OpenAPI 3.0, en la que se basa el objeto Schema. La compatibilidad con JSON Schema está disponible como versión preliminar a través del campo responseJsonSchema, que acepta cualquier esquema JSON con las siguientes limitaciones:

Solo funciona con Gemini 2.5.
Si bien se pueden pasar todas las propiedades del esquema JSON, no todas son compatibles. Consulta la documentación del campo para obtener más detalles.
Las referencias recursivas solo se pueden usar como el valor de una propiedad de objeto no obligatoria.
Las referencias recursivas se expanden hasta un grado finito, según el tamaño del esquema.
Los esquemas que contienen $ref no pueden contener ninguna propiedad que no comience con un $.
Este es un ejemplo de cómo generar un esquema JSON con Pydantic y enviarlo al modelo:


curl "https://generativelanguage.googleapis.com/v1alpha/models/\
gemini-2.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY"\
    -H 'Content-Type: application/json' \
    -d @- <<EOF
{
  "contents": [{
    "parts":[{
      "text": "Please give a random example following this schema"
    }]
  }],
  "generationConfig": {
    "response_mime_type": "application/json",
    "response_json_schema": $(python3 - << PYEOF
    from enum import Enum
    from typing import List, Optional, Union, Set
    from pydantic import BaseModel, Field, ConfigDict
    import json

    class UserRole(str, Enum):
        ADMIN = "admin"
        VIEWER = "viewer"

    class Address(BaseModel):
        street: str
        city: str

    class UserProfile(BaseModel):
        username: str = Field(description="User's unique name")
        age: Optional[int] = Field(ge=0, le=120)
        roles: Set[UserRole] = Field(min_items=1)
        contact: Union[Address, str]
        model_config = ConfigDict(title="User Schema")

    # Generate and print the JSON Schema
    print(json.dumps(UserProfile.model_json_schema(), indent=2))
    PYEOF
    )
  }
}
EOF
Aún no se admite pasar el esquema JSON directamente cuando se usa el SDK.

Prácticas recomendadas
Ten en cuenta las siguientes consideraciones y prácticas recomendadas cuando uses un esquema de respuesta:

El tamaño del esquema de respuesta se considera para el límite de tokens de entrada.
De forma predeterminada, los campos son opcionales, lo que significa que el modelo puede propagar los campos o omitirlos. Puedes configurar los campos según sea necesario para forzar al modelo a proporcionar un valor. Si no hay suficiente contexto en la instrucción de entrada asociada, el modelo genera respuestas principalmente en función de los datos con los que se entrenó.
Un esquema complejo puede generar un error InvalidArgument: 400. La complejidad puede deberse a nombres de propiedades largos, límites de longitud de arrays largos, enumeraciones con muchos valores, objetos con muchas propiedades opcionales o una combinación de estos factores.

Si recibes este error con un esquema válido, realiza uno o más de los siguientes cambios para resolverlo:

Acorta los nombres de las propiedades o los nombres de las enumeraciones.
Compacta los arrays anidados.
Reduce la cantidad de propiedades con restricciones, como los números con límites mínimos y máximos.
Reduce la cantidad de propiedades con restricciones complejas, como las que tienen formatos complejos, como date-time.
Reduce la cantidad de propiedades opcionales.
Reduce la cantidad de valores válidos para las enumeraciones.
Si no ves los resultados que esperas, agrega más contexto a tus instrucciones de entrada o revisa tu esquema de respuesta. Por ejemplo, revisa la respuesta del modelo sin un resultado estructurado para ver cómo responde. Luego, puedes actualizar el esquema de respuesta para que se adapte mejor al resultado del modelo. Si deseas obtener más sugerencias para solucionar problemas relacionados con el resultado estructurado, consulta la guía de solución de problemas.

Cómo realizar la puesta a tierra con Google Maps

La fundamentación con Google Maps conecta las capacidades generativas de Gemini con los datos enriquecidos, fácticos y actualizados de Google Maps. Esta función permite a los desarrolladores incorporar fácilmente la funcionalidad basada en la ubicación en sus aplicaciones. Cuando una búsqueda del usuario tiene un contexto relacionado con los datos de Maps, el modelo de Gemini aprovecha Google Maps para proporcionar respuestas fácticas y actualizadas que son pertinentes para la ubicación especificada por el usuario o el área general.

Respuestas precisas y basadas en la ubicación: Aprovecha los datos extensos y actuales de Google Maps para las búsquedas específicas de una ubicación geográfica.
Personalización mejorada: Adapta las recomendaciones y la información según las ubicaciones proporcionadas por el usuario.
Información contextual y widgets: Tokens contextuales para renderizar widgets interactivos de Google Maps junto con el contenido generado.
Comenzar
En este ejemplo, se muestra cómo integrar Grounding con Google Maps en tu aplicación para proporcionar respuestas precisas y basadas en la ubicación a las preguntas de los usuarios. La instrucción solicita recomendaciones locales con una ubicación del usuario opcional, lo que permite que el modelo de Gemini aproveche los datos de Google Maps.

Python
JavaScript
REST

from google import genai
from google.genai import types

client = genai.Client()

prompt = "What are the best Italian restaurants within a 15-minute walk from here?"

response = client.models.generate_content(
    model='gemini-2.5-flash-lite',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on grounding with Google Maps
        tools=[types.Tool(google_maps=types.GoogleMaps())],
        # Optionally provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
Cómo funciona la fundamentación con Google Maps
La fundamentación con Google Maps integra la API de Gemini en el ecosistema geográfico de Google usando la API de Maps como fuente de fundamentación. Cuando la búsqueda de un usuario contiene contexto geográfico, el modelo de Gemini puede invocar la herramienta Fundamentos con Google Maps. Luego, el modelo puede generar respuestas fundamentadas en los datos de Google Maps que sean pertinentes para la ubicación proporcionada.

Por lo general, el proceso incluye lo siguiente:

Consulta del usuario: Un usuario envía una consulta a tu aplicación, que puede incluir contexto geográfico (p.ej., "Cafeterías cerca de mí", "Museos en San Francisco").
Invocación de la herramienta: El modelo de Gemini, que reconoce la intención geográfica, invoca la herramienta de fundamentación con Google Maps. De manera opcional, se puede proporcionar a esta herramienta el latitude y el longitude del usuario para obtener resultados que tengan en cuenta la ubicación.
Recuperación de datos: El servicio de Grounding con Google Maps consulta Google Maps para obtener información pertinente (p.ej., lugares, opiniones, fotos, direcciones y horarios de atención).
Generación fundamentada: Los datos recuperados de Maps se usan para fundamentar la respuesta del modelo de Gemini, lo que garantiza la precisión y la relevancia fácticas.
Token de respuesta y widget: El modelo devuelve una respuesta de texto que incluye citas de fuentes de Google Maps. De manera opcional, la respuesta de la API también puede contener un google_maps_widget_context_token, lo que permite a los desarrolladores renderizar un widget contextual de Google Maps en su aplicación para la interacción visual.
Por qué y cuándo usar la Fundamentación con Google Maps
La fundamentación con Google Maps es ideal para las aplicaciones que requieren información precisa, actualizada y específica de la ubicación. Mejora la experiencia del usuario, ya que proporciona contenido pertinente y personalizado respaldado por la extensa base de datos de Google Maps de más de 250 millones de lugares en todo el mundo.

Debes usar la fundamentación con Google Maps cuando tu aplicación necesite lo siguiente:

Proporciona respuestas completas y precisas a preguntas específicas de la ubicación geográfica.
Crea planificadores de viajes y guías locales conversacionales.
Recomendar lugares de interés según la ubicación y las preferencias del usuario, como restaurantes o tiendas
Crea experiencias basadas en la ubicación para servicios de redes sociales, venta minorista o entrega de comida.
La fundamentación con Google Maps se destaca en los casos de uso en los que la proximidad y los datos fácticos actuales son fundamentales, como encontrar la "mejor cafetería cerca de mí" o recibir indicaciones para llegar.

Métodos y parámetros de la API
La fundamentación con Google Maps se expone a través de la API de Gemini como una herramienta dentro del método generateContent. Para habilitar y configurar la fundamentación con Google Maps, incluye un objeto googleMaps en el parámetro tools de tu solicitud.

JSON

{
  "contents": [{
    "parts": [
      {"text": "Restaurants near Times Square."}
    ]
  }],
  "tools":  { "googleMaps": {} }
}
La herramienta googleMaps también puede aceptar un parámetro booleano enableWidget, que se usa para controlar si el campo googleMapsWidgetContextToken se devuelve en la respuesta. Se puede usar para mostrar un widget contextual de Places.

JSON

{
"contents": [{
    "parts": [
      {"text": "Restaurants near Times Square."}
    ]
  }],
  "tools":  { "googleMaps": { "enableWidget": true } }
}
Además, la herramienta admite pasar la ubicación contextual como toolConfig.

JSON

{
  "contents": [{
    "parts": [
      {"text": "Restaurants near here."}
    ]
  }],
  "tools":  { "googleMaps": {} },
  "toolConfig":  {
    "retrievalConfig": {
      "latLng": {
        "latitude": 40.758896,
        "longitude": -73.985130
      }
    }
  }
}
Cómo comprender la respuesta de fundamentación
Cuando una respuesta se fundamenta correctamente con datos de Google Maps, incluye un campo groundingMetadata. Estos datos estructurados son esenciales para verificar las afirmaciones y crear una experiencia de citas enriquecida en tu aplicación, así como para cumplir con los requisitos de uso del servicio.

JSON

{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "CanteenM is an American restaurant with..."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "groundingChunks": [
          {
            "maps": {
              "uri": "https://maps.google.com/?cid=13100894621228039586",
              "title": "Heaven on 7th Marketplace",
              "placeId": "places/ChIJ0-zA1vBZwokRon0fGj-6z7U"
            },
            // repeated ...
          }
        ],
        "groundingSupports": [
          {
            "segment": {
              "startIndex": 0,
              "endIndex": 79,
              "text": "CanteenM is an American restaurant with a 4.6-star rating and is open 24 hours."
            },
            "groundingChunkIndices": [0]
          },
          // repeated ...
        ],
        "webSearchQueries": [
          "restaurants near me"
        ],
        "googleMapsWidgetContextToken": "widgetcontent/..."
      }
    }
  ]
}
La API de Gemini devuelve la siguiente información con groundingMetadata:

groundingChunks: Es un array de objetos que contiene las fuentes de maps (uri, placeId y title).
groundingSupports: Es un array de fragmentos para conectar el texto de respuesta del modelo con las fuentes en groundingChunks. Cada fragmento vincula un intervalo de texto (definido por startIndex y endIndex) a uno o más groundingChunkIndices. Esta es la clave para crear citas intercaladas.
googleMapsWidgetContextToken: Es un token de texto que se puede usar para renderizar un widget contextual de Places.
Si deseas ver un fragmento de código que muestra cómo renderizar citas intercaladas en el texto, consulta el ejemplo en la documentación de Grounding con la Búsqueda de Google.

Cómo mostrar el widget contextual de Google Maps
Para usar el googleMapsWidgetContextToken que se devolvió, debes cargar la API de Google Maps JavaScript.

Casos de uso
La fundamentación con Google Maps admite una variedad de casos de uso que tienen en cuenta la ubicación. En los siguientes ejemplos, se muestra cómo diferentes instrucciones y parámetros pueden aprovechar la fundamentación con Google Maps. La información de los resultados fundamentados de Google Maps puede diferir de las condiciones reales.

Cómo responder preguntas específicas sobre lugares
Haz preguntas detalladas sobre un lugar específico para obtener respuestas basadas en las opiniones de los usuarios de Google y otros datos de Maps.

Python
JavaScript
REST

from google import genai
from google.genai import types

client = genai.Client()

prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?"

response = client.models.generate_content(
    model='gemini-2.5-flash-lite',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on the Maps tool
        tools=[types.Tool(google_maps=types.GoogleMaps())],

        # Provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
  ```
Proporcionar personalización basada en la ubicación
Obtener recomendaciones personalizadas según las preferencias de un usuario y un área geográfica específica

Python
JavaScript
REST

from google import genai
from google.genai import types

client = genai.Client()

prompt = "Which family-friendly restaurants near here have the best playground reviews?"

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps())],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context; this is Austin, TX.
          lat_lng=types.LatLng(
              latitude=30.2672, longitude=-97.7431))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
Asistencia con la planificación de itinerarios
Genera planes de varios días con instrucciones sobre cómo llegar e información sobre varias ubicaciones, lo que resulta ideal para aplicaciones de viajes.

En este ejemplo, se solicitó googleMapsWidgetContextToken habilitando el widget en la herramienta de Google Maps. Cuando se habilita, el token que se devuelve se puede usar para renderizar un widget contextual de Places con <gmp-places-contextual> component de la API de Maps JavaScript de Google Maps.

Python
JavaScript
REST

from google import genai
from google.genai import types

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps(enable_widget=True))],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context, this is in San Francisco.
          lat_lng=types.LatLng(
              latitude=37.78193, longitude=-122.40476))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')

  if widget_token := grounding.google_maps_widget_context_token:
    print('-' * 40)
    print(f'<gmp-place-contextual context-token="{widget_token}"></gmp-place-contextual>')
Cuando se renderice el widget, se verá de la siguiente manera:

Ejemplo de un widget de mapas cuando se renderiza

Requisitos de uso del servicio
En esta sección, se describen los requisitos de uso del servicio de Grounding con Google Maps.

Informa al usuario sobre el uso de las fuentes de Google Maps
Con cada resultado fundamentado de Google Maps, recibirás fuentes en groundingChunks que respaldan cada respuesta. También se devuelven los siguientes metadatos:

URI de origen
título
ID
Cuando presentes resultados de la fundamentación con Google Maps, debes especificar las fuentes asociadas de Google Maps y comunicarles a los usuarios lo siguiente:

Las fuentes de Google Maps deben aparecer inmediatamente después del contenido generado que admiten. Este contenido generado también se conoce como resultado fundamentado de Google Maps.
Las fuentes de Google Maps deben poder verse en una sola interacción del usuario.
Mostrar fuentes de Google Maps con vínculos a Google Maps
Para cada fuente en groundingChunks y en grounding_chunks.maps.placeAnswerSources.reviewSnippets, se debe generar una vista previa del vínculo según los siguientes requisitos:

Atribuye cada fuente a Google Maps según los lineamientos de atribución de texto de Google Maps.
Muestra el título de la fuente proporcionado en la respuesta.
Vincula la fuente con uri o googleMapsUri de la respuesta.
Estas imágenes muestran los requisitos mínimos para mostrar las fuentes y los vínculos de Google Maps.

Instrucción con respuesta que muestra las fuentes

Puedes contraer la vista de las fuentes.

Instrucción con respuesta y fuentes contraídas

Opcional: Mejora la vista previa del vínculo con contenido adicional, como el siguiente:

Se inserta un favicon de Google Maps antes de la atribución de texto de Google Maps.
Una foto de la URL de origen (og:image).
Para obtener más información sobre algunos de nuestros proveedores de datos de Google Maps y sus condiciones de licencia, consulta los avisos legales de Google Maps y Google Earth.

Lineamientos para la atribución de texto de Google Maps
Cuando atribuyas fuentes a Google Maps en texto, sigue estos lineamientos:

No modifiques el texto de Google Maps de ninguna manera:
No cambies el uso de mayúsculas en Google Maps.
No dividas Google Maps en varias líneas.
No localices Google Maps en otro idioma.
Evita que los navegadores traduzcan Google Maps usando el atributo HTML translate="no".
Aplica el siguiente estilo al texto de Google Maps:
Propiedad	Estilo
Font family	Roboto. La carga de la fuente es opcional.
Fallback font family	Cualquier fuente de cuerpo sans serif que ya se use en tu producto o "Sans-Serif" para invocar la fuente predeterminada del sistema
Font style	Normal
Font weight	400
Font color	Blanco, negro (#1F1F1F) o gris (#5E5E5E). Mantén un contraste accesible (4.5:1) con el fondo.
Font size	
Tamaño de fuente mínimo: 12 sp
Tamaño de fuente máximo: 16 sp
Para obtener información sobre sp, consulta las unidades de tamaño de fuente en el sitio web de Material Design.
Spacing	Normal
Ejemplo de CSS
El siguiente código CSS renderiza Google Maps con el color y el estilo tipográfico adecuados sobre un fondo blanco o claro.

CSS

@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

.GMP-attribution {

font-family: Roboto, Sans-Serif;
font-style: normal;
font-weight: 400;
font-size: 1rem;
letter-spacing: normal;
white-space: nowrap;
color: #5e5e5e;
}
Token de contexto, ID de lugar y ID de opinión
Los datos de Google Maps incluyen el token de contexto, el ID de lugar y el ID de opinión. Puedes almacenar en caché, guardar y exportar los siguientes datos de respuesta:

googleMapsWidgetContextToken
placeId
reviewId
No se aplican las restricciones contra el almacenamiento en caché de las Condiciones de Fundamentación con Google Maps.

Actividad y territorio prohibidos
La fundamentación con Google Maps tiene restricciones adicionales para cierto contenido y actividades para mantener una plataforma segura y confiable. Además de las restricciones de uso que se mencionan en las Condiciones, no usarás la fundamentación con Google Maps para actividades de alto riesgo, incluidos los servicios de respuesta ante emergencias. No distribuirás ni comercializarás tu aplicación que ofrece Grounding con Google Maps en un Territorio Prohibido. Los territorios prohibidos actuales son los siguientes:

China
Crimea
Cuba
República Popular de Donetsk
Irán
República Popular de Luhansk
Corea del Norte
Siria
Vietnam
Es posible que esta lista se actualice de forma periódica.

Prácticas recomendadas
Proporciona la ubicación del usuario: Para obtener las respuestas más relevantes y personalizadas, siempre incluye user_location (latitud y longitud) en tu configuración de googleMapsGrounding cuando se conozca la ubicación del usuario.
Renderiza el widget contextual de Google Maps: El widget contextual se renderiza con el token de contexto, googleMapsWidgetContextToken, que se devuelve en la respuesta de la API de Gemini y se puede usar para renderizar contenido visual de Google Maps. Para obtener más información sobre el widget contextual, consulta Cómo fundamentar con el widget de Google Maps en la Guía para desarrolladores de Google.
Informa a los usuarios finales: Informa claramente a los usuarios finales que se usan datos de Google Maps para responder sus preguntas, en especial cuando la herramienta está habilitada.
Supervisa la latencia: En el caso de las aplicaciones conversacionales, asegúrate de que la latencia del percentil 95 para las respuestas fundamentadas se mantenga dentro de los umbrales aceptables para mantener una experiencia del usuario fluida.
Desactivar cuando no sea necesario: La fundamentación con Google Maps está desactivada de forma predeterminada. Solo habilítalo ("tools": [{"googleMaps": {}}]) cuando una búsqueda tenga un contexto geográfico claro para optimizar el rendimiento y el costo.

modelos de texto :

Modelos de Gemini

NUESTRO MODELO MÁS AVANZADO

Gemini 2.5 Pro
Nuestro modelo de pensamiento de vanguardia, capaz de razonar sobre problemas complejos en código, matemáticas y STEM, así como analizar grandes conjuntos de datos, bases de código y documentos con un contexto extenso.

Expande para obtener más información
RÁPIDO E INTELIGENTE

Gemini 2.5 Flash
Es nuestro mejor modelo en términos de relación precio-rendimiento y ofrece capacidades integrales. 2.5 Flash es ideal para el procesamiento a gran escala, la baja latencia, las tareas de gran volumen que requieren pensamiento y los casos de uso de agentes.

Expande para obtener más información
ULTRA RÁPIDA

Gemini 2.5 Flash-Lite
Nuestro modelo flash más rápido, optimizado para la rentabilidad y el alto rendimiento.

Expande para obtener más información

Versiones del modelo
Imagen 4
Propiedad	Descripción
Código del modelo 
API de Gemini

imagen-4.0-generate-001
imagen-4.0-ultra-generate-001
imagen-4.0-fast-generate-001

Tipos de datos admitidos
Entrada

Texto

Resultado

Imágenes

Límites de tokens[*]
Límite de tokens de entrada

480 tokens (texto)

Imágenes de salida

1 a 4 (Ultra/Estándar/Rápido)

Última actualización	Junio de 2025
Imagen 3
Propiedad	Descripción
Código del modelo 
API de Gemini

imagen-3.0-generate-002

Tipos de datos admitidos
Entrada

Texto

Resultado

Imágenes

Límites de tokens[*]
Límite de tokens de entrada

N/A

Imágenes de salida

Hasta 4

Última actualización	Febrero de 2025

recoemndaciones : en lo que es chat y voz usa gemini 2.5 pro , el resto puedes tal vez ejecutar pruebas 