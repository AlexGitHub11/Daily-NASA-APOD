import streamlit as st
import requests

api_key = "API_KEY"

url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

# get data from api into dict
request = requests.get(url)
content = request.json()

# Extract relevant info
title = content["title"]
img = content["url"]
explanation = content["explanation"]

# Download image
image_path = "img.png"
response = requests.get(img)
with open(image_path, "wb") as file:
    file.write(response.content)


st.title(title)
st.image(image_path)
st.text(explanation)

