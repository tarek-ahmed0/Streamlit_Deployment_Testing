import streamlit as st
import pandas as pd
import numpy as np




st.title("Adventure Journey :violet[Recommendation]")
st.markdown("""
:gray[The Random Recommender delivers a tailored, spontaneous travel itinerary, featuring a curated selection of destinations and activities. Ideal for those seeking adventure, it offers a seamless, hassle-free travel experience, highlighting both hidden gems and popular attractions.]
            """)
st.header("", divider = 'violet')


col1, col2 = st.columns(2)
with col1 :
    members = st.slider("How Many :violet[**Members**] You Have In Journey", 1, 6)
    st.markdown(f"""Members : :violet[**{members}**]""")
with col2 :
    days = st.slider("How Many :violet[**Days**] Will You Stay", 1, 30)
    st.markdown(f"""Days : :violet[**{days}**]""")

st.subheader('Torists Journey Feedback')

chart_data = pd.DataFrame(np.random.randn(20, 3))
st.area_chart(chart_data)

with st.sidebar :
    st.header("Navigate Our Application")

