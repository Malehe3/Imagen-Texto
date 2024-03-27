import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image
import os
from gtts import gTTS

# Función para convertir texto a audio
def text_to_speech(text, tld):
    # Verificar si el directorio "temp" existe, si no existe, crearlo
    if not os.path.exists("temp"):
        os.makedirs("temp")
    
    # Generar archivo de audio
    tts = gTTS(text, "es", tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, text

# Tomar una foto y procesarla
st.write("Toma una foto")
img_file_buffer = st.file_uploader("Selecciona una imagen", type=["jpg", "jpeg", "png"])

# Si se selecciona una imagen
if img_file_buffer is not None:
    # Convertir imagen a texto usando OCR (reconocimiento óptico de caracteres)
    img = Image.open(img_file_buffer)
    text = pytesseract.image_to_string(img, lang='spa')
    st.write("Texto obtenido de la imagen:")
    st.write(text) 

    # Convertir texto a audio
    if st.button("Convertir texto a audio"):
        result, output_text = text_to_speech(text, "es")
        audio_file = open(f"temp/{result}.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3", start_time=0)
        st.markdown("## Texto en audio:")
        st.write(output_text)

    


