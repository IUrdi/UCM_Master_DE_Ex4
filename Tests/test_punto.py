from geom2D import Punto,Vector
import pytest

def test_punto_hash():
    spunto={Punto(1,0),Punto(0,1),Punto(0,0)}
    assert Punto(1.0,0.0)==Punto(1,0)
    assert Punto(1.0,0.0) in spunto
    assert Punto(0,1.0)  ==Punto(0,1)
    assert Punto(0,1.0) in spunto

@pytest.mark.parametrize(
    "P1,P2,V",[
        (Punto(0,0),Punto(0,3),Vector(0,-3)),
        (Punto(3,0),Punto(0,4),Punto(3,-4))
        ]
)
def test_punto_sub(P1: Punto,P2: Punto,V: Vector):
    assert (P1-P2)==V

@pytest.mark.parametrize(
    "P1,P2,dist",[
        (Punto(0,0),Punto(0,3),3),
        (Punto(3,0),Punto(0,4),5)
        ]
)
def test_punto_distance(P1: Punto,P2: Punto,dist):
    assert P1.distance(P2)==dist