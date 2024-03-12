

def foo(x, y):
    z = 0
    if (x > 0):
        if y > 0:
            z = x
    return z

def bar(a, b):
    z = 0
    if a > b:
        if a > 0:
            z = a
        else:
            z = b
    return a + b + z

def baz(x, y):
    z = 0
    if x > 0 and y > 0:
        if x < y:
            z = x
        else:
            z = y
    return x + y + z

def bazz(x, y):
    z = 0
    if x > 0 and y < 0:
        if y < -5:
            z = x
    else:
        while x < 5:
            x += 1
    return x + y + z



import math

class Point:
    "Represents a point in two-dimensional geometric coordinates"

    def __init__(self, new_x=0, new_y=0):
        """Initialize the position of a new point. The x and y
        coordinates can be specified. If they are not, the
        point defaults to the origin."""

        self.move(new_x, new_y)

    def reset(self):
        "Reset the point back to the geometric origin: 0, 0"

        self.move(0, 0)

    def move(self, new_x, new_y):
        "Move the point to a new location in 2D space."

        self._x = new_x
        self._y = new_y

    def calculate_distance(self, other_point):
        """Calculate the distance from this point to a second
        point passed as a parameter.

        This function uses the Pythagorean Theorem to calculate
        the distance between the two points. The distance is
        returned as a float."""
        
        return math.sqrt(
            (self._x - other_point._x)**2 +
            (self._y - other_point._y)**2
        )

    def __eq__(self, other):
        return self._x == other._x and self._y == other._y

def closest_pair(points_list):
    min_dist = points_list[0].calculate_distance(points_list[1])
    pair = (points_list[0], points_list[1])
    for p1 in points_list:
        for p2 in points_list:
            if not p1 is p2: # this was missing
                current_dist = p1.calculate_distance(p2) 
                if current_dist < min_dist:
                    min_dist = current_dist
                    pair = (p1, p2)
    return pair
