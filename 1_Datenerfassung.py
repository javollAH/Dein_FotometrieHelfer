# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 12:30:05 2023

@author: Anna & Filipa
"""

import streamlit as st
from Services import load_standards, save_standards, load_probes, save_probes

# Seite darstellen
st.set_page_config(page_title="Datenerfassung", page_icon="📊")
st.markdown("# 📊 Datenerfassung")
st.write(
    """
    Auf dieser Seite können die Daten erfasst werden.
    """
)

# Lokale Daten vorbereiten
standards_list = load_standards()
probes_list = load_probes()

# Sidebar aufbauen (Hilfe zur Bedienung)
st.sidebar.title("Bedienung beim Bearbeiten")
st.sidebar.header("Hinzufügen")
st.sidebar.markdown("Plus auf der letzten Zeile klicken")
st.sidebar.header("Ändern")
st.sidebar.markdown("Zeile markieren und Werte anpassen")
st.sidebar.header("Entfernen")
st.sidebar.markdown("Eine oder mehrere Zeilen markieren und Taste *del* drücken")

# Weiter mit Seiteninhalt...
function_radio = st.radio("Funktion", 
                          ('Anzeigen', 'Bearbeiten'), 
                          label_visibility='hidden',
                          horizontal=True)
# Leere Zeile
st.write("")

# In zwei nebeneinander liegende Bereiche teilen
col1, col2 = st.columns(2)
with col1:
    st.markdown("### Standards")
with col2:
    st.markdown("### Proben")

if function_radio == 'Anzeigen':
    with col1:
        standards_list = st.dataframe(data = standards_list, 
                                      use_container_width = True)
    
    with col2:
        probes_list = st.dataframe(data = probes_list, 
                                   use_container_width = True)
else:
    with col1:
        standards_list_edit = st.experimental_data_editor(data = standards_list, 
                                                          use_container_width = True,
                                                          num_rows="dynamic")

    with col2:
        probes_list_edit = st.experimental_data_editor(data = probes_list, 
                                                       use_container_width = True,
                                                       num_rows="dynamic")

    save_button = st.button("Daten speichern")
    
    if save_button == True:
        save_standards(standards_list_edit)
        save_probes(probes_list_edit)