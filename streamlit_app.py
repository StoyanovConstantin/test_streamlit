import streamlit as st
import csv


st.title('My new project 2025')
file = open(r"file.txt", 'r', encoding='UTF-8')
filerow = csv.reader(file)
for f in filerow:
    st.write(f)
file.close()