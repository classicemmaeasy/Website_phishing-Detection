import pickle
import re
import streamlit as st

# Load vectorizer and model
vector = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("dt_model.pkl", "rb"))

# Streamlit app
st.set_page_config(page_title="Website Phishing Detection", page_icon="🌐", layout="centered")

st.title("🌐 Website Phishing Detection")
st.write("Enter a website URL below to check if it is legitimate or phishing.")

# Input field
url = st.text_input("Enter URL (e.g., https://example.com)")

if st.button("Check URL"):
    if url.strip() == "":
        st.warning("Please enter a URL.")
    else:
        # Clean the URL
        cleaned_url = re.sub(r'^https?://(www\.)?', '', url.strip())

        # Transform & predict
        vect_data = vector.transform([cleaned_url])
        prediction = model.predict(vect_data)[0]

        # Display result
        if prediction == "good":
            st.success("✅ This URL is Legitimate.")
        elif prediction == "bad":
            st.error("⚠️ This URL is Phishing. Please be cautious!")
        else:
            st.warning("Something went wrong! Try again later.")
