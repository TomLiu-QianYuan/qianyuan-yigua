import os
import streamlit as st
import base64

if "pages" in os.getcwd():
    os.chdir("../")
if "书籍" in os.getcwd():
    os.chdir("../")
print(os.getcwd())


def displayPDF(file):
    # Opening file from file path
    with open(file, "rb", encoding='gbk') as f:
        base64_pdf = base64.b64encode(f.read()).decode('gbk')

    # Embedding PDF in HTML
    pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)


list_files = os.listdir("书籍")
file_to_read = st.selectbox("书籍选择", list_files)

if file_to_read in list_files:
    os.chdir("书籍")
    data = open(file_to_read, 'r', encoding='utf-8').read()
    # data_2 = ''
    # for i in data.split('；'):
    #     data_2 += i + '；\n'
    os.chdir("../")
    if str(file_to_read).endswith(".txt"):
        st.code(data)
    elif str(file_to_read).endswith(".md"):
        st.markdown(data)
        # displayPDF(file_to_read)
