import streamlit as st
import pickle
import re
import nltk
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import string
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

def transform_text(text):
    tokens = re.findall(r'\b\w+\b', text)
    y = []
    for i in tokens:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()
    for i in text:
        if i not in ENGLISH_STOP_WORDS and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)



tf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title("E-Mail/SMS Classifier")
input_sms = st.text_area("Message",height = 180,placeholder = "Enter Message Here...")

if st.button("Predict"):
    #1. transform
    transformed_sms = transform_text(input_sms)

    #2. vectorize
    vector_input = tf.transform([transformed_sms])

    #3. predict
    result = model.predict(vector_input)[0]

    #4. display
    if result == 1:
        st.header("this message is classified as Spam.")
    else:
        st.header("this message is Not classified as Spam.")

st.markdown("___")
st.caption("Project is build using Streamlit,Scikit-learn,NLP")