import streamlit as st
import pickle
import string
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

model = pickle.load(open('model.pkl','rb'))

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
            
    text = y[:]
    y.clear()
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
            
    text = y[:]
    y.clear()
    
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)


st.title("Email / SMS spam classifier")
input_sms = st.text_area("Enter Message")
if st.button("Predict"):
    transformed_text = transform_text(input_sms)

    result = model.predict([transformed_text])[0]
    if result == 1:
        st.header("Spam Messsage",)
    else:
        st.header("Not Spam / Ham Message")