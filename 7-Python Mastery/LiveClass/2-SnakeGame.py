import turtle as t
import random as rd 

t.bgcolor("green")

caterPiller = t.Turtle()
caterPiller.shape("square")
caterPiller.color("red")
caterPiller.speed(0.5)
caterPiller.penup()
caterPiller.hideturtle()


leaf = t.Turtle()
leafShape = ((0,0), (14,2), (18, 6), (20, 20), (6, 18), (2, 14))
t.register_shape("leaf", leafShape)
leaf.shape("leaf")
leaf.penup()
leaf.hideturtle()
leaf.speed()


gameStarted = False
textTurtle = t.Turtle()
textTurtle.write("Press Space to start", align="center", font=("Arial", 16, "bold"))
textTurtle.hideturtle()

scoreTurtle = t.Turtle()
scoreTurtle.hideturtle()
scoreTurtle.speed(0)


def outsideWindow():
    leftWall = -t.window_width()/2
    rightWall = t.window_width()/2
    topWall = t.window_height()/2
    bottomWall = -t.window_height()/2
    (x, y) = caterPiller.pos()
    outside = x < leftWall or x > rightWall or y < bottomWall or y > topWall
    return outside


def gameOver():
    caterPiller.color("yellow")
    leaf.color("yellow")
    t.penup()
    t.hideturtle()
    t.write("Game Over!!!", align="center", font=("Arial", 30, "bold"))


def displayScore(currentScore):
    scoreTurtle.clear()
    scoreTurtle.penup()
    x = (t.window_width()/2) - 50
    y = (t.window_height()/2) - 50
    scoreTurtle.setpos(x, y)
    scoreTurtle.write(str(currentScore), align="right", font=("Arial", 40, "bold"))

def placeLeaf():
    leaf.hideturtle()
    leaf.setx(rd.randint(-200, 200))
    leaf.sety(rd.randint(-200, 200))
    leaf.showturtle()

def startGame():
    global gameStarted
    if (gameStarted):
        return 

    gameStarted = True
    score = 0
    textTurtle.clear()
    caterPillerSpeed = 2
    caterPillerLength = 3
    caterPiller.shapesize(1, caterPillerLength, 1)
    caterPiller.showturtle()
    displayScore(score)
    placeLeaf()

    while(True):
        caterPiller.forward(caterPillerSpeed)

        if (caterPiller.distance(leaf) < 20):
            placeLeaf()
            caterPillerLength += 1
            caterPiller.shapesize(1, caterPillerLength, 1)
            caterPillerSpeed += 1
            score += 5
            displayScore()

        if (outsideWindow):
            gameOver()
            break


def moveUp():
    if (caterPiller.heading() == 0 or caterPiller.heading() == 180):
        caterPiller.setheading(90)


def moveDown():
    if (caterPiller.heading() == 0 or caterPiller.heading() == 180):
        caterPiller.setheading(270)


def moveLeft():
    if (caterPiller.heading() == 90 or caterPiller.heading() == 270):
        caterPiller.setheading(180)


def moveRight():
    if (caterPiller.heading() == 90 or caterPiller.heading() == 270):
        caterPiller.setheading(0)


t.onkey(startGame, "space")
t.onkey(moveUp, "Up")
t.onkey(moveDown, "Down")
t.onkey(moveLeft, "Left")
t.onkey(moveRight, "Right")


t.listen()
t.mainloop()


