import pickle
from flask import Flask, render_template, request
import re

app = Flask(__name__)

vector = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("dt_model.pkl", "rb"))



@app.route("/")
def home():
     return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    # Get form data
  if request.method == "POST":
    url = request.form.get("url")  # field name
    cleaned_url = re.sub(r'^https?://(www\.)?', '', url)  # Remove http:// or https://

    vect_data = vector.transform([cleaned_url])
    prediction = model.predict(vect_data)[0]

    if prediction == "good":
        prediction = " 🤳This URL is Legitimate."
    elif prediction == "bad":
       prediction = " 🤳This URL is Phishing. Please be cautious.!!"

    else:
        prediction = "Something went wrong!!. try again later"
    
  return render_template("index.html", result=prediction)



if __name__=="__main__":
    app.run(debug=True)


