# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 20:28:37 2023

@author: Anna & Filipa
"""

import json, os

STANDARDS_FILE = "data\standards.json"
PROBES_FILE = "data\probes.json"

# Funktion zum Laden der Standards aus einer JSON-Datei
def load_standards():
    if os.path.isfile(STANDARDS_FILE):
        with open(STANDARDS_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
    else:
        # Datensatz mit einem Element zurückgeben
        data = [{
            "Konzentration in mg/L": 0,
            "Extinktion": 0
            }]
    return data

# Funktion zum Speichern der Standards in einer JSON-Datei
def save_standards(data):
    with open(STANDARDS_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        
def load_probes():
    if os.path.isfile(PROBES_FILE):
        with open(PROBES_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
    else:
        # Datensatz mit einem Element zurückgeben
        data = [{
            "Extinktion": 0
            }]
    return data

# Funktion zum Speichern der Standards in einer JSON-Datei
def save_probes(data):
    with open(PROBES_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)