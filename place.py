import streamlit as st
import requests
from geopy.geocoders import Nominatim

# Function to get place details
def get_place_details(place_name):
    geolocator = Nominatim(user_agent="place_details_app")
    location = geolocator.geocode(place_name)
    
    if location:
        return {
            "Address": location.address,
            "Latitude": location.latitude,
            "Longitude": location.longitude,
            "Location": location.raw
        }
    else:
        return None

# Streamlit UI
st.title("Place Details Finder")

place_name = st.text_input("Enter a place name:")

if st.button("Get Details"):
    if place_name:
        details = get_place_details(place_name)
        
        if details:
            st.subheader("Details of the Place:")
            for key, value in details.items():
                st.write(f"**{key}:** {value}")
        else:
            st.error("Place not found. Please try another name.")
    else:
        st.warning("Please enter a place name.")
