# from accounts import SavingsAccount

   
class point:
    static_variable = 0

    def __init__(self):
        "Initializes the point"
        self._x = 1
        self._y = 0

    def print_point(self):
        "print's the point"
        print(self._x)

    def __str__(self):
        "works"
        return f"((self._x), (self._y))"


    @classmethod
    def classmethod(cls):
        pass
        
    @staticmethod               # better to just leave out of class, only for organization
    def staticmethod():
        pass

this = point()

this.print_point()