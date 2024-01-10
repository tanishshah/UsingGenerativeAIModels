import requests
from vertexai.preview.generative_models import GenerativeModel, Image

imgReq = requests.get("<img_url>")
if (imgReq.status_code == 200):
    img = Image.from_bytes(imgReq.content)
    model = GenerativeModel("gemini-pro-vision")
    model_response = model.generate_content(
        [
            img, "describe the image please"
        ]
    )
    print(model_response.candidates[0].content.text)
else:
    print("Failed to get the image")
