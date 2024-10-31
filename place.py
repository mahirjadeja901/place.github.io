import streamlit as st
import requests

st.title("Place Information Finder")

# User input for place name
place_name = st.text_input("Enter the name of a place:")

if st.button("Get Details"):
    if place_name:
        # Nominatim API to fetch place details
        url = f"https://nominatim.openstreetmap.org/search?q={place_name}&format=json&addressdetails=1&limit=1"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data:
                place_info = data[0]
                
                st.write("### Place Details:")
                st.write(f"**Name:** {place_info.get('display_name')}")
                st.write(f"**Latitude:** {place_info.get('lat')}")
                st.write(f"**Longitude:** {place_info.get('lon')}")
                
                if 'address' in place_info:
                    st.write("**Address Details:**")
                    for key, value in place_info['address'].items():
                        st.write(f"{key.capitalize()}: {value}")
            else:
                st.error("No details found for the given place.")
        else:
            st.error("Error fetching data from the API.")
    else:
        st.warning("Please enter a place name.")
