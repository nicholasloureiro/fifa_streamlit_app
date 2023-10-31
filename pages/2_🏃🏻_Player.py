import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Players",
    page_icon="🏃🏻",
    layout="wide"
)

df_data = st.session_state["data"]

clubs = pd.unique(df_data["Club"])
club = st.sidebar.selectbox("Club", clubs)

df_players = df_data[(df_data["Club"] == club)]
players = pd.unique(df_players["Name"])
player = st.sidebar.selectbox("Player", players)

player_stats = df_data[df_data["Name"] == player].iloc[0]

st.image(player_stats["Photo"])
st.title(player_stats["Name"])

st.markdown(f"**Club:** {player_stats['Club']}")
st.markdown(f"**Position:** {player_stats['Position']}")


col1, col2, col3, col4 = st.columns(4)

col1.markdown(f"**Age:** {player_stats['Age']}")
col2.markdown(f"**Height:** {player_stats['Height(cm.)'] / 100} m")
col3.markdown(f"**Weight:** {player_stats['Weight(lbs.)'] / 2.2:.1f} kg")

st.divider()

st.subheader(f"**Overall** {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))


col5, col6, col7, col8 = st.columns(4)

col5.metric(label="Value: ",value=f"{player_stats['Value(£)']:,}")
col6.metric(label ="Wage: ",value=f"{player_stats['Wage(£)']:,}")
col7.metric(label="Preferred Foot: ",value=f"{player_stats['Preferred Foot']}")