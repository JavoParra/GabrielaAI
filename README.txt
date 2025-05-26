# Gabriela AI - Chat Assistant with LangChain, Ollama, and RAG

Este proyecto implementa un asistente conversacional llamado **Gabriela** que responde preguntas utilizando modelos Ollama y recuperación aumentada por contexto (RAG) sobre documentos web, PDF o CSV. El sistema está construido con Clean Architecture y es fácilmente extensible para nuevos proveedores de calendario y fuentes de datos.

## Características
- **Chat interactivo** con historial de conversación.
- **Recuperación de contexto** relevante usando embeddings y búsqueda vectorial (Chroma).
- **Carga de documentos** desde web, PDF y CSV.
- **Soporte para múltiples proveedores de calendario** (Google Calendar, Google Sheets, Calendly).
- **Integración con modelos Ollama** para LLM y embeddings.
- **Arquitectura limpia** y modular.

## Requisitos
- Python 3.10+
- [Ollama](https://ollama.com/) instalado y corriendo localmente
- Modelos Ollama descargados: `llama3.2:latest` y `nomic-embed-text`

## Instalación
1. Clona este repositorio:
   ```sh
   git clone <url-del-repo>
   cd LLMLangChainExercise
   ```
2. Crea y activa un entorno virtual:
   ```sh
   python -m venv .venv
   .venv\Scripts\activate  # En Windows
   # source .venv/bin/activate  # En Linux/Mac
   ```
3. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   pip install chromadb beautifulsoup4
   ```
4. Descarga los modelos necesarios en Ollama:
   ```sh
   ollama pull llama3.2:latest
   ollama pull nomic-embed-text
   ```

## Uso
1. Ejecuta el script principal:
   ```sh
   python main.py
   ```
2. Interactúa con Gabriela escribiendo preguntas. Usa `historial` para ver el historial de chat o `salir` para terminar.

### Ejemplo de uso
```
Escribe tu pregunta (o 'salir' para terminar, 'historial' para ver el historial): ¿Qué es LangChain?
Gabriela: LangChain es una librería para construir aplicaciones de lenguaje natural con LLMs y datos externos.
```

## Estructura del Proyecto
- `main.py` — Punto de entrada, chat y lógica de RAG.
- `providers/` — Proveedores de calendario y lógica de integración externa.
- `requirements.txt` — Dependencias del proyecto.

## Personalización y Extensión
- Cambia la URL en `main.py` para usar otros documentos web.
- Puedes cargar documentos PDF o CSV usando las funciones `PDFFileLoader` y `csvFileLoader`.
- Agrega tus propios proveedores en la carpeta `providers/`.
- Modifica el prompt en `main.py` para personalizar la personalidad de Gabriela.

## Preguntas Frecuentes
- **¿Por qué no responde sobre el contenido del documento?**
  - Asegúrate de que los modelos estén descargados y que el contexto se recupere correctamente en el chat.
- **¿Cómo agrego más documentos?**
  - Usa las funciones de carga y concatena los resultados en la variable `docs`.
- **¿Puedo usar otros modelos de Ollama?**
  - Sí, solo cambia el nombre del modelo en la inicialización de `OllamaLLM` o `OllamaEmbeddings`.

## Notas
- Asegúrate de que el servidor Ollama esté corriendo antes de iniciar el chat.
- Puedes cargar y consultar documentos web, PDF o CSV fácilmente extendiendo las funciones de carga.
- Si tienes problemas con dependencias, revisa que tu entorno virtual esté activado y actualizado.

## Licencia
MIT

## Contacto
Para dudas o mejoras, abre un issue o contacta al autor.
