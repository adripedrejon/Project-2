import requests
from PIL import Image, ImageDraw, ImageFont, ImageColor
from io import BytesIO
import streamlit as st
import numpy as np

HUGGING_TOKEN = ""
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"


headers = {"Authorization": f"Bearer {HUGGING_TOKEN}"}

def generate_logo(product_name, logo_color, font_style="Arial", max_width=300):
    """Generates a minimalist and sophisticated logo using Hugging Face API."""

    font_descriptions = {
        "Arial": "a clean, sans-serif font with smooth lines and a modern look.",
        "Helvetica": "a neutral sans-serif font with a timeless, professional appeal.",
        "Times New Roman": "a classic serif font evoking authority and elegance.",
        "Courier New": "a monospaced font with a retro feel.",
        "Verdana": "a sans-serif font designed for clarity and readability."
    }

    font_description = font_descriptions.get(font_style, f"a {font_style} font")

    # Define the prompt for the logo
    prompt = f"""
    Create a minimalist and sophisticated logo for a product named '{product_name}'. 
    The logo should feature the product name '{product_name}' prominently displayed in the center.
    The logo must use the **exact** color '{logo_color}' as specified, with no variations or deviations in shade.
    The logo has to use the font style '{font_description}'.
    Use a subtle geometric shape (e.g., thin circle or rounded rectangle) to frame the product name.
    The design should have a clean, modern, and professional look with a light or transparent background.
    Avoid gradients, complex illustrations, and ensure the design is simple and recognizable.
    """
    
    data = {"inputs": prompt, "options": {"use_gpu": True}}

    try:
        # API Request to generate the logo
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()  # Raise an error if the request fails
        
        img = Image.open(BytesIO(response.content))
        img.thumbnail((max_width, max_width))  # Maintain aspect ratio
        return img

    except requests.exceptions.RequestException as e:
        print(f"Error generating logo: {e}")
        return None
