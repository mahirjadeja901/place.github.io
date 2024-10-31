import streamlit as st
import pythreejs as p3js

def create_3d_text(name, color):
    # Create a scene
    scene = p3js.Scene()
    
    # Create a camera
    camera = p3js.PerspectiveCamera(position=[0, 0, 5], aspect=1)
    
    # Create a renderer
    renderer = p3js.WebGLRenderer()
    
    # Set the size of the renderer
    renderer.setSize(width=800, height=600)

    # Create text geometry
    text_geometry = p3js.TextGeometry(
        text=name,
        parameters={
            'font': p3js.FontLoader().load('https://threejs.org/fonts/helvetiker_regular.typeface.json'),
            'size': 1,
            'height': 0.1,
            'curveSegments': 12,
        }
    )
    
    # Create a material with the desired color
    text_material = p3js.MeshBasicMaterial(color=color)
    
    # Create a mesh with the geometry and material
    text_mesh = p3js.Mesh(geometry=text_geometry, material=text_material)
    
    # Add the mesh to the scene
    scene.add(text_mesh)

    # Return the renderer and scene
    return renderer, scene, camera

# Streamlit UI
st.title("3D Name Generator")

name = st.text_input("Enter your name:")
color = st.color_picker("Choose a color:", "#FF5733")

if st.button("Generate 3D Name"):
    if name:
        renderer, scene, camera = create_3d_text(name, color)
        
        # Render the scene
        st.write(renderer.to_html())
    else:
        st.warning("Please enter a name.")
