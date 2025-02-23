import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO

st.title('Aplicación para remover fondo')

imagen = st.file_uploader('Sube tu imagen:', type=['jpeg', 'png', 'jpg'])  #archivo binario

if imagen is not None:
    col1, col2 = st.columns(2)
    with col1 :
        st.image(imagen)
    with col2: 
        input_data = imagen.read()  #lo lees como bytes
        output_data = remove(input_data)  #recibe bytes y devulve bytes
        st.image(output_data)  
    
    col1, col2, col3 =st.columns(3)
    with col3:
        st.download_button('Descargar', 
                    data = output_data, 
                    file_name= 'imagen_procesada.jpg',
                    mime='image/png')
    
    