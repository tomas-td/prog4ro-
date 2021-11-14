class Shape:
    
    def __init__(self,pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y
        self.color = None

    def setColor(self, color):
        self.color = color

    def draw(self, turtle):
        turtle.penup()
        turtle.setpos(self.x, self.y)
        turtle.pendown()