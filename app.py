import streamlit as st
from multiapp import MultiApp
from apps import welcome, checker,plaigrism, sentiment_analyze, translate, emotion, dummy

app = MultiApp()

st.markdown("""
#  Writing Assistant Application 

""")

# Add all your application here

app.add_app("Index", welcome.app)
app.add_app("Grammer and Spell Checker", checker.app)
app.add_app("Sentiment_Analyzer", sentiment_analyze.app)
app.add_app("Translator", translate.app)
app.add_app("Plaigrism_Checker", plaigrism.app)
app.add_app("Emotion Finder", emotion.app)
app.add_app("Spelling and grammer suggestions", dummy.app)

app.run()