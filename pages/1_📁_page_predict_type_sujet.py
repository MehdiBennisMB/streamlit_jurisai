import streamlit as st
import requests
import json
import os
from io import StringIO

'''
# JurisAI
'''

# st.set_page_config(
#     page_title="Search similar documents",
#     page_icon="📁",
# )
# text=st.text_input("Text to be analysed","Décret")






uploaded_file = st.file_uploader("Choose a file")
print(uploaded_file)
if uploaded_file is not None:
    # print(uploaded_file)
    bytes_data = uploaded_file.getvalue()
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write("You selected the file:", uploaded_file.name)
    # uploaded_file.read()
    text = stringio.read()
    st.markdown(text)
    data = json.dumps(text).encode('utf-8')
    url = "https://jurisaiimage-l6sefij74q-ew.a.run.app/predict"
    response = requests.post(url, data=data, headers={ 'Content-Type': 'text/plain' })
    prediction=response.json()
    type = prediction['type']
    subject = prediction['subject']

    st.header(f'Type: {type}')
    st.header(f'{subject}')


# fichier = open(os.path.join(os.getcwd(),'document_test',filename), "r")
# text=fichier.read()
# fichier.close()

# data = json.dumps(text).encode('utf-8')
