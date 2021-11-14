from shape import Shape

class Triangle(Shape):
    def __init__(self, pos_x, pos_y, side_a):
        super().__init__(pos_x, pos_y)
        self.a = side_a

    def draw(self, turtle):
        super().draw(turtle)
        if self.color != None:
            turtle.pencolor(self.color)

        for i in range(3):
            turtle.fd(self.a)
            turtle.rt(120)