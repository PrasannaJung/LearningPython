import turtle

t = turtle.Turtle()
t.up()
t.goto(0, -100)
t.down()
t.color('red')
t.begin_fill()
t.circle(100)
t.end_fill()
# fill a color


t.up()
t.goto(350,200)
t.down()
t.color('purple')
t.begin_fill()
t.circle(100)
t.end_fill()

t.up()
t.goto(350,-350)
t.down()
t.color('green')
t.begin_fill()
t.circle(100)
t.end_fill()

t.up()
t.goto(-350,200)
t.down()
t.color('yellow')
t.begin_fill()
t.circle(100)
t.end_fill()

t.up()
t.goto(-350,-350)
t.down()
t.color('blue')
t.begin_fill()
t.circle(100)
t.end_fill()

t.ht()
turtle.mainloop()
