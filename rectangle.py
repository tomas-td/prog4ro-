from shape import Shape

class Rectangle(Shape):
    def __init__(self, pos_x, pos_y, side_a, side_b):
        super().__init__(pos_x,pos_y)
        self.a = side_a
        self.b = side_b

    def draw(self, turtle):
        super().draw(turtle)
        if self.color != None:
            turtle.pencolor(self.color)

        for i in range(0,2):
            turtle.fd(self.a)
            turtle.right(90)
            turtle.fd(self.b)
            turtle.right(90)