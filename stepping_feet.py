import turtle

wn = turtle.Screen()
wn.setup(350,350)
print(wn.screensize())
wn.bgpic('striped_bw.gif')
# wn.bgcolor('gray')
wn.title('Stepping Feet')
wn.register_shape("rectangle",((0,0),(0,30),(15,30),(15,0)))


bus1 = turtle.Turtle()
bus1.color('blue')
bus1.speed(0)
bus1.shape('rectangle')
bus1.penup()
bus1.dx = 3

bus2 = turtle.Turtle()
bus2.color(255/255,239/255,129/255)
bus2.speed(0)
bus2.shape('rectangle')
bus2.penup()
bus2.dx = 3

bus1.setpos(-160,-25)
bus2.setpos(-160,25)
while True:
    bus1.setx(bus1.xcor()+bus1.dx)
    bus2.setx(bus2.xcor()+bus2.dx)
    if bus1.xcor()>120 or bus1.xcor()<-160:
        bus1.dx*=-1
    if bus2.xcor()>120 or bus2.xcor()<-160:
        bus2.dx*=-1




wn.mainloop()
