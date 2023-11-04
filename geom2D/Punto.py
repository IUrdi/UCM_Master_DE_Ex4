from .vector import Vector
from typing import Self
#from geom2D import Vector
class Punto():
    def __init__(self,x:float,y:float):
        self._x=x
        self._y=y

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @x.setter
    def x(self,x) -> None:
        self._x=x

    @y.setter
    def y(self,y) -> None:
        self._y=y

    def __eq__(self, other: Self) -> bool:
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return f'P({self.x},{self.y})'

    def __str__(self) -> str:
        return f'({self.x},{self.y})'

    def __hash__(self):
        return hash((self.x,self.y))

    def __sub__(self,other: Self) -> Vector:
        return(Vector(self.x-other.x,self.y-other.y))

    def distance(self,other: Self)->float:
        return (self-other).mod

if __name__=='__main__':
    P1=Punto(5,1)
    P2=Punto(2,5)
    V=P1-P2
    print(V)
    print(P1.distance(P2))