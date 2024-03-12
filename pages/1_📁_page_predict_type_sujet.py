import streamlit as st
import requests
import json
import os



'''
# JurisAI
'''

# st.set_page_config(
#     page_title="Search similar documents",
#     page_icon="📁",
# )
# text=st.text_input("Text to be analysed","Décret")

st.markdown('''
You can classify Moroccan legal documents that you have right here !
''')

fichier = open(os.path.join(os.getcwd(),'document_test','TypeArreteSujetSanteFrench0.txt'), "r")

text=fichier.read()
st.markdown(text)

fichier.close()

data = json.dumps(text).encode('utf-8')

url = "https://jurisaiimage-l6sefij74q-ew.a.run.app/predict"
response = requests.post(url, data=data, headers={ 'Content-Type': 'text/plain' })

prediction=response.json()
type = prediction['type']
subject = prediction['subject']


st.header(f'Tipe:{type}')
st.header(f'{subject}')
