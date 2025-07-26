import streamlit as st
import pandas as pd
import sqlite3

def load_data():
    conn = sqlite3.connect("data/predictions.db")
    df = pd.read_sql_query("SELECT * FROM logs ORDER BY timestamp DESC", conn)
    conn.close()
    return df

st.set_page_config(page_title="MLOps Dashboard", layout="wide")
st.title("MLOps Monitoring Dashboard")

df = load_data()

if df.empty:
    st.warning("No predictions logged")
else:
    st.subheader(" Recent Predictions")
    st.dataframe(df)

    st.subheader("Prediction Class ")
    st.bar_chart(df["prediction"].value_counts())

    st.subheader("Activity Over Time")
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.set_index('timestamp', inplace=True)
    st.line_chart(df.resample('1min').size())
