# class ClassA:
#     def __init__(self, names=[]):
#         self.my_names = names
#         self.my_names.append("Tim")

#     obj1 = ClassA()

#     # obj1.my_names prints ["Tim", "Tim"] b/c lists are mutable

class ClassA:
    def __init__(self, names=None):
        if not names: #if nothing was passed in
            self.my_names = []
        else:
            self.my_names = names
        self.my_names.append("Tim")

    obj1 = ClassA()

class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def area(self):
        return self._length * self._width

class Square(Rectangle):
    def __init__(self, length, *args, **kwargs):
        super().__init__(length, length, *args, **kwargs)

# need to use super(). when using the same name as parent
class Triangle(Rectangle):
    def area(self):
        return super().area() / 2

class Cube(Square):
    def surface_area(self):
        face_area = self.area()
        return face_area * 6