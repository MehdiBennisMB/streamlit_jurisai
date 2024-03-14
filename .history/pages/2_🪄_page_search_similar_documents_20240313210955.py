import streamlit as st
import requests
import json
import os
import pandas as pd

POSSIBLE_TYPES = ['Arrêté', 'Décret', 'Dahir', '-----', 'Loi', 'Décision', 'Rectificatif']

st.set_page_config(
    page_title="Search similar documents",
    page_icon="🪄",
)
'''
# JurisAI
'''

st.markdown('''
You can classify Moroccan legal documents that you have right here !
''')

text=st.text_input("Enter text to be looked for below","Décret")

option = st.radio('Select database to search legal documents into:',
                  ['Textes fondamentaux',
                   'Documents classifiés'])

data = json.dumps(text).encode('utf-8')

url = "https://jurisaiimage-l6sefij74q-ew.a.run.app/semantic"

params={"question":text,"source":option}
response = requests.get(url, params=params)

prediction=response.json()
type = prediction['type']
subject = prediction['subject']

if option == 'Documents classifiés':
    options = st.multiselect(
        'Type de documents classifiés',
        POSSIBLE_TYPES,
        POSSIBLE_TYPES)
else :
    #nothing to be done
    pass

if st.button('Look for similar documents'):
    # code here for the API returning a dataframe with similar documents
    # use variable text, option, and options to retrieve the relevant parameter values
    pass

    # display the results as 2 main lines and a rectangle containing text
    for documents in API_RETURN:
        type = documents['Type']
        subject = documents['Sujet']
        display_text = documents['text']
        st.header(f'Type: {type}')
        st.header(f'{subject}')

        hauteur_affichage = 400  # nb of pixels
        st.markdown(f"""
            <div style="border: 2px solid #d3d3d3; border-radius: 5px; padding: 10px; font-size: 25px;
                        height: {hauteur_affichage}px; overflow-y: scroll; background-color: #f9f9f9;">
                {display_text}
            </div>
        """, unsafe_allow_html=True)
