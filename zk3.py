# Příklad 3: Základy OOP (dědičnost, abstrakce, zapouzdření)
# Zadání:
# Vytvořte dvě podtřídy třídy `Shape`: `Rectangle` a `Circle`.
# - `Rectangle` má atributy `width` a `height` a implementuje metodu `area`.
# - `Circle` má atribut `radius` a implementuje metodu `area`.


import math
#vsechny tridy dedi od tridy Shape
class Shape:
    def area(self):
        return 0.0
    
    #__init__ je konstruktor pro nastavení počátečních hodnot atributů
class Rectangle(Shape):
    def __init__(self, width, height):
        #self odkazuje na konrétní instanci třídy
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height #konkretni tvar ( dedeicna metoda)


class Circle(Shape):
    def __init__(self, radius): 
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

def test_shapes():
    rect = Rectangle(4, 5)
    assert rect.area() == 20

    circle = Circle(3)
    assert round(circle.area(), 1) == 28.3

test_shapes()
