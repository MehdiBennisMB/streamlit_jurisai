import streamlit as st
import requests


'''
# JurisAI
'''

st.markdown('''
You can classify Moroccan legal documents that you have right here !
''')

text=st.text_input("Contenu du document","Decret")


url = "https://jurisaiimage-l6sefij74q-ew.a.run.app/predict"
response = requests.post(url, data=text, headers={ 'Content-Type': 'text/plain' })

prediction=response.json()
type = prediction['type']
subject = prediction['subject']


st.header(f'Tipe:{type}')
st.header(f'Sujet:{subject}')
