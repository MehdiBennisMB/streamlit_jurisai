import streamlit as st
import requests
import json
import os
import pandas as pd

POSSIBLE_TYPES = ['Arrêté', 'Décret', 'Dahir', '-----', 'Loi', 'Décision', 'Rectificatif']

API_RETURN = [{'Date Greg': 'Date grégorienne: 25-08-1999',
  'Numero': 'Numéro: 1-99-211',
  'Sujet': 'Sujet: Civil',
  'Titre': 'Portant promulgation de la loi n° 64-99 relative au recouvrement des loyers.',
  'Type': 'Dahir',
  'text': "dû demander au président du tribunal de première instance compétent l'autorisation d'adresser une mise en demeure de paiement au locataire la demande n'est recevable que si elle est assortie de l'une des preuves visées à l'article premier article la mise en demeure doit sous peine d'irrecevabilité mentionner les noms des parties tels que portés sur les documents visés à l'article premier l'adresse du bailleur l'adresse du local donné à bail et le cas échéant le domicile ou le lieu de résidence du locataire le montant du loyer la durée de location impayée le total du montant du loyer dont le locataire est redevable le droit du bailleur à recourir à la procédure d'homologation de la mise en demeure en cas de non paiement dans les délais fixés article la mise en demeure fixe au locataire un délai d'au moins quinze jours pour s'acquitter des montants du loyer ce délai court à compter de la date de notification de la mise en demeure article le bailleur peut demander en cas de non paiement total ou partiel des montants du loyer fixés dans la mise en demeure au président du tribunal de première instance compétent d'homologuer la mise en demeure et d'ordonner"},
 {'Date Greg': 'Date grégorienne: 30-11-2007',
  'Numero': 'Numéro: 1-07-134',
  'Sujet': 'Sujet: Civil',
  'Titre': "portant promulgation de la loi n° 07-03 relative à la révision du montant du loyer des locaux à usage d'habitation ou à usage professionnel, commercial, industriel ou artisanal.",
  'Type': 'Loi',
  'text': "taux d'augmentation du loyer si son montant n'excède pas quatre cent dirhams par mois sans que le taux d'augmentation fixé par le tribunal soit supérieur à article conformément aux dispositions des articles et du dahir formant code des obligations et contrats le locataire peut demander la diminution du montant du loyer s'il survient des circonstances qui ont des répercussions sur l'usage pour lequel le local a été loué article le montant nouveau du loyer est applicable à compter de la date à partir de laquelle l'action en justice a été introduite si le bailleur demande la révision du loyer par voie de mise en demeure adressée au locataire le montant nouveau du loyer est applicable à compter de la date de réception par le locataire de cette mise en demeure à condition que le bailleur introduise une action en justice dans les trois mois qui suivent la date de réception de ladite mise en demeure par le locataire article le tribunal de première instance est compétent pour connaître des litiges concernant la révision et le recouvrement de l'augmentation du loyer que cette augmentation soit stipulée dans le contrat ou prévue par la législation en vigueur relative aux locaux visés à"}]

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
    # code here for the API returning a dataframe with similar documents
    # use variable text, option, and options to retrieve the relevant parameter values
    pass

    # display the results stored into a dataframe as a table in streamlit
    # simply add '[...]' at the beginning and end of the text
    # df_to_display = pd.DataFrame(API_RETURN)
    # df_to_display['text'] = '[...]' + df_to_display['text'].astype(str) + '[...]'
    # st.table(df_to_display)

    # display the results as one main line and another sub-line containing text
    for documents in API_RETURN:
        header_to_display = documents['Sujet'] + ' ----- ' + documents['Titre']
        st.header(header_to_display)
        st.text('[...]' + documents['text'] + '[...]')
