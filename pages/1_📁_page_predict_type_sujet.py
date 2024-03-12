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

button1=st.button(label='Load document')

def save_uploaded_file(uploaded_file):
  with open(os.path.join(os.getcwd(),'document_test'),"wb") as f:
     f.write(uploaded_file.getbuffer())
  return st.success("Saved file :{} ".format(uploaded_file.name))

if button1:
    datafile = st.file_uploader("Upload text",type=['txt'])
    if datafile is not None:
        file_details = {"FileName":datafile.name,"FileType":datafile.type}
        save_uploaded_file(datafile)



st.markdown('''
You can classify Moroccan legal documents that you have right here !
''')


def file_selector(folder_path=os.path.join(os.getcwd(),'document_test')):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    file_path=os.path.join(folder_path, selected_filename)
    return file_path


filename=file_selector()
fichier = open(os.path.join(os.getcwd(),'document_test',filename), "r")
text=fichier.read()
fichier.close()

data = json.dumps(text).encode('utf-8')

url = "https://jurisaiimage-l6sefij74q-ew.a.run.app/predict"
response = requests.post(url, data=data, headers={ 'Content-Type': 'text/plain' })

prediction=response.json()
type = prediction['type']
subject = prediction['subject']

st.header(f'Tipe:{type}')
st.header(f'{subject}')
