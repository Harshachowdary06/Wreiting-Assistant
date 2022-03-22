import streamlit as st
from deep_translator import GoogleTranslator
def app():
    st.write("# Translator")
    #langs_list = GoogleTranslator.get_supported_languages()
    input1 = st.text_area("Enter Text")
    langinput =st.text_input("Enter target language code")
    if st.button("GO"):
        translated = GoogleTranslator(source='auto', target=langinput).translate(input1) 
        st.write(translated)
    up_file = st.file_uploader(label="select your file",type=['csv','xlsx','txt'])
    langinput2 =st.text_input("Enter target language code for file")
    if st.button("Translate File"):
        if up_file ==None or langinput2=='':
            st.warning("Pleaes select file and language code")
        else:
            data = up_file.readlines()
            for i in data:
              #temp = i.decode('UTF-8')
              temp2 = GoogleTranslator(source='auto', target=langinput2).translate(i) 
              st.write(i+":"+temp2)