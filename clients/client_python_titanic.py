import requests

data = {"pclass": 1, "sex": 0, "age": 21}
reponse = requests.post("http://127.0.0.1:5000/titanic_death", json=data)
print(reponse.json())
