import streamlit as st
import requests


'''
# JurisAI
'''

st.markdown('''
You can classify Moroccan legal documents that you have right here !
''')

text=st.text_input("Contenu du document")


url = "https://jurisai-ubyqget7zq-oa.a.run.app/predict"
response = requests.post(url, data=text, headers={ 'Content-Type': 'text/plain' })
response.json()
pred = prediction['fare']

st.header(f'Fare amount: ${round(pred, 2)}')
