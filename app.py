pip install streamlit
import streamlit as st
st.title('Multiplication of 2 numbers')
a=st.number_input('Enter 1st number')
b=st.number_input('Enter 2nd number')
c=st.number_input('Enter 3rd number')
st.write("Max of numbers is =",max(a,b,c))
