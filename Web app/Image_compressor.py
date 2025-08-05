import streamlit as st
from Image_Compression_mod import run_kMeans
import numpy as np
from PIL import Image
import io

col1,col2 = st.columns([1,1])
with col1:
    K = st.slider(f'Number of colors',min_value = 4,max_value = 128,step = 4)
    iter = st.slider(f'Number of iterations',min_value = 8,max_value = 20,step = 1)
file = st.file_uploader(f'Upload image to compress',type = ['png','jpg','jpeg'])
with col1:
    fmt = st.selectbox(f'Select output format',['.png','.jpeg','.jpg'],index = 1)
if st.button('Compress',disabled = not file):
    if file:
        img = Image.open(file)
        img = np.array(img)
        
        if len(img.shape) == 2:
            img = np.expand_dims(img,axis = -1)
            m,n,c = img.shape
        else:
            m,n,c = img.shape

        if m*n > 1000000000:
            st.warning('Uploaded image is too large!')
        else:
            with st.spinner("Please wait..."):
                comp_img = run_kMeans(img,K,iter)
            st.image(comp_img)
            comp_img = Image.fromarray((comp_img*255).astype(np.uint8))
            buf = io.BytesIO()
            comp_img.save(buf,format = 'JPEG')
            img_byte = buf.getvalue()
            compressed_size_bytes = len(img_byte)
            compressed_size_kb = compressed_size_bytes / 1024
            st.write(f"Compressed Image Size: {compressed_size_kb:.2f} KB")
            st.download_button(
                label = 'Download',
                data = img_byte,
                file_name = f"compressed_{file.name}{fmt}"
            )

        