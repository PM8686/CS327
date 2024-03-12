class Point:
    def __init__(self):
        self.move(x,y)

    def move(self, x=0, y=0): #if you don't pass in a value, initialized to (0,0), if do those are replace
        self.x = x
        self.y = y

p1 = Point()
p2 = Point()

print(p1)

p1.move(1,2)

Point.move(p2, 1, 2)

p1 = Point(y=4)


print(f"({p1.x},{p1.y})")
print(f"({p2.x},{p2.y})")