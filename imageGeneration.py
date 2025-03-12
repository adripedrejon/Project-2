import requests
from PIL import Image, ImageDraw, ImageFont, ImageColor
from io import BytesIO
import streamlit as st
import numpy as np

HUGGING_TOKEN = ""
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"


headers = {"Authorization": f"Bearer {HUGGING_TOKEN}"}

def hex_to_rgb(hex_color):
    """Convert hex color to RGB format with validation."""
    hex_color = hex_color.lstrip('#')  # Remove '#' if present
    if len(hex_color) != 6:
        raise ValueError(f"Invalid hex color format: {hex_color}")
    
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def generate_logo(product_name, logo_color="#008000", font_style="Arial", max_width=300):
    """Generates a minimalist and sophisticated logo using Hugging Face API."""
    rgb_color = hex_to_rgb(logo_color)
    rgb_str = f"rgb({rgb_color[0]}, {rgb_color[1]}, {rgb_color[2]})"

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
    The logo should feature the product name '{product_name}' prominently displayed in the center, 
    using the font style '{font_description}' and the color '{rgb_str}'.
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
