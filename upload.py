import streamlit as st

st.title("Document Uploader")

uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "txt"])

# if uploaded_file is not None:
#     file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type}
#     st.write(file_details)

#     with open(uploaded_file.name, "wb") as f:
#         f.write(uploaded_file.getbuffer())
#     st.success("File successfully uploaded!")
