import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

if "data" not in st.session_state:
    df_data = pd.read_csv('CLEAN_FIFA23_official_data.csv', index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0 ]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

st.markdown("# FIFA 2023 OFFICIAL DATASET! ⚽")

st.sidebar.markdown("Developed by [Nicholas Loureiro]")

btn = st.button("Acess the dataset")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

st.markdown('''
    The Football Player Dataset spanning 2017 to 2023 encompasses extensive data
on professional football players. It covers a broad spectrum of features such as 
player demographics, physical traits, game statistics, contract specifics, and club memberships. 
Boasting more than 17,000 entries, this dataset is a rich resource for those in the football analysis domain, 
researchers, and aficionados keen on delving into different facets of the football realm. 
It facilitates the examination of player attributes, performance indicators, 
market values, club evaluations, player roles, and the progression of players over time.
            ''')