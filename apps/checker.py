# imports
import streamlit as st
import nltk
from gramformer import Gramformer
from textblob import TextBlob


#  loading data sets

gf = Gramformer(models=1, use_gpu=False)

# running application
def app():
    
    st.title('Grammar & Spell Checker In Python')
    st.warning("server under maintanace")
    
# input
    text = st.text_area("Enter Text:", value='', height=None, max_chars=None, key=None)
    
    #working
    if st.button('Correct Sentence'):
        if text == '':
            st.write('Please enter text for checking')
        else:
            new_text = gf.correct(text)
            new_text = ', '.join(new_text)
            tb= TextBlob(new_text)
            out=tb.correct()
            st.write(out)
    else: pass