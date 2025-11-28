from project.main_agent import run_agent
import gradio as gr

def chat(u):
    return run_agent(u)

ui = gr.Interface(fn=chat, inputs="text", outputs="text")

if __name__ == "__main__":
    ui.launch()
