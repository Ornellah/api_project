from ipynb.fs.full.model_titanic import *

def test_entree_survie():
    p_class = 2
    sex  = 0
    age = 21
    result = np.array([p_class,sex,age]).reshape(1,3)
    assert isinstance(result, np.ndarray)
    

def test_sortie_survie():
    p_class = 2
    sex  = 0
    age = 21
    x=np.array([p_class,sex,age]).reshape(1,3)
    result = model.predict(x)
    assert result == 'Survivant' or result == 'Mort'
    