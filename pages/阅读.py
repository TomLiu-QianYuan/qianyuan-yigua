import os
import streamlit as st
import base64
from pathlib import Path
import tempfile

if "pages" in os.getcwd():
    os.chdir("../")
if "书籍" in os.getcwd():
    os.chdir("../")
print(os.getcwd())


def read_pdf(file_path):
    # file = open(file_path, 'rb').read()
    if file_path is not None:
        # with open(file_path, "rb") as f:
        #     base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        # pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="800" height="1000" type="application/pdf">'
        # st.markdown(pdf_display, unsafe_allow_html=True)

        # # print(file)
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            fp = Path(tmp_file.name)
            fp.write_bytes(file)
            with open(tmp_file.name, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" ' \
                          f'width="800" height="1000" type="application/pdf">'
            st.markdown(pdf_display, unsafe_allow_html=True)

list_files = os.listdir("书籍")
file_to_read = st.selectbox("书籍选择", list_files)

if file_to_read in list_files:
    os.chdir("书籍")
    # data_2 = ''
    # for i in data.split('；'):
    #     data_2 += i + '；\n'
    if str(file_to_read).endswith(".txt"):
        data = open(file_to_read, 'r', encoding='utf-8').read()
        st.code(data)
    elif str(file_to_read).endswith(".md"):
        data = open(file_to_read, 'r', encoding='utf-8').read()
        st.markdown(data)
        # displayPDF(file_to_read)
    elif str(file_to_read).endswith(".pdf"):
        read_pdf(file_to_read)
    os.chdir("../")
