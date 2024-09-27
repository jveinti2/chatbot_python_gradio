import os
import openai
import gradio as gr

OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")

openai.api_key =  OPEN_AI_KEY

def chat_with_gpt(promt):
    response = openai.chat.completions.create(
        messages=[{"role": "user", "content": promt}],
        model="gpt-3.5-turbo",
    )
    
    return response['choices'][0]['message']['content']



#Gradio interface
iface = gr.Interface(
    fn=chat_with_gpt,
    inputs=gr.Textbox(placeholder="Type your message here..."),
    outputs=gr.Textbox(placeholder="Bot response will appear here..."),
    title="GPT-JBbot",
    description="Chat with GPT-JBbot, a chatbot trained on the GPT-3.5-turbo model."
)

if __name__ == "__main__":
    iface.launch()


# Is not requiered beacouse the chat interaction is with gradio interface
# if __name__ == "__main__":
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["exit", "quit", "bye", "adios", "chao" , "salir", "cerrar"]:
#             print("Bot: Goodbye!")
#             break
#         response = chat_with_gpt(user_input)
#         print(f"Bot: {response}")
    
    