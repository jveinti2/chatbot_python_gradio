# Chatbot Python Gradio

<div
style="display: grid; place-content: center; grid-auto-flow: column; gap:10px">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" alt="Python Logo" width="100"/>
<img src="https://seeklogo.com/images/G/gradio-icon-logo-908AE1836C-seeklogo.com.png" alt="Gradio Logo" width="100"/>
<img src="https://static.vecteezy.com/system/resources/previews/022/227/364/non_2x/openai-chatgpt-logo-icon-free-png.png" alt="OpenAI Logo" width="100"/>
</div>

## Requisitos

- Python 3.x
- pip (gestor de paquetes de Python)

## Instalación

1. Clonar el repositorio:

   ```bash
   git clone <url_del_repositorio>
   ```

   ```bash
   cd <nombre_del_proyecto>
   ```

2. Crear y activar un entorno virtual:

   ```bash
   python -m venv venv
   ```

   ```bash
   .\venv\Scripts\activate  # Windows
   # o
   source venv/bin/activate  # Linux / macOS
   ```

3. Instalar dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Configurar la clave API de OpenAI:

   Asegúrate de establecer la variable de entorno `OPEN_AI_KEY` con tu clave API de OpenAI. Puedes hacerlo en la terminal:

   - **Windows (CMD)**:

     ```bash
     set OPEN_AI_KEY=tu_clave_api
     ```

   - **Windows (PowerShell)**:

     ```bash
     $env:OPEN_AI_KEY="tu_clave_api"
     ```

   - **Linux / macOS**:
     ```bash
     export OPEN_AI_KEY=tu_clave_api
     ```

5. Ejecutar la aplicación:

   ```bash
   python main.py
   ```

   Esto iniciará el chatbot utilizando Gradio, y podrás interactuar con él a través de tu navegador web.

## Uso

- Una vez que la aplicación esté en ejecución, abre tu navegador y ve a `http://127.0.0.1:7860` para acceder a la interfaz del chatbot.
- Escribe tu mensaje en el cuadro de texto y presiona Enter para obtener una respuesta.

## Notas

- Asegúrate de que tu clave API esté configurada correctamente antes de ejecutar la aplicación.
- Puedes detener la aplicación presionando `CTRL + C` en la terminal donde se está ejecutando.
