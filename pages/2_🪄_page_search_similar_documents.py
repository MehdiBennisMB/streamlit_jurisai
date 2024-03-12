import streamlit as st
import requests
import json
import os

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

if option == 'Documents classifiés':
    options = st.multiselect(
        'Type de documents classifiés',
        POSSIBLE_TYPES,
        POSSIBLE_TYPES)
else :
    #nothing to be done
    pass

if st.button('Search similar documents'):
    #code here for the API returning a dataframe with similar documents
    # use variable text, option, and options to retrieve the relevant parameter values
    pass
