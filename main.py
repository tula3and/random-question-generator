import streamlit as st
from qrng import random_number
import csv
import time

# set page title and icon
st.set_page_config(page_title="Random Questions", page_icon="🐈", layout="centered")
st.title("🐈 Random Questions!")
st.caption("You know what? Random numbers used in this page are from Hadamard gates in Qiskit!")

# welcome balloons
st.balloons()

# set a default language option
option = st.selectbox(
        'Choose language first',
        ('한국어', 'English', 'Arabic', 'Japanese'))

if option == '한국어':
    language = 0
elif option == 'English':
    language = 1
elif option == 'Arabic':
    language = 2
else:
    language = 3

# choose one number from 0 to 31
num = random_number()

# read questions for a csv file
f = open('questions.csv', 'r', encoding="UTF-8")
rdr = csv.reader(f)

# count the number of questions
cnt = -1
questions = []
for line in rdr:
    cnt += 1
    if (cnt == 0 or len(line) == 0): continue
    questions.append(line)

f.close()

# pick another number
if st.button('New Question!'):
    num = random_number()

with st.spinner('Cats are running around...'):
    time.sleep(1)

# print selected question
st.success(questions[num % cnt][language])
