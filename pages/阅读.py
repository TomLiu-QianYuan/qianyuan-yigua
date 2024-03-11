import os
import streamlit as st

if "pages" in os.getcwd():
    os.chdir("../")
if "书籍" in os.getcwd():
    os.chdir("../")
print(os.getcwd())

list_files = os.listdir("书籍")
file_to_read = st.selectbox("书籍选择", list_files)

if file_to_read in list_files:
    os.chdir("书籍")
    data = open(file_to_read, 'r', encoding='utf-8').read()
    # data_2 = ''
    # for i in data.split('；'):
    #     data_2 += i + '；\n'
    os.chdir("../")
    st.code(data)
