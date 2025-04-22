import requests
from PIL import Image, ImageDraw, ImageFont, ImageColor
from gradio_client import Client, handle_file
from io import BytesIO
import streamlit as st
import numpy as np
import base64
import os

HUGGING_TOKEN = "" # Insert your KEY
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"


headers = {"Authorization": f"Bearer {HUGGING_TOKEN}"}


def generate_logo(product_name, logo_color, font_style="Arial", max_width=300):
    """Generates a logo using the UNO-FLUX model via Hugging Face gradio_client."""
    font_descriptions = {
    "Arial": "a clean, sans-serif font with smooth lines and a modern look.",
    "Helvetica": "a neutral sans-serif font with a timeless, professional appeal.",
    "Times New Roman": "a classic serif font evoking authority and elegance.",
    "Courier New": "a monospaced font with a retro feel.",
    "Verdana": "a sans-serif font designed for clarity and readability."
    }

    font_description = font_descriptions.get(font_style, f"a {font_style} font")

    prompt = f"""
    Create a minimalist and sophisticated logo for a product named '{product_name}'. 

    The logo must use the **exact** color '{logo_color}' as specified, with no variations or deviations in shade.
    The logo has to use the font style '{font_description}'.
    Use a subtle geometric shape (e.g., thin circle or rounded rectangle) to frame the product name.
    The design should have a clean, modern, and professional look with a light or transparent background.
    Avoid gradients, complex illustrations, and ensure the design is simple and recognizable.
    """

    try:
        client = Client("bytedance-research/UNO-FLUX", hf_token="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")

        example_img_url = 'https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png'

        result = client.predict(
            prompt=prompt,
            width=512,
            height=512,
            guidance=5,
            num_steps=30,
            seed=-1,
            image_prompt1=None,
            image_prompt2=None,
            image_prompt3=None,
            image_prompt4=None,
            api_name="/gradio_generate"
        )

        if isinstance(result, tuple):
            image_path = result[0]  # Use the first file path
            if os.path.exists(image_path):
                img = Image.open(image_path)
                img.thumbnail((max_width, max_width))
                return img
            else:
                print(f"File not found at: {image_path}")
        else:
            print("Unexpected result format:", result)

        return None

    except Exception as e:
        print(f"Error generating logo: {e}")
        return None

    

def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str
