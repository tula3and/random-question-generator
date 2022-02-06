import streamlit as st
from qrng import random_number

st.write("""
        # Random Question Generator
        질문을 추천해드려요!
        """)

num = random_number()

st.write(num)

