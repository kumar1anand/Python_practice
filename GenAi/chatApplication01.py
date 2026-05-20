#! pip install gradio 

import gradio as gr
from google import genai
from google.genai import types
client = genai.Client(api_key="AIzaSyBMwtinq_Sraji5TSVcbBvUd2kW4O3CtPQ")

def chat_fun(message, history):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=message
        # config=types.ContentResponseFormat(
        #         system_instructions="You are a helpful contact center assistant."),
        #         contents= message
        )
            
    
    return response.text


gr.ChatInterface(
    fn=chat_fun, 
    title="GenAI Chat Application",
    description="Ask me anything!"
    ).launch(server_name="0.0.0.0", server_port=7860,share=True)