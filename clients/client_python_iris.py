import requests

data = {
    "SepalLengthCm": 1.8,
    "SepalWidthCm": 2.6,
    "PetalLengthCm": 2.1,
    "PetalWidthCm": 3.5,
}
reponse = requests.post("http://127.0.0.1:5000/iris_species", json=data)
print(reponse.json())
