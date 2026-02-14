# Base class
class Polygon:
    def __init__(self, name):
        self.name = name

    def area(self):
        print("Area method not implemented!")

    def display(self):
        print(f"Polygon: {self.name}")
        print(f"Area: {self.area()}")


# Rectangle class (inherits from Polygon)
class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Square class (inherits from Rectangle)
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.name = "Square"


# Triangle class
class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Circle class
class Circle(Polygon):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.142 * self.radius * self.radius


# Main program
def main():
    print("Choose a polygon to calculate area:")
    print("1. Rectangle")
    print("2. Square")
    print("3. Triangle")
    print("4. Circle")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        shape = Rectangle(length, width)

    elif choice == 2:
        side = float(input("Enter side length: "))
        shape = Square(side)

    elif choice == 3:
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        shape = Triangle(base, height)

    elif choice == 4:
        radius = float(input("Enter radius: "))
        shape = Circle(radius)

    else:
        print("Invalid choice!")
        return

    shape.display()


# Run the program
if __name__ == "__main__":
    main()