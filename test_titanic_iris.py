import requests

def test_sortie_titanic():
    data = {
        'pclass':1,
        'sex': 0,
        'age':21
    }
    reponse = requests.post('http://127.0.0.1:5000/titanic_death', json=data)
    assert reponse.json() == 'Survivant' or reponse.json() == 'Mort'
    
    
def test_sortie_iris():
    data = {
        'SepalLengthCm':1.8,
        'SepalWidthCm': 2.6,
        'PetalLengthCm':2.1,
        'PetalWidthCm':3.5
    }
    reponse = requests.post('http://127.0.0.1:5000/iris_species', json=data)
    reponse = reponse.json()
    assert reponse.find('Iris') != -1