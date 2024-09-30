import os
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr
load_dotenv()


client = OpenAI(
    api_key = os.getenv("OPEN_AI_KEY"),
)

def chat_with_gpt(prompt):
    
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return completion.choices[0].message.content
    

# Gradio interface
iface = gr.Interface(
    fn=chat_with_gpt,
    inputs=gr.Textbox(placeholder="Type your message here..."),
    outputs=gr.Textbox(placeholder="Bot response will appear here..."),
    title="GPT-JBbot",
    description="Chat with GPT-JBbot, a chatbot trained on the GPT-3.5-turbo model."
)

if __name__ == "__main__":
    iface.launch(share=True)  # Share the link publicly if desired
