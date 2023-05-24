# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 11:07:53 2023

@author: Anna & Filipa
"""

import streamlit as st
import pandas as pd
from jsonbin import load_key, save_key
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

st.set_page_config(
    page_title="Fotometrie-Helfer",
    page_icon="👋",
)

# -------- load secrets for jsonbin.io --------
jsonbin_secrets = st.secrets["jsonbin"]
api_key = jsonbin_secrets["api_key"]
bin_id = jsonbin_secrets["bin_id"]

# -------- user login --------
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
)

fullname, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status == True:   # login successful
    authenticator.logout('Logout', 'main')   # show logout button
elif authentication_status == False:
    st.error('Username/password is incorrect')
    st.stop()
elif authentication_status == None:
    st.warning('Please enter your username and password')
    st.stop()

data = load_key(api_key, bin_id, username)

st.write (data)


st.write("# 👋 Fotometrie-Helfer!")

st.sidebar.success("Bereit...")

st.markdown(
    """
    ## Fotometrie — das Wichtigste
    - Die Photometrie ist ein Messverfahren zur Konzentrationsbestimmung von gelösten Substanzen durch Messung ihrer Transmission.
    - Über Messung der Transmission kann die Extinktion bestimmt werden.
    - Die Extinktion umfasst die folgenden lichtschwächenden Prozesse: Absorption, Reflexion und Brechung.
    - Das Messgerät zur photometrischen Messung ist ein Photometer. 
    - Die Eigenschaften des Photometers sind der geringe Zeitaufwand und seine hohe Präzision.
    
    👈 Bitte in der Sidebar Dateneingabe oder Datendarstellung wählen!

    ### Willst du mehr über Fotometrie wissen?
    - Check out [studyflix.de](https://studyflix.de/chemie/photometrie-5394)
    - Check out [wikipedia.org](https://de.wikipedia.org/wiki/Photometrie) 

    ### Diese App wurde mit streamlit ermöglicht
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
"""
)
