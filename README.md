# Proyecto AI de Consulta de Datos de Deuda

Este proyecto utiliza técnicas de procesamiento de lenguaje natural y modelos de lenguaje para responder preguntas sobre datos económicos relacionados con la deuda. Se aprovechan datos históricos contenidos en un archivo CSV, que son procesados y vectorizados para permitir búsquedas semánticas y respuestas precisas basadas en el contenido de los registros.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instalación](#instalación)
- [Uso](#uso)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Contribuciones y Licencia](#contribuciones-y-licencia)

## Descripción

El proyecto se divide en dos partes principales:

1. **Vectorización y Almacenamiento de Datos:**
   - Se carga el archivo `deuda.csv` que contiene información histórica de deuda (fecha, saldos, desembolsos, pagos y transferencias netas).
   - Mediante el script `vector.py`, se procesa cada registro para crear documentos enriquecidos que contienen detalles claves del registro.
   - Estos documentos se indexan en una base de datos vectorial utilizando `Chroma` junto con las representaciones generadas por `OllamaEmbeddings`.

2. **Consulta y Generación de Respuestas:**
   - El script `main.py` implementa una interfaz interactiva en la línea de comandos que permite al usuario ingresar preguntas sobre economía.
   - Para cada pregunta, se recuperan los registros más relevantes de la base de datos vectorial.
   - Un modelo LLM (en este caso, "deepseek-r1:1.5b") utiliza una plantilla de prompt para generar una respuesta basada exclusivamente en la información proveniente de los datos.

## Estructura del Proyecto

- **deuda.csv**: Archivo CSV con datos históricos de deuda.
- **vector.py**: Script encargado de:
  - Leer y procesar el CSV.
  - Generar documentos a partir de cada registro.
  - Almacenar los documentos en una base de datos vectorial mediante `Chroma`.
- **main.py**: Script principal que:
  - Interactúa con el usuario a través de la terminal.
  - Recupera registros relevantes mediante el `retriever` configurado en `vector.py`.
  - Genera respuestas utilizando un modelo LLM mediante una plantilla de prompt.
- **requirements.txt**: Lista de dependencias necesarias para el proyecto.

## Instalación

1. **Clonar el repositorio:**

   ```shell
   git clone <URL_del_repositorio>
   cd localai
   ```

2. **Crear un entorno virtual (recomendado):**

   ```shell
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instalar las dependencias:**

   ```shell
   pip install -r requirements.txt
   ```

## Uso

Para ejecutar la aplicación, utiliza el script `main.py`:

```shell
python main.py
```

El programa iniciará una interfaz interactiva en la terminal donde podrás escribir preguntas relacionadas con economía y deuda. El asistente buscará registros relevantes y generará una respuesta basada en los datos.

Para salir del programa, escribe `q` y presiona Enter.

## Tecnologías Utilizadas

- **Python:** Lenguaje de programación principal.
- **Pandas:** Para lectura y manipulación de datos en CSV.
- **Langchain:** Para la gestión de prompts y cadenas de procesamiento.
- **OllamaEmbeddings:** Para generar representaciones vectoriales de los registros.
- **Chroma:** Base de datos vectorial para el almacenamiento y recuperación de documentos.
- **deepseek-r1:1.5b:** Modelo de lenguaje utilizado para la generación de respuestas.

## Contribuciones y Licencia

Este proyecto es de código abierto. Las contribuciones son bienvenidas. Si deseas reportar algún problema o proponer mejoras, abre un *issue* o envía un *pull request*.

El proyecto se distribuye bajo la licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles.

---

¡Gracias por utilizar este proyecto y esperamos tus aportaciones!