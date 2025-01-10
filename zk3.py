# Příklad 3: Základy OOP (dědičnost, abstrakce, zapouzdření)
# Zadání:
# Vytvořte dvě podtřídy třídy `Shape`: `Rectangle` a `Circle`.
# - `Rectangle` má atributy `width` a `height` a implementuje metodu `area`.
# - `Circle` má atribut `radius` a implementuje metodu `area`.


import math

class Shape:
    def area(self):
        return 0.0

class Rectangle(Shape):
    def __init__(self, width, height):
        #implementace sir a vys, pomoci kontsr
        self.width = width
        self.height = height

    def area(self):
        # Výpočet plochy 
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius): #konstruktor ktery impl radius
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

def test_shapes():
    rect = Rectangle(4, 5)
    assert rect.area() == 20

    circle = Circle(3)
    assert round(circle.area(), 1) == 28.3

test_shapes()
