import gradio as gr
from summarizer import summarize

gr.Interface(
    fn = summarize,
    inputs = gr.Textbox(label="Enter a URL"),
    outputs = gr.Textbox(label="Summary"),
    title = "Website Summarizer",
    description = "Enter a URL to get a short, friendly summary of the website's contents.",
).launch(share=True)