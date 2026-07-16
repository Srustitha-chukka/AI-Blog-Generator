
from google import genai
import gradio as gr
#geminai api key
client = genai.Client(api_key="")
def generate_blogs(topic,audience,tone,words):
  prompt = f"""
  write a {word}-word bloag
  Topic:{topic}
  Audience:{audience}
  Tone: {tone}
  Include:
  -Title
  - abstract
  -body
  -
  -Conclusion
  """
  responce = client.models.generate_content(
      model="gemini-2.5-flash",
       contentys=prompt
     
  )
   return response.text
demo = gr.Interface(
    fn=generate_blog,
    inputs=[
        gr.Textbox(label="Topic"),
        gr.Dropdown(["Tech Expert", "Friendly Student", "Storyteller"], label="Persona"),
        gr.Textbox(label="SEO Keyword"),
        gr.Radio(["Listicle", "How-to Guide", "Opinion Piece"], label="Format"),
        gr.Slider(minimum=200, maximum=1000, label="Word Count")
    ], 
    outputs="markdown" # Use 'markdown' so your bolding and headers render perfectly
    title=""
)
demo.launch()
