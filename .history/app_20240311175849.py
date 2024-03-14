import streamlit as st
import requests


'''
# JurisAI
'''

st.markdown('''
You can classify Moroccan legal documents that you have right here !
''')

text=st.text_input("Contenu du document")





url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':
    '''
    You can make the prediction right there
    '''
