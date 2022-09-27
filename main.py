import turtle
import random


window = turtle.Screen()
window.title('Simple space_ship Shooting Game')
window.setup(800,600)
window.bgpic('bg.png')
window.tracer(0)
window.listen() 

space_ship = turtle.Turtle()
space_ship.shape('triangle')
space_ship.shapesize(4,2) 
space_ship.color('blue')
space_ship.up() 
space_ship.goto(-380, 0)
space_ship.setheading(0)

bullet = turtle.Turtle()
bullet.shape('classic')
bullet.shapesize(.9, 1.5)
bullet.color('yellow')
bullet.up()
bullet.goto(space_ship.xcor(), space_ship.ycor())
bullet.state = 'ready'

pen = turtle.Turtle()
pen.up()
pen.hideturtle()
pen.color('red')
pen.goto(200,-275)
pen.write('Score: 0', font=('Courier', 24, 'normal'))


def shoot():
    bullet.state = 'fire'
   
    
def bullet_shot():
    bullet.fd(10)
    if bullet.ycor()<-300 or bullet.ycor()>300 or bullet.xcor()>400: 
        bullet.goto(space_ship.xcor(), space_ship.ycor())
        bullet.state = 'ready'
        
    
def turn_right():
    if bullet.state == 'ready':
        bullet.rt(10)
    
    
def turn_left():
    if bullet.state == 'ready':
        bullet.lt(10)
    
def move_up():
    if(bullet.state == "ready"):
        bullet.setheading(90)
        bullet.fd(30)
        bullet.setheading(0)
    
    space_ship.setheading(90)
    space_ship.fd(30)
    space_ship.setheading(0)

def move_down():
    if(bullet.state == "ready"):
        bullet.setheading(270)
        bullet.fd(30)
        bullet.setheading(0)
    space_ship.setheading(270)
    space_ship.fd(30)
    space_ship.setheading(0)



window.onkey(shoot, 'space')
window.onkey(turn_left, 'Left')
window.onkey(move_up, 'Up')
window.onkey(move_down, 'Down')
window.onkey(turn_right, 'Right')

enemy_list = []
colors = ['#cccccc', '#b3b3b3', '#595959', '#e6e6e6' , '#b3b3b3', '#666666']
game_over = False
score = 0

while not game_over:
    window.update()
    
    if bullet.state == 'fire':
        bullet_shot()

    delay = random.random() 
    if len(enemy_list)<10 and delay < 0.05: 
        enemy = turtle.Turtle()
        enemy.shape('circle')
        enemy.setheading(180)
        enemy.shapesize(2,3)
        enemy.color(random.choice(colors))
        enemy.up()
        enemy.goto(420, random.randint(-280,280))
        enemy_list.append(enemy)

    for i in enemy_list:
        i.goto(i.xcor()-0.5, i.ycor())

        if i.xcor()<-420:
            i.goto(1000,1000)
            enemy_list.remove(i)
            game_over = True
            pen.goto(0,0)
            pen.clear()
            pen.write(f'GAME OVER\nScore: {score}',align='center',
                      font=('Courier', 36, 'normal'))
            
        if bullet.distance(i) < 30:
            i.goto(1000,1000)
            enemy_list.remove(i)
            bullet.goto(space_ship.xcor(), space_ship.ycor())
            bullet.state = 'ready'
            score += 1
            pen.clear()
            pen.write(f'Score: {score}', font=('Courier', 24, 'normal'))
