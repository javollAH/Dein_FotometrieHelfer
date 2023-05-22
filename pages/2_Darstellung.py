# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 12:30:05 2023

@author: Anna & Filipa
"""

import streamlit as st
import numpy as np
import pandas as pd
from Services import load_standards, load_probes

st.set_page_config(page_title="Darstellung", page_icon="📈")

st.markdown("# 📈 Darstellung")
st.write(
    """
    Darstellung der erfassten Daten
    """
)

# Lokale Daten vorbereiten
standards_list = load_standards()
probes_list = load_probes()

# und in Datenframes überführen
df_std = pd.DataFrame(standards_list)
df_prb = pd.DataFrame(probes_list)

# X- und Y- Achse als Array extrahieren
x_std = df_std['Konzentration in mg/L'].to_numpy()
y_std = df_std['Extinktion'].to_numpy()

# Mit Numpy ein Lin-Fit machen (polyfit 1-Grades)
m,b = np.polyfit(x_std, y_std, 1)

# Chart zeichnen (leider kann streamlit keine Dots zeichnen, zumindest nicht nativ)
chart = st.line_chart(df_std, 
                      x = 'Konzentration in mg/L', 
                      y = 'Extinktion',
                      use_container_width = True)

# Neues Datenframe mit Steigung und Offset erzeugen
df_meta = pd.DataFrame()
df_meta["Steigung m"] = [m]
df_meta["Offset b"] = [b]
st.dataframe(df_meta, use_container_width = True)

x_prb = []
y_prb = df_prb['Extinktion'].to_numpy()
for y in y_prb:
    # Für Debug-Zwecke
    # st.write(str(y) + ' - ' + str(b) + ' / ' + str(m))
    x_prb.append((y-b)/m)

df_prb['Konzentration in mg/L'] = x_prb

# In zwei nebeneinander liegende Bereiche teilen
col1, col2 = st.columns(2)
with col1:
    st.markdown("### Standards")
    st.dataframe(df_std,
                 use_container_width = True)
    
with col2:
    st.markdown("### Proben")
    st.dataframe(df_prb,
                 use_container_width = True)