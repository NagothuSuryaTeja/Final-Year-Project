from flask import Flask, request, jsonify, render_template
from src.utils import load_object,DataCleaning


app = Flask(__name__)


def predict(text):

    vectorizer=load_object("./artifacts/tfidf_preprocessing_model.pkl")
    ie_model=load_object("./artifacts/model_ie.pkl")
    ns_model=load_object("./artifacts/model_ns.pkl")
    tf_model=load_object("./artifacts/model_tf.pkl")
    jp_model=load_object("./artifacts/model_jp.pkl")
    clean_text = DataCleaning()
    cleaned_text = clean_text.clean_text_advanced(text)
    X = vectorizer.transform([cleaned_text])
    ie = 'I' if ie_model.predict(X)[0] == 1 else 'E'
    ns = 'N' if ns_model.predict(X)[0] == 1 else 'S'
    tf = 'T' if tf_model.predict(X)[0] == 1 else 'F'
    jp = 'J' if jp_model.predict(X)[0] == 1 else 'P'

    result = ie + ns + tf + jp

    return result

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/response", methods=["GET", "POST"])
def response():

    if request.method == "POST":
        snippet = request.form["fsnippet"]
        # Testing with predict.py
        personality_type = predict(snippet)
    return render_template("response.html", name=personality_type, string=snippet)


@app.route("/analysis")
def analysis():
    return render_template("analysis.html")


@app.route("/methodology")
def methodology():
    return render_template("methodology.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
