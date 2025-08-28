import streamlit as st
from PIL import Image

st.set_page_config(page_title="Interactive Holographic Police Scenarios", layout="wide")
st.title("👮‍♂️ Holographic Police Visualization for Crime Deterrence")

# -----------------------
# Sidebar: Scenario Selection
# -----------------------
scenario = st.sidebar.selectbox(
    "Choose Scenario",
    [f"Scenario {i}" for i in range(1, 11)]
)

# Sliders for interactive settings
st.sidebar.header("Adjust Hologram Settings")
glow_intensity = st.sidebar.slider("Hologram Glow Intensity", 0.0, 1.0, 0.5)
torch_brightness = st.sidebar.slider("Torch Brightness", 0, 100, 70)
fog_density = st.sidebar.slider("Night Fog Density", 0, 100, 30)

# -----------------------
# Display Corresponding Image
# -----------------------
image_path = f"images/scenario{scenario.split()[-1]}.png"  # Load appropriate scenario image
img = Image.open(image_path)
st.image(img, caption=f"{scenario}: Holographic Police Officer", use_column_width=True)

# -----------------------
# Description Panel
# -----------------------
st.subheader("Scenario Details & Psychological Effect")
scenario_texts = [
    "Urban Park Night Patrol: Officer standing in dim park, torch lights path, creating vigilance perception.",
    "Busy Street Evening: Officer at street corner, watching pedestrians and traffic, promoting safety.",
    "School Playground Evening: Officer near playground, monitoring students leaving school.",
    "Subway Station Patrol: Officer near subway entrance, overseeing commuters for safety.",
    "Parking Lot Monitoring: Officer patrolling parking lot, torch illuminating cars to deter crime.",
    "Riverbank Night Observation: Officer near riverbank, torch reflecting on water, misty atmosphere.",
    "Urban Alleyway Patrol: Officer in narrow alley, torch casting light, monitoring potential threats.",
    "Public Park with Joggers: Officer observing joggers, torch lighting pathways, promoting safety.",
    "Shopping Mall Entrance: Officer at mall entrance, monitoring visitors, creating security presence.",
    "Bridge/Elevated Walkway: Officer overlooking pedestrians/vehicles, torch casting reflections, maintaining vigilance."
]
st.write(scenario_texts[int(scenario.split()[-1]) - 1])


