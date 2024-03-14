import streamlit as st
import requests


'''
# JurisAI
'''

st.markdown('''
You can classify Moroccan legal documents that you have right here !
''')

text=st.text_input("Contenu du document")


wagon_cab_api_url = 'https://taxifare.lewagon.ai/predict'
response = requests.get(wagon_cab_api_url, params=params)

prediction = response.json()

pred = prediction['fare']

st.header(f'Fare amount: ${round(pred, 2)}')
