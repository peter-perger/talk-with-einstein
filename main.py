from functions import chat
import gradio as gr

custom_css = """
.gradio-container {
    max-width: 1300px !important; 
    margin: 0 auto;
}
"""


page = gr.Blocks(
    title="Chat with Einstein",
    css=custom_css
)

with page:
    gr.Markdown(
        """
        # Chat with Einstein
        Welcome to your personal Einstein assistant!
        """
    )

    chatbot = gr.Chatbot()

    msg = gr.Textbox()
    msg.submit(chat, [msg, chatbot], [msg, chatbot])

    clear = gr.Button("Clear chat")
    clear.click()


page.launch(theme=gr.themes.Soft())
