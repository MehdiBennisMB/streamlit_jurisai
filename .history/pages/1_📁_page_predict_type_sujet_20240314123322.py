import streamlit as st
import requests
import json
import os
from io import StringIO

'''
# JurisAI - Smart Classifier
'''

# st.set_page_config(
#     page_title="Search similar documents",
#     page_icon="📁",
# )
# text=st.text_input("Text to be analysed","Décret")

MAX_CHAR=1000

uploaded_file = st.file_uploader("Choose a file")
print(uploaded_file)
if uploaded_file is not None:

    # print(uploaded_file)
    bytes_data = uploaded_file.getvalue()
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

    # uploaded_file.read()
    text = stringio.read()
    display_text=text

    data = json.dumps(text).encode('utf-8')
    url = "https://jurisaiimage-l6sefij74q-ew.a.run.app/predict"
    response = requests.post(url, data=data, headers={ 'Content-Type': 'text/plain' })
    print(response)
    prediction=response.json()
    type = prediction['type']
    subject = prediction['subject']

    st.header(f'Type: {type}')
    st.header(f'Topic: {subject}')

    hauteur_affichage = 400  # nb of pixels
    st.markdown(f"""
        <div style="border: 2px solid #d3d3d3; border-radius: 5px; padding: 10px; font-size: 25px;
                    height: {hauteur_affichage}px; overflow-y: scroll; background-color: #f9f9f9;">
            {display_text}
        </div>
    """, unsafe_allow_html=True)
# fichier = open(os.path.join(os.getcwd(),'document_test',filename), "r")
# text=fichier.read()
# fichier.close()

# data = json.dumps(text).encode('utf-8')
