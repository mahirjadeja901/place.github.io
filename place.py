import streamlit as st
import time

# Set the title of the app
st.title("🎆 Diwali Celebration with Fireworks 🎆")

# Add a description
st.write("Welcome to the Diwali celebration! Let's enjoy the fireworks!")

# Create a button to start the fireworks animation
if st.button("Light the Fireworks!"):
    # Show a loading spinner while the fireworks are being displayed
    with st.spinner("Lighting the fireworks..."):
        time.sleep(2)  # Simulate a delay for effect
        st.balloons()  # Display balloons as a representation of fireworks
        st.success("Happy Diwali! 🎉")  # Show a success message

# Add some festive decorations
st.markdown("""
    <style>
    .stApp {
        background-color: #ffe6e6;  /* A light pink background for a festive feel */
    }
    </style>
""", unsafe_allow_html=True)

# Add a festive image (replace with a valid image URL)
st.image("https://your-image-url.com/path_to_your_diwali_image.jpg", caption="Happy Diwali!", use_column_width=True)

# Add a closing message
st.write("Thank you for celebrating Diwali with us!")
