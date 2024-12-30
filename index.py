from flask import Flask, render_template, jsonify, request
import pickle
import numpy as np

app = Flask(__name__)
model_titanic = pickle.load(
    open("./models/model_titanic_nom.pkl", "rb")
)  # loading the trained model
model_iris = pickle.load(open("./models/model_iris_nom.pkl", "rb"))


####### Avec interface ########


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/page_iris")
def iris():
    return render_template("predict_iris.html")


@app.route("/page_titanic")
def titanic():
    return render_template("predict_titanic.html")


@app.route("/predict_iris", methods=["POST"])
def predict_iris():
    """
    For rendering results on HTML GUI
    """

    # retrieving values from form
    init_features = [float(x) for x in request.form.values()]
    final_features = [np.array(init_features)]

    prediction = model_iris.predict(final_features)  # making prediction

    return render_template(
        "predict_iris.html", prediction_text="Predicted Class: {}".format(prediction)
    )  # rendering the predicted result


@app.route("/predict_titanic", methods=["POST"])
def predict_titanic():
    """
    For rendering results on HTML GUI
    """

    # retrieving values from form
    features = [[int(x) for x in request.form.values()]]
    prediction = model_titanic.predict(features)  # making prediction

    return render_template(
        "predict_titanic.html", prediction_text="Predicted Class: {}".format(prediction)
    )  # rendering the predicted result


####### Sans interface ########


@app.route("/titanic_death", methods=["POST"])
def predict_death():
    features = request.get_json()
    X = [[features["pclass"], features["sex"], features["age"]]]
    prediction = model_titanic.predict(X)

    return jsonify(prediction[0])


@app.route("/iris_species", methods=["POST"])
def predict_species():
    features = request.get_json()
    X = [
        [
            features["SepalLengthCm"],
            features["SepalWidthCm"],
            features["PetalLengthCm"],
            features["PetalWidthCm"],
        ]
    ]
    prediction = model_iris.predict(X)

    return jsonify(prediction[0])


if __name__ == "__main__":
    app.run("0.0.0.0")
