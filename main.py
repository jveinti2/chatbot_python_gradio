import os
import gradio as gr
import openai
from dotenv import load_dotenv

# Cargar la API key de OpenAI desde el archivo .env
load_dotenv()

openai.api_key = os.getenv("OPEN_AI_KEY")

# Función para procesar texto o audio
def chat_with_gpt(text_input, audio_input):
    if text_input:
        prompt = text_input
    elif audio_input:
        # audio_input es la ruta del archivo de audio en formato .wav
        print(f"Ruta del archivo de audio: {audio_input}")
        try:
            # Abrimos el archivo de audio y lo transcribimos usando Whisper
            with open(audio_input, "rb") as audio_file:
                transcript = openai.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file
                )

                print(f"Transcripción del audio: {transcript.text}")

                prompt = transcript.text
        except Exception as e:
            return f"Error al procesar el audio: {str(e)}"
    else:
        return "Por favor, proporciona texto o audio."

    # Enviar el prompt a la API de OpenAI
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return completion.choices[0].message.content

# Interfaz de Gradio
iface = gr.Interface(
    fn=chat_with_gpt,
    inputs=[
        gr.Textbox(placeholder="Escribe tu mensaje aquí..."),  # Entrada de texto
        gr.Audio(sources="microphone", type="filepath")         # Entrada de audio en formato .wav
    ],
    outputs=gr.Textbox(placeholder="La respuesta del bot aparecerá aquí..."),
    title="GPT-JBbot",
    description="Chatea con GPT-JBbot usando texto o audio."
)

if __name__ == "__main__":
    iface.launch(share=True)
