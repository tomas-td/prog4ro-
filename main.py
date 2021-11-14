import turtle
from rectangle import Rectangle
from triangle import Triangle
from circle import Circle

jano = turtle.Turtle()
jano.speed(5)

rectangle_1 = Rectangle(30,30,60,100)
rectangle_1.setColor("purple")
rectangle_1.draw(jano)

rectangle_2 = Rectangle(-85,85,160,40)
rectangle_2.setColor("red")
rectangle_2.draw(jano)

triangle = Triangle(60,0,100)
triangle.setColor("black")
triangle.draw(jano)

circle = Circle(0,0,40)
circle.setColor("orange")
circle.draw(jano)

turtle.exitonclick()