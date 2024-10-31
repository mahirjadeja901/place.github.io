import streamlit as st
import pythreejs as p3js

def create_renderer():
    # Create a WebGLRenderer
    renderer = p3js.WebGLRenderer()
    # Set initial size
    renderer.setSize(800, 600)
    return renderer

def create_scene(renderer):
    # Create a scene and camera
    scene = p3js.Scene()
    camera = p3js.PerspectiveCamera(position=[0, 0, 5], aspect=800/600)

    # Example object (a simple cube)
    geometry = p3js.BoxGeometry()
    material = p3js.MeshBasicMaterial(color='blue')
    cube = p3js.Mesh(geometry=geometry, material=material)
    scene.add(cube)

    # Render the scene
    renderer.render(scene, camera)

    return scene, camera

# Streamlit UI
st.title("3D Scene with WebGLRenderer")

if st.button("Create 3D Scene"):
    renderer = create_renderer()
    scene, camera = create_scene(renderer)

    # Render the scene in the Streamlit app
    st.write(renderer.to_html())
