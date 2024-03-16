from math import pi


class Figure():

    def get_name(self,sides):  # Define a class of figure on number of this sides
        if len(sides) == 1:
            return "Circle"
        elif len(sides) == 3:
            return "Triangle"
        else:
            raise Exception('Type of figure is not allowed')

    def __init__(self,sides:list, name=None):  # 'sides' is list if numerical values - sides of figure,
                                               # name - type of figure, will be defined automaticly if it == None
        try:
            sides = list(map(lambda x: float(x), sides))
        except TypeError:
            return

        if any([x<=0 for x in sides]):
            raise ValueError()

        self.sides = sides
        self.name = name
        if name not in ["Circle", "Triangle"]:
            self.name = self.get_name(self.sides)
        print(self.sides,self.name)

    def circle_square(self):
        return pi*self.sides[0]**2

    def triangle_exists(self):
        a,b,c = self.sides[:3]
        if a>=b+c or b>=a+c or c>=a+b:
            print("This triangle not exists")
            return False
        else:
            return True

    def right_triangle(self):
        a, b, c = self.sides[:3]
        if a**2==b**2+c**2:
            return True
        elif b**2==a**2+c**2:
            self.sides[:3]=b,a,c
            return True
        elif c**2==a**2+b**2:
            self.sides[:3] = c, b, a
            return True
        else:
            return False

    def triangle_square(self):
        if self.triangle_exists():
            if self.right_triangle():
                return self.sides[1]*self.sides[2]/2
            else:
                a,b,c = self.sides[:3]
                p = (a+b+c)/2
                return (p*(p-a)*(p-b)*(p-c))**0.5
        else:
            raise ValueError
            return

    def calculate_square(self):
        if self.name == 'Circle':
            return self.circle_square()
        elif self.name == 'Triangle':
            return self.triangle_square()
        else:
            return

