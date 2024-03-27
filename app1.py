import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image


st.title("CocinaFacil - Tu Asistente de Cocina Personalizado")
st.write(f"¡Hola Soy ChefIA, tu asistente de cocina personal. Con solo una foto de una receta, puedo convertirla en texto para que puedas escuchar las instrucciones mientras cocinas y así evitar cualquier accidente")
st.write(f"Toma una foto")
img_file_buffer = st.camera_input("Toma una Foto")

with st.sidebar:
      filtro = st.radio("Aplicar Filtro",('Con Filtro', 'Sin Filtro'))


if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    
    if filtro == 'Con Filtro':
         cv2_img=cv2.bitwise_not(cv2_img)
    else:
         cv2_img= cv2_img
    
        
    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    text=pytesseract.image_to_string(img_rgb)
    st.write(text) 
