import turtle
chirag = turtle.Turtle()
chirag.penup()
chirag.goto(-150 , 0)
chirag.pendown()
chirag.color('red', 'yellow')
chirag.begin_fill()
while True:
    chirag.forward(300)
    chirag.right(170)
    if abs(chirag.pos()) < 1 :
     break
chirag.end_fill()


turtle.done()



