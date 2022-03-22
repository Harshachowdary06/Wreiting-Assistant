import streamlit as st
import nltk
import base64
from nltk.sentiment.vader import SentimentIntensityAnalyzer



def app():
  st.write("# Sentiment Analyzer")
  user_input = st.text_input("Please enter a statement to analyze sentiment")
  p=0
  n=0
  a=0
  if st.button("GO"):
    nltk.download("vader_lexicon")
    s = SentimentIntensityAnalyzer()
    score = s.polarity_scores(user_input)
    if score == 0:
          st.write("# ")
    elif score["neg"] != 0:
          st.write("# Negative")
    elif score["pos"] != 0:
          st.write("# Positive")
    else:
          st.write("# neutral")
  up_file = st.file_uploader(label="select your file",type=['csv','xlsx','txt'])
  if st.button("Check Files"):
    if up_file ==None:
        st.warning("Pleaes select file")
    else:
        nltk.download("vader_lexicon")
        s= SentimentIntensityAnalyzer()
        data = up_file.readlines()
        for i in data:
              a=a+1
              #st.write(i)
              #st.write(type(i))
              #temp = base64.b64decode(i)
              #st.write(temp)
              #temp = i.decode('UTF-8')
              score = s.polarity_scores(i)
              if score == 0:
                pass
              elif score["neg"] != 0:
                n=n+1
              elif score["pos"] != 0:
                p=p+1
        total_p = ((p)/(p+n))*100
        neu=a-(p+n)
        st.write("possitve rate:",total_p)
        st.write("# Total statements:",a)
        st.write("Total Possitive sentences:",p)
        st.write("Total Negative sentences:",n)
        st.write("Total Neutral sentences:",neu)
    
    

        
