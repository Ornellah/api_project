from ipynb.fs.full.model_titanic import *

def test_survie():
    p_class = 2
    sex  = 0
    age = 21
    x=np.array([p_class,sex,age]).reshape(1,3)
    assert isinstance(x, np.ndarray)
    
    