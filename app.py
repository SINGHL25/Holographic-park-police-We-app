
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Holographic Park Police", layout="wide")
st.title("👮‍♂️ Holographic Police Visualization for Park Safety")

# Sidebar controls
st.sidebar.header("Adjust Hologram Settings")
glow_intensity = st.sidebar.slider("Hologram Glow Intensity", 0.0, 1.0, 0.5)
torch_brightness = st.sidebar.slider("Torch Brightness", 0, 100, 70)
fog_density = st.sidebar.slider("Night Fog Density", 0, 100, 30)

# Display AI-generated image
image_path = "images/hologram1.png"  # Replace with AI-generated hologram
img = Image.open(image_path)
st.image(img, caption="Holographic Police Officer at Night", use_column_width=True)

# Description panel
st.subheader("Psychological Effect")
st.write("""
The holographic officer with torchlight creates a **perception of vigilance**.
This can help **reduce crime perception and encourage safer behavior** in public parks at night.
""")
