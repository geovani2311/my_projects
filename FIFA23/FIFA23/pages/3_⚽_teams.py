import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Teams",
    page_icon="⚽",
    layout="wide"
)

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Time", clubes)

df_filtered = df_data[(df_data["Club"] == club)].set_index("Name")

st.image(df_filtered.iloc[0]["Club Logo"])
st.markdown(f"## {club}")

columns = ["Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Joined', 'Height(cm.)', 'Weight(lbs.)', 'Contract Valid Until', 'Release Clause(£)']

st.data_editor(
    df_data,
    column_config={
        "Overall": st.column_config.ProgressColumn(
            "Overall",
            format="%d",
            min_value=0,
            max_value=100,
        ),
        "Wage(£)": st.column_config.ProgressColumn(
            "Wage(£)",
            format="%d",
            min_value=0,
            max_value=df_filtered["Wage(£)"].max(),
        ),

        "Photo": st.column_config.ImageColumn(),
        "Flag" : st.column_config.ImageColumn("Count")
    }
)