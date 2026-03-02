from functions import chat, clear_chat
import gradio as gr

custom_css = """
.gradio-container {
    width: 900px !important;
    margin: 0 auto;
}
"""


page = gr.Blocks(title="Chat with Einstein")

with page:
    gr.Markdown(
        """
        # Chat with Einstein
        Welcome to your personal Einstein assistant!
        """
    )

    chatbot = gr.Chatbot(
        avatar_images=[None, './images/einstein.svg'],
        show_label=False
    )

    msg = gr.Textbox(show_label=False, placeholder="Send message")
    msg.submit(chat, [msg, chatbot], [msg, chatbot])

    clear = gr.Button("Clear chat")
    clear.click(clear_chat, outputs=[msg, chatbot])


page.launch(theme=gr.themes.Soft(),
            css=custom_css)
