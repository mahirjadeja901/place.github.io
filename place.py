import streamlit as st
from PIL import Image, ImageDraw
import imageio
import numpy as np
import os

def create_image(text, width=200, height=100, bgcolor=(255, 255, 255)):
    """Create an image with the specified text."""
    img = Image.new('RGB', (width, height), bgcolor)
    draw = ImageDraw.Draw(img)
    textwidth, textheight = draw.textsize(text)
    text_x = (width - textwidth) // 2
    text_y = (height - textheight) // 2
    draw.text((text_x, text_y), text, fill=(0, 0, 0))
    return img

def create_gif(texts):
    """Create a GIF from a list of texts."""
    images = []
    for text in texts:
        img = create_image(text)
        images.append(img)
    
    # Save images as a GIF
    gif_path = 'custom_gif.gif'
    images[0].save(gif_path, save_all=True, append_images=images[1:], duration=500, loop=0)
    return gif_path

# Streamlit UI
st.title("Custom GIF Generator")

text_input = st.text_input("Enter text for the GIF (comma-separated):", "Hello, World, Streamlit")

if st.button("Generate GIF"):
    if text_input:
        texts = [text.strip() for text in text_input.split(',')]
        gif_path = create_gif(texts)
        
        # Display the GIF
        st.image(gif_path, caption="Generated GIF", use_column_width=True)
        
        # Optionally, provide a download link
        with open(gif_path, "rb") as f:
            st.download_button("Download GIF", f, file_name="custom_gif.gif")
    else:
        st.warning("Please enter some text.")

# Clean up generated GIF after download
if os.path.exists(gif_path):
    os.remove(gif_path)
