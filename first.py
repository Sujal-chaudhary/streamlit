import streamlit as st

sal = st.number_input('Enter your salary')
credit = st.number_input('Enter your credit score')

if sal > 50000 and credit > 700:
    st.write('You are eligible for a loan')
    st.balloons()