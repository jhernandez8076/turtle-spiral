import turtle

k=turtle.Turtle()
turtle.bgcolor('black')
k.shape('turtle')
k.speed(0)

#will draw a spiral with lines going left
#the line will have different colors 
#repeat the fuction and include color at the end of it
def draw_blackhole(k,size):
    for i in range(180):
        k.color('orange')
        k.fd(size*2)

        k.rt(10)
        k.fd(size/2)
        k.color('red')
        k.lt(80)
        k.fd(size)
        k.color('blue')
        k.rt(30)
        k.fd(size/3)
        k.color('yellow green')
        k.lt(70)
        k.fd(size/3.5)
        k.color('magenta')
        k.rt(70)
        k.fd(size*1.2)
        k.up()
        k.setpos(0,0)
        k.down()
        k.rt(2)

#will draw a star
#circles will be on the right line of the star  
sides=180
for times in range(sides):
        k.color('red')
        k.forward(times * 5)
        k.left(200)
        k.circle(50)
        k.speed(0)
draw_blackhole(k,100)



      
