import streamlit as st
from difflib import SequenceMatcher

def app():
  st.write("# Plaigrism Checker")
  input = st.text_area("Please enter a statement to assist")
  if st.button("GO"):
        if input=='':
            st.warning("Pleaes give a sentence")
        else:
            with open('apps/datasets/source.txt') as source:
                file1_data = source.read()
                similarity = SequenceMatcher(None, file1_data, input).ratio()
                st.warning(f"The contents are {similarity*100}% common.")
            
  up_file = st.file_uploader(label="select your file",type=['csv','xlsx','txt'])
  if st.button("Check plaigrism"):
        if up_file ==None:
            st.warning("Pleaes select file ")
        else:
            pass
  