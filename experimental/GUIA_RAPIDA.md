# 🧪 GUÍA RÁPIDA - FASE 1: EXPERIMENTACIÓN

## ✅ CHECKLIST RÁPIDO

### 1. Verificar Instalación
```powershell
cd experimental
python verificar_sistema.py
```

**Debe mostrar**:
- ✅ Python 3.8+
- ✅ Todas las dependencias instaladas
- ✅ API Key configurada
- ✅ Conexión con Gemini exitosa

---

### 2. Ejecutar Tests en Orden

#### Test 1: Texto (OBLIGATORIO - Empezar aquí)
```powershell
python test_gemini_text.py
```

**Qué prueba**:
- ✅ Respuestas simples
- ✅ System instructions
- ✅ Chat multi-turno (contexto)
- ✅ Streaming
- ✅ Diferentes temperaturas
- ✅ Modo rápido (sin pensamiento)

**Tiempo estimado**: 3-5 minutos

---

#### Test 2: Visión y OCR
```powershell
python test_gemini_vision.py
```

**Qué prueba**:
- ✅ Leer imágenes locales
- ✅ OCR de vouchers
- ✅ Extracción JSON estructurada
- ✅ Múltiples imágenes
- ✅ Detección de objetos

**Genera**: Imágenes de prueba automáticamente

**Tiempo estimado**: 4-6 minutos

---

#### Test 3: Generación de Imágenes
```powershell
python test_gemini_image.py
```

**Qué prueba**:
- ✅ Imagen simple desde texto
- ✅ Descripción detallada
- ✅ Diferentes estilos (fotorrealista, kawaii, minimalista)
- ✅ Logo profesional
- ✅ Estado de WhatsApp (9:16)
- ✅ Foto de producto e-commerce

**Genera**: Carpeta `imagenes_generadas/` con todas las imágenes

**Tiempo estimado**: 5-8 minutos

---

#### Test 4: Texto a Voz (TTS)
```powershell
python test_gemini_tts.py
```

**Qué prueba**:
- ✅ Voz simple
- ✅ 5 voces diferentes
- ✅ Diferentes estilos (alegre, susurro, serio)
- ✅ Conversación multi-hablante
- ✅ Mensaje promocional profesional

**Genera**: Carpeta `audios_generados/` con archivos WAV

**Tiempo estimado**: 4-6 minutos

---

#### Test 5: JSON Estructurado
```powershell
python test_gemini_json.py
```

**Qué prueba**:
- ✅ Extracción de datos de pago
- ✅ Clasificación de mensajes
- ✅ Listas estructuradas
- ✅ Análisis de conversaciones
- ✅ Validación completa con enums

**Casos de uso real**: Perfecto para el bot

**Tiempo estimado**: 3-5 minutos

---

## 📊 RESULTADOS ESPERADOS

### Si todo funciona ✅
Cada test debe mostrar:
- Respuestas coherentes de Gemini
- Archivos generados (imágenes/audio)
- JSON válido y parseado
- Sin errores de conexión

### Si hay errores ❌

#### Error: API Key
```
❌ API Key de Gemini no configurada
```
**Solución**:
1. Edita `.env`
2. Verifica que tenga: `GEMINI_API_KEY=AIzaSyDiyBs75bDIsM7kTl36DT0mccOVFFfETiI`

#### Error: Dependencias
```
❌ No module named 'google'
```
**Solución**:
```powershell
pip install -r requirements.txt
```

#### Error: Rate Limit
```
❌ Resource exhausted
```
**Solución**: Espera 1 minuto y vuelve a intentar

---

## 🎯 PRÓXIMOS PASOS

Una vez completados TODOS los tests:

### 1. Revisar Resultados
- Verifica que todas las imágenes se generaron correctamente
- Escucha los audios generados
- Revisa los JSON estructurados

### 2. Documentar
```powershell
# Crear documento con tus observaciones
notepad RESULTADOS_FASE1.md
```

**Documenta**:
- ✅ Tests que funcionaron
- ❌ Tests que fallaron (si alguno)
- ⏱️ Tiempos de respuesta
- 💡 Observaciones sobre calidad

### 3. Continuar con Fase 2
Una vez completa la experimentación:
```powershell
# Ver plan de la siguiente fase
notepad ..\PLAN_DESARROLLO.md
```

Busca la sección: **FASE 2: BOT DE WHATSAPP**

---

## 🚨 SOLUCIÓN DE PROBLEMAS

### Test se congela
- Presiona `Ctrl+C`
- Espera 30 segundos
- Vuelve a ejecutar

### Imágenes no se generan
- Verifica espacio en disco
- Revisa permisos de escritura en carpeta

### Audio no se escucha
- Verifica que los archivos .wav existan
- Usa Windows Media Player o VLC

### JSON inválido
- Normal en algunos casos
- El modelo lo intenta de nuevo automáticamente

---

## 📝 NOTAS IMPORTANTES

1. **No saltar tests**: Cada uno prueba funcionalidades diferentes
2. **Internet requerido**: Todos los tests requieren conexión
3. **Tiempo total**: ~20-30 minutos para todos los tests
4. **Archivos generados**: Se crean en carpetas automáticamente

---

## ✅ CHECKLIST FINAL DE FASE 1

- [ ] `verificar_sistema.py` pasó sin errores
- [ ] `test_gemini_text.py` completado ✅
- [ ] `test_gemini_vision.py` completado ✅
- [ ] `test_gemini_image.py` completado ✅
- [ ] `test_gemini_tts.py` completado ✅
- [ ] `test_gemini_json.py` completado ✅
- [ ] Archivos generados revisados ✅
- [ ] Resultados documentados ✅

**Cuando todos estén ✅**: ¡Lista para Fase 2! 🎉

---

**Última actualización**: 22 de Octubre, 2025
**Fase**: 1 - Experimentación
**Estado**: En progreso
