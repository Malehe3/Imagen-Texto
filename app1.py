import streamlit as st
import os

# Ensure the 'temp' directory exists
if not os.path.exists("temp"):
    os.makedirs("temp")

def text_to_speech(text, tld):
    tts = gTTS(text, "es", tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    save_path = os.path.join("temp", f"{my_file_name}.mp3")  # Construct the file path
    tts.save(save_path)
    return my_file_name, text

if st.button("Convertir texto a audio"):
    result, output_text = text_to_speech(text, "es")
    audio_path = os.path.join("temp", f"{result}.mp3")  # Construct the file path
    if os.path.exists(audio_path):  # Check if the file exists before attempting to read it
        audio_file = open(audio_path, "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3", start_time=0)
        st.markdown("## Texto en audio:")
        st.write(output_text)
    else:
        st.write("¡Ups! Parece que hubo un error al generar el archivo de audio.")

# Remove files older than 7 days
def remove_files(n):
    mp3_files = glob.glob("temp/*.mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.path.isfile(f) and os.stat(f).st_mtime < now - n_days:
                os.remove(f)

remove_files(7)

