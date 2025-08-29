import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("You must provide either a radius or a diameter")

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"circle with radius {self.radius:.2f}, diameter {self.diameter:.2f}, area {self.area:.2f}"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented








c1 = Circle(radius=4)
c2 = Circle(diameter=10)

print(c1)
print(f"c1 radius: {c1.radius}")          
print(f"c2 diameter: {c2.diameter}")      
print(f"c1 area: {c1.area:.2f}")          
c3 = c1 + c2
print(f"c1 + c2 = {c3}")                            
print(f"c1 < c2? {c1 < c2}")             
circles = [c1, c2]
sorted_circles = sorted(circles)
for c in sorted_circles:
    print(c)

