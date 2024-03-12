import streamlit as st
import requests
import json
import os


'''
# JurisAI
'''

st.markdown('''
You can classify Moroccan legal documents that you have right here !
''')


text=st.text_input("Enter text to be looked for here","Décret")

option = st.radio('Select the database to search legal documents into:',
                  ['Textes fondamentaux',
                   'Documents classifiés'])

if option == 'Documents classifiés':
    options = st.multiselect(
        'Type de documents classifiés',
        ['Loi', 'Arrêt', 'Dahir', 'Décret'],
        ['Loi', 'Arrêt', 'Dahir', 'Décret'])
else :
    pass
