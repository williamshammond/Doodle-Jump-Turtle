#####----------Doodle Jump in Python With Turtle by William Hammond @ Juni Learning----------#####

##imports
import turtle, random

###----------Turtle initialization----------###

#Turtle for Alien
s = turtle.Screen()
alien = turtle.Turtle()
alien.speed(0)
alien.pensize(2)
alien.ht()

#Turtle for platforms
platform = turtle.Turtle()
platform.speed(0)
platform.ht()
#Screen Turtle
screen = turtle.Screen()
screen.tracer(0)

#Turle for drawing gamespace
space = turtle.Turtle()
space.ht()

#Turtle for drawing button
button = turtle.Turtle()
button.pensize(10)
button.ht()



###----------Global Variables----------###

platforms = []
speed = 4
#Screen 0 means start screen, 1 means rules screen, 2 means skins screen, 3 means playing
whichScreen = 0
gravity = 0
alienSpeed = 18
alienXSpeed = 0
alienDirection = 1
platformSpeed = 4
score = 0
highScore = 0
#The maximum number of platforms will decrease throughout the game
numPlatforms = 8
#Skin 0 is the default green skin
skin = 0



##----------#Functions----------###

#Function to draw alien
def drawAlien(x,y,direction,skin):
  if whichScreen != 1 and whichScreen != 2:
    alien.clear()
    
  #Color of outline
  if skin == 1:
    alien.color("royal blue")
  elif skin == 2:
    alien.color("firebrick")
  else:
    alien.color("black")
    
  alien.penup()
  alien.goto(x,y)
  if direction == 1:
    alien.setheading(90)
    alien.forward(55)
    alien.left(90)
    alien.forward(24)
    alien.right(180)
    alien.pendown()
    
    alien.begin_fill()
    alien.setheading(90)
    for i in range(9):
      alien.forward(8)
      alien.right(18)
    for i in range(14):
      alien.forward(1.5)
      alien.left(5)
    alien.forward(14)
    alien.left(60)
    
    for i in range(20):
      alien.forward(2.7)
      alien.right(15)
    alien.left(60)
    alien.forward(10)
    
    for i in range(18):
      alien.forward(1.5)
      alien.left(5)
    alien.right(90)
    alien.forward(49)
    
    #Main body color
    if skin == 0:
      alien.color("yellow green")
    elif skin == 1:
      alien.color("deep sky blue")
    elif skin == 2:
      alien.color("black")
    elif skin == 3:
      alien.color("gold")
    elif skin == 4:
      alien.color("pink")
    elif skin == 5:
      alien.color("dark orange")
    elif skin == 6:
      alien.color("white")
    elif skin == 7:
      #light red
      alien.color(245,70,50)
    elif skin == 8:
      alien.color("orchid")
    elif skin == 9:
      alien.color("silver")
      
    alien.end_fill()
    alien.setheading(270)
    alien.forward(25)
    
    #Main lower body color
    if skin == 0:
      alien.color("olive drab")
    elif skin == 1:
      alien.color("steel blue")
    elif skin == 2:
      alien.color("maroon")
    elif skin == 3:
      alien.color("goldenrod")
    elif skin == 4:
      alien.color("deep pink")
    elif skin == 5:
      alien.color("orange red")
    elif skin == 6:
      alien.color("black")
    elif skin == 7:
      #darkish red
      alien.color(230,0,0)
    elif skin == 8:
      alien.color("dark orchid")
    elif skin == 9:
      alien.color("dark grey")
      
    alien.begin_fill()
    for i in range(2):
      alien.left(90)
      alien.forward(49)
      alien.left(90)
      alien.forward(24)
    alien.left(90)
    alien.end_fill()
    
    #Color of lower part lines
    if skin == 6:
      alien.color("crimson")
    else:
      alien.color("black")
      
    alien.forward(49)
    alien.left(90)
    alien.forward(8)
    alien.left(90)
    alien.forward(49)
    alien.right(90)
    alien.forward(8)
    alien.right(90)
    alien.forward(49)
    alien.left(90)
    alien.forward(8)
    alien.left(90)
    alien.forward(49)
    alien.left(90)
    alien.forward(24)
    alien.backward(24)
    
    #Color of outline
    if skin == 1:
      alien.color("royal blue")
    elif skin == 2:
      alien.color("firebrick")
    else:
      alien.color("black")
      
    alien.backward(31)
    alien.forward(31)
    
    #Color of lower part lines
    if skin == 6:
      alien.color("crimson")
    else:
      alien.color("black")
  
    alien.left(90)
    alien.forward(49)
    alien.right(90)
    alien.forward(24)
    alien.penup()
    alien.backward(55)
    alien.right(90)
    
    #Eye color
    if skin == 2:
      alien.color("red")
    elif skin == 3:
      alien.color("dodger blue")
    elif  skin == 6:
      alien.color("crimson")
    elif skin == 9:
      alien.color("cyan")
    else:
      alien.color("black")
      
    alien.forward(10)
    alien.dot(3)
    alien.forward(15)
    alien.dot(3)
    alien.backward(25)
    alien.left(90)
    alien.forward(55)
    
    #Color of legs
    alien.color("black")

    alien.pendown()
    for i in range(4):
      alien.right(90)
      alien.forward(11)
      alien.left(90)
      alien.forward(10)
      alien.left(90)
      alien.forward(5)
      alien.backward(5)
      alien.right(90)
      alien.backward(10)
      
    #Color of lower lines
    if skin == 6:
      alien.color("crimson")
    else:
      alien.color("black")
      
    alien.left(90)
    alien.backward(5)
    alien.forward(49)
     
  #Inverse version of the alien drawing code if the alien is facing left
  else:
    
    #Color of outline
    if skin == 1:
      alien.color("royal blue")
    elif skin == 2:
      alien.color("firebrick")
    else:
      alien.color("black")
    
    alien.setheading(90)
    alien.forward(55)
    alien.right(90)
    alien.forward(24)
    alien.left(180)
    alien.pendown()
    
    alien.begin_fill()
    alien.setheading(90)
    for i in range(9):
      alien.forward(8)
      alien.left(18)
    for i in range(14):
      alien.forward(1.5)
      alien.right(5)
    alien.forward(14)
    alien.right(60)
    
    for i in range(20):
      alien.forward(2.7)
      alien.left(15)
    alien.right(60)
    alien.forward(10)
    
    for i in range(18):
      alien.forward(1.5)
      alien.right(5)
    alien.left(90)
    alien.forward(49)
    
    #Main body color
    if skin == 0:
      alien.color("yellow green")
    elif skin == 1:
      alien.color("deep sky blue")
    elif skin == 2:
      alien.color("black")
    elif skin == 3:
      alien.color("gold")
    elif skin == 4:
      alien.color("pink")
    elif skin == 5:
      alien.color("dark orange")
    elif skin == 6:
      alien.color("white")
    elif skin == 7:
      #light red
      alien.color(245,70,50)
    elif skin == 8:
      alien.color("orchid")
    elif skin == 9:
      alien.color("silver")
    
    alien.end_fill()
    alien.setheading(270)
    alien.forward(25)
    
    #Main lower body color
    if skin == 0:
      alien.color("olive drab")
    elif skin == 1:
      alien.color("steel blue")
    elif skin == 2:
      alien.color("maroon")
    elif skin == 3:
      alien.color("goldenrod")
    elif skin == 4:
      alien.color("deep pink")
    elif skin == 5:
      alien.color("orange red")
    elif skin == 6:
      alien.color("black")
    elif skin == 7:
      #darkish red
      alien.color(230,0,0)
    elif skin == 8:
      alien.color("dark orchid")
    elif skin == 9:
      alien.color("dark grey")
      
    alien.begin_fill()
    for i in range(2):
      alien.right(90)
      alien.forward(49)
      alien.right(90)
      alien.forward(24)
    alien.right(90)
    alien.end_fill()
    
    #Color of lower part lines
    if skin == 6:
      alien.color("crimson")
    else:
      alien.color("black")

    alien.forward(49)
    alien.right(90)
    alien.forward(8)
    alien.right(90)
    alien.forward(49)
    alien.left(90)
    alien.forward(8)
    alien.left(90)
    alien.forward(49)
    alien.right(90)
    alien.forward(8)
    alien.right(90)
    alien.forward(49)
    alien.right(90)
    alien.forward(24)
    alien.backward(24)
    
    #Color of outline
    if skin == 1:
      alien.color("royal blue")
    elif skin == 2:
      alien.color("firebrick")
    else:
      alien.color("black")
      
    alien.backward(31)
    alien.forward(31)
    
    #Color of lower part lines
    if skin == 6:
      alien.color("crimson")
    else:
      alien.color("black")
  
    alien.right(90)
    alien.forward(49)
    alien.left(90)
    alien.forward(24)
    alien.penup()
    alien.backward(55)
    alien.left(90)
    
    #Eye color
    if skin == 2:
      alien.color("red")
    elif skin == 3:
      alien.color("dodger blue")
    elif  skin == 6:
      alien.color("crimson")
    elif skin == 9:
      alien.color("cyan")
    else:
      alien.color("black")
      
    alien.forward(10)
    alien.dot(3)
    alien.forward(15)
    alien.dot(3)
    alien.backward(25)
    alien.right(90)
    alien.forward(55)
    
    #Color of legs
    alien.color("black")

    
    alien.pendown()
    for i in range(4):
      alien.left(90)
      alien.forward(11)
      alien.right(90)
      alien.forward(10)
      alien.right(90)
      alien.forward(5)
      alien.backward(5)
      alien.left(90)
      alien.backward(10)
      
    #Color of lower part lines
    if skin == 6:
      alien.color("crimson")
    else:
      alien.color("black")
      
    alien.right(90)
    alien.backward(5)
    alien.forward(49)
      
  alien.penup()
  alien.goto(x,y)

#Functions for side to side alien movement
def moveAlienLeft():
  global alienDirection, alienXSpeed
  #Set global direction and speed variables to be negative
  alienDirection = -1
  alienXSpeed = -8
  
def moveAlienRight():
  global alienDirection, alienXSpeed
  #Set global direction and speed variables to be positive
  alienDirection = 1
  alienXSpeed = 8
  
#Function for alien bouncing
def alienBounce():
  global gravity, alienSpeed
  
  #Check if the alien's coordinates are coliding with any of the platforms
  for platform in platforms:
    if(alien.ycor() - platform[1] < 35 and alien.ycor() - platform[1] > -5 and abs(alien.xcor() - platform[0]) < 65 and alienSpeed < 0):
      #If the platform is not level 3, bounce the alien
      if platform[3] < 2:
        platform[3] += 1
        gravity = 0
        alienSpeed = 18
        break
      else:
        #If the platfom is level 3, explode and remove it
        drawPlatform(platform[0],platform[1],3)
        screen.update()
        platforms.remove(platform)
        break
  
#Function for alien moving up and down   
def alienMovement():
  global gravity, alienSpeed, alienXSpeed, skin
  x = alien.xcor()
  y = alien.ycor()
  y += alienSpeed
  x += alienXSpeed
  
  #Apply and increaase cravity
  alienSpeed -= gravity
  gravity += 0.05
  
  #Bounce alien off walls
  if abs(x)>270:
    alienXSpeed *= -1
    x += 2 * alienXSpeed

  #Cap maximum downward speed
  if alienSpeed < -40:
    alienSpeed = -40
  
  drawAlien(x,y,1,skin)  

#Function to draw platform
def drawPlatform(x,y,breakLevel):
  platform.pensize(2)
  platform.setheading(0)
  platform.penup()
  platform.goto(x,y)
  platform.pendown()
    
  #If it is a level 0, 1, or 2 platform  
  if breakLevel != 3:
    platform.color("yellow green")
    platform.begin_fill()
    
    for i in range(2):
      platform.forward(50)
      for i in range(9):
        platform.forward(2)
        platform.left(20)
      platform.forward(50)
      
    platform.end_fill()
    
    #Draw cracks if platform is breaking
    if breakLevel == 1:
      platform.color("black")
      platform.left(120)
      platform.forward(5)
      platform.right(60)
      platform.forward(5)
      platform.left(60)
      platform.forward(5)
    elif breakLevel == 2:
      platform.color("black")
      platform.penup()
      platform.backward(35)
      platform.pendown()
      platform.left(90)
      platform.forward(5)
      platform.right(60)
      platform.forward(5)
      platform.left(60)
      platform.forward(5)
      platform.right(110)
      platform.forward(5)
      platform.right(60)
      platform.forward(5)
      platform.left(60)
      platform.forward(5)
      platform.left(60)
      platform.forward(5)
      platform.right(60)
      platform.forward(5)
      platform.left(60)
      platform.forward(5)
      platform.right(90)
      platform.forward(10)
      platform.left(90)
      platform.forward(5)
      platform.left(30)
      platform.forward(5)
      platform.right(90)
      platform.forward(8)
      platform.right(25)
      platform.forward(5)
      platform.left(45)
      platform.forward(8)
      platform.left(70)
      platform.forward(8)
      platform.right(90)
      platform.forward(5)
      platform.right(30)
      platform.forward(8)
      platform.backward(8)
      platform.left(60)
      platform.forward(8)
      platform.right(50)
      platform.forward(5)
      platform.left(50)
      platform.forward(5)
      
  #If it's a level 3 platform then it just exploded
  else:
    platform.begin_fill()
    for i in range(18):
      platform.forward(10)
      platform.right(100)
      platform.forward(10)
      platform.left(80)
    platform.color("orange")
    platform.end_fill()
    platform.penup()
    platform.right(98)
    platform.forward(47)
    platform.pendown()
    platform.color("black")
    platform.begin_fill()
    
    for i in range(18):
      platform.forward(7)
      platform.right(100)
      platform.forward(7)
      platform.left(80)
    platform.color("yellow")
    platform.end_fill()
    platform.penup()
    platform.right(104)
    platform.forward(32)
    platform.pendown()
    platform.color("black")
    platform.begin_fill()
    
    for i in range(12):
      platform.forward(6)
      platform.right(100)
      platform.forward(6)
      platform.left(70)
    platform.color("orange red")
    platform.end_fill()
 
#Function to move platforms
def movePlatforms():
  platform.clear()
  for i in range(len(platforms)):
    plat = platforms[i]
    x = plat[0]
    y = plat[1]
    direction = plat[2]
    breakLevel = plat[3]
    
    x += direction * platformSpeed
    
    #Bounce off walls
    if (abs(x)>235):
      direction *= -1
    
    platforms[i] = [x,y,direction,breakLevel]
    drawPlatform(x,y,breakLevel)

#Function to draw start button
def drawStartButton():
  button.setheading(0)
  button.penup()
  button.goto(-100,-150)
  button.pendown()
  button.pensize(3)
  button.color("black")
  button.begin_fill()
  
  for i in range(2):
    button.forward(200)
    button.left(90)
    button.forward(100)
    button.left(90)
  button.color("yellow")
  button.end_fill()
  
  button.color("black")
  button.left(90)
  button.forward(100)
  button.penup()
  button.goto(-2,-115)
  button.write("START", move=False, align="center", font=("Courier",45, "normal"))
  
  button.goto(0,-225)
  highScoreString = "High Score: " + str(highScore)
  button.write(highScoreString, move=False, align="center", font=("Courier",22, "normal"))
  
  drawAlien(-10,20,1,skin)
  drawPlatform(-10,-10,0)
  
#Function to draw replay button
def drawReplayButton():
  button.setheading(0)
  button.penup()
  button.goto(-100,-150)
  button.pendown()
  button.color("black")
  button.begin_fill()
  
  for i in range(2):
    button.forward(200)
    button.left(90)
    button.forward(100)
    button.left(90)
    
  button.color("yellow")
  button.end_fill()
  button.color("black")
  button.left(90)
  button.forward(100)
  button.penup()
  button.goto(-1,-115)
  button.write("REPLAY", move=False, align="center", font=("Courier",38, "normal"))
  
  button.goto(0,-225)
  highScoreString = "High Score: " + str(highScore)
  button.write(highScoreString, move=False, align="center", font=("Courier",22, "normal"))
  button.penup()

  drawAlien(-10,20,1,skin)
  drawPlatform(-10,-10,0)
  
#Function to draw rules button
def drawRulesButton():
  button.setheading(0)
  button.pensize(3)
  button.penup()
  button.goto(-100,-165)
  button.pendown()
  button.color("black")
  button.begin_fill()
  
  for i in range(2):
    button.forward(90)
    button.right(90)
    button.forward(30)
    button.right(90)
  button.color("red")
  button.end_fill()
  button.color('black')
  button.right(90)
  button.forward(30)
  button.penup()
  button.left(135)
  button.forward(9)
  button.write("Rules", move=False, align="left", font=("Courier",20, "normal"))

#Function to draw skins button
def drawSkinsButton():
  button.setheading(0)
  button.pensize(3)
  button.penup()
  button.goto(10,-165)
  button.pendown()
  button.color("black")
  button.begin_fill()
  
  for i in range(2):
    button.forward(90)
    button.right(90)
    button.forward(30)
    button.right(90)
  button.color("medium purple")
  button.end_fill()
  button.color('black')
  button.right(90)
  button.forward(30)
  button.penup()
  button.left(135)
  button.forward(9)
  button.write("Skins", move=False, align="left", font=("Courier",20, "normal"))
  
#Function to draw rules page
def showRules():
  button.penup()
  button.goto(-80,370)
  button.write("Rules", move=False, align="Center", font=("Courier",40, "normal"))
  button.goto(-280,350)
  button.pensize(3)
  button.pendown()
  button.setheading(0)
  button.forward(560)
  button.penup()
  
  drawAlien(-150,210,-1,skin)
  drawAlien(150,170,1,skin)
  button.goto(-25,240)
  button.pendown()
  button.begin_fill()
  button.setheading(180)
  button.forward(70)
  button.left(90)
  button.forward(10)
  button.right(135)
  button.forward(15)
  button.right(90)
  button.forward(15)
  button.right(135)
  button.forward(10)
  button.left(90)
  button.forward(70)
  button.end_fill()
  
  button.penup()
  button.goto(25,205)
  button.pendown()
  button.begin_fill()
  button.setheading(0)
  button.forward(70)
  button.left(90)
  button.forward(10)
  button.right(135)
  button.forward(15)
  button.right(90)
  button.forward(15)
  button.right(135)
  button.forward(10)
  button.left(90)
  button.forward(70)
  button.end_fill()
  button.penup()
  
  button.goto(-280,130)
  button.write("Use the left/right arrow keys to move side to side", move=False, align="Center", font=("Courier",14, "normal"))
  
  button.pensize(2)
  button.setheading(0)
  button.goto(-270,105)
  button.pendown()
  
  for i in range(68):
    button.forward(5)
    button.penup()
    button.forward(3)
    button.pendown()
  button.penup()
  
  drawPlatform(-210,40,0)
  drawPlatform(-60,10,1)
  drawPlatform(80,40,2)
  drawPlatform(240,50,3)
  
  button.goto(-250,-60)
  button.write("Platforms will explode on their third bounce", move=False, align="Center", font=("Courier",14, "normal"))
  
  button.setheading(0)
  button.goto(-270,-80)
  button.pendown()
  for i in range(68):
    button.forward(5)
    button.penup()
    button.forward(3)
    button.pendown()
  button.penup()
  
  drawAlien(0,-190,1,skin)
  button.goto(-18,-200)
  button.pensize(1)
  for i in range(3):
    button.pendown()
    button.setheading(270)
    button.forward(30)
    button.backward(30)
    button.left(90)
    button.penup()
    button.forward(20)
  button.goto(-230,-120)
  
  button.write("High Score: 2460", move=False, align="Center", font=("Courier",14, "bold"))
  button.goto(-270,-260)
  button.write("Fewer platforms will spawn as you make it higher", move=False, align="Center", font=("Courier",14, "normal"))
  button.goto(-170,-285)
  button.write("Try to beat your high score!", move=False, align="Center", font=("Courier",14, "normal"))
  
  button.pensize(2)
  button.setheading(0)
  button.goto(-270,-310)
  button.pendown()
  for i in range(68):
    button.forward(5)
    button.penup()
    button.forward(3)
    button.pendown()
  button.penup()
  
  #Draw main menu return button
  button.pensize(3)
  button.penup()
  button.goto(-100,-340)
  button.pendown()
  button.color("black")
  button.begin_fill()
  for i in range(2):
    button.forward(200)
    button.right(90)
    button.forward(50)
    button.right(90)
  button.color("red")
  button.end_fill()
  button.color('black')
  button.right(90)
  button.forward(50)
  button.penup()
  button.left(133)
  button.forward(25)
  button.write("Main Menu", move=False, align="left", font=("Courier",22, "normal"))
  button.penup()
  screen.update()
  
def selectSkin():
  button.clear()
  button.penup()
  button.goto(-230,370)
  button.write("Pick Your Skin!", move=False, align="Center", font=("Courier",40, "normal"))
  button.goto(-280,350)
  button.pensize(3)
  button.pendown()
  button.setheading(0)
  button.forward(560)
  button.penup()
  
  #Draw main menu return button
  button.pensize(3)
  button.penup()
  button.goto(-100,-340)
  button.pendown()
  button.color("black")
  button.begin_fill()
  for i in range(2):
    button.forward(200)
    button.right(90)
    button.forward(50)
    button.right(90)
  button.color("red")
  button.end_fill()
  button.color('black')
  button.right(90)
  button.forward(50)
  button.penup()
  button.left(133)
  button.forward(25)
  button.write("Main Menu", move=False, align="left", font=("Courier",22, "normal"))
  button.penup()
  drawAlien(-150,80,1,0)
  drawAlien(-10,80,1,1)
  drawAlien(120,80,1,2)
  drawAlien(-225,-50,1,3)
  drawAlien(-85,-50,1,4)
  drawAlien(55,-50,1,5)
  drawAlien(195,-50,1,6)
  drawAlien(-150,-180,1,7)
  drawAlien(-10,-180,1,8)
  drawAlien(120,-180,1,9)
  
  if skin == 0:
    button.goto(-185,165)
  elif skin == 1:
    button.goto(-45,165)
  elif skin == 2:
    button.goto(85,165)
  elif skin == 3:
    button.goto(-265,35)
  elif skin == 4:
    button.goto(-120,35)
  elif skin == 5:
    button.goto(20,35)
  elif skin == 6:
    button.goto(160,35)
  elif skin == 7:
    button.goto(-185,-95)
  elif skin == 8:
    button.goto(-45,-95)
  elif skin == 9:
    button.goto(85,-95)
      
  button.setheading(90)
  button.pensize(6)
  for i in range(4):
    button.pendown()
    button.forward(10)
    button.right(90)
    button.forward(10)
    button.penup()
    button.forward(90)

  screen.update()

#Function to draw score
def drawScore():
  button.clear()
  button.penup()
  button.goto(-270,390)
  scoreString = "SCORE: " + str(score)
  button.write(scoreString, move=False, align="left", font=("Courier",22, "normal"))
  screen.update()
  
#Death function
def checkDeath():
  global whichScreen, highScore
  if alien.ycor() < -450:
    alien.clear()
    platform.clear()
    whichScreen = 0
    if score > highScore:
      highScore = score
    return False
  else:
    return True
    
#Function for shifting screen up
def updateScreen():
  global score
  y = alien.ycor()
  if y > 200 and alienSpeed > -15:
    y -= 10
    score += 5
    for i in range(len(platforms)):
      platform = platforms[i]
      platforms[i] = [platform[0],platform[1]-10,platform[2],platform[3]]
    alien.goto(alien.xcor(), y)
      
#Function to add and delete platforms
def updatePlatforms():
  global platforms, score, numPlatforms
  j = 0
  for i in range(len(platforms)):
    if platforms[j][1] < -380:
      platforms.remove(platforms[j])
    else:
      j+=1
  while alien.ycor() > 100 and len(platforms) < numPlatforms:
    direction = random.randint(0,1)
    if direction == 0:
      direction = -1
    platforms.append( [random.randint(-210,210),random.randint(250,400),direction,0])
  if random.randint(0,300) == 500 and score != 0 and numPlatforms > 5 and alien.ycor() > 200:
    numPlatforms -=1

#Function to run game the main game
def runGame():
  global score, gravity, alienSpeed, platforms, alienDirection, alienXSpeed
  score = 0
  gravity = 0
  alienSpeed = 18
  alienDirection = 1
  alienXSpeed = 0
  
  #Create all of the initial platforms
  platforms = []
  #List of alien x,x tuples
  #(x,y,direction,breakLevel) -1 = left 1 = right
  #3 bounces before breaking
  
  #Track sections to allocate platforms
  sectionBottom = -350
  sectionTop = -200
  
  #Nested loop to allocate platforms fairly across the board
  for i in range(4):
    for i in range(2):
      x = random.randint(-210,210)
      y = random.randint(sectionBottom,sectionTop)
      direction = random.randint(0,1)
      if direction == 0:
        direction = -1
      breakLevel = 0
      platforms.append([x,y,direction,breakLevel])
    sectionTop += 150
    sectionBottom += 150
  
  #Each turn while true loop
  while True:
    updatePlatforms()
    movePlatforms()
    alienBounce()
    alienMovement()
    updateScreen()
    drawAlien(alien.xcor(),alien.ycor(), alienDirection,skin)
    drawScore()
    screen.update()
    if checkDeath() == False:
      break
    
  drawReplayButton()
  drawRulesButton()
  drawSkinsButton()
  screen.update()

#Start game click function
def buttonClicks(x,y):
  global whichScreen, skin
  if abs(x) < 100 and y < -50 and y > -150 and whichScreen == 0:
    whichScreen = 3
    alien.goto(0,0)
    button.clear()
    runGame()
  elif x > -100 and x < -10 and y < -165 and y > -195 and whichScreen== 0:
    whichScreen = 1
    alien.goto(0,0)
    button.clear()
    alien.clear()
    platform.clear()  
    showRules()
  elif x > 10 and x < 100 and y < -165 and y > -195 and whichScreen == 0:
    whichScreen = 2
    alien.goto(0,0)
    button.clear()
    alien.clear()
    platform.clear()
    selectSkin()
  elif abs(x) < 100 and y < -340 and y > -390 and (whichScreen == 1 or whichScreen == 2):
    whichScreen = 0
    button.clear()
    alien.clear()
    platform.clear()
    drawStartButton()
    drawRulesButton()
    drawSkinsButton()
    screen.update()
  elif whichScreen == 2 and x > -185 and x < -85 and y > 65 and y < 165:
    skin = 0
    selectSkin()
  elif whichScreen == 2 and x > -45 and x < 55 and y > 65 and y < 165:
    skin = 1
    selectSkin()
  elif whichScreen == 2 and x > 85 and x < 185 and y > 65 and y < 165:
    skin = 2
    selectSkin()
  elif whichScreen == 2 and x > -265 and x < -165 and y > -65 and y < 35:
    skin = 3
    selectSkin()
  elif whichScreen == 2 and x > -120 and x < -20 and y > -65 and y < 35:
    skin = 4
    selectSkin()
  elif whichScreen == 2 and x > 20 and x < 120 and y > -65 and y < 35:
    skin = 5
    selectSkin()
  elif whichScreen == 2 and x > 160 and x < 260 and y > -65 and y < 35:
    skin = 6
    selectSkin()
  elif whichScreen == 2 and x > -185 and x < -85 and y > -195 and y < -95:
    skin = 7
    selectSkin()
  elif whichScreen == 2 and x > -45 and x < 55 and y > -195 and y < -95:
    skin = 8
    selectSkin()
  elif whichScreen == 2 and x > 85 and x < 185 and y > -195 and y < -95:
    skin = 9
    selectSkin()



###---------------Keyboard and Mouse Event Listeners---------------###

screen.onkey(moveAlienLeft,"Left")
screen.onkey(moveAlienRight,"Right")
screen.onclick(buttonClicks)
screen.listen()



###---------------Startup Game Code---------------###

#Draw background
space.penup()
space.pensize(20)
space.goto(-300,-425)
space.pendown()

space.color("black")
space.begin_fill()
for i in range(2):
  space.forward(600)
  space.left(90)
  space.forward(875)
  space.left(90)
space.color("light blue")
space.end_fill()
space.left(90)
space.color("black")
space.forward(875)

#Set up initial buttons and messages
drawStartButton()
drawRulesButton()
drawSkinsButton()
button.goto(-175,340)
button.write("DOODLE", move=False, align="left", font=("Courier",70, "normal"))
button.goto(-115,270)
button.write("JUMP", move=False, align="left", font=("Courier",70, "normal"))
button.goto(-115,240)
button.write("by William Hammond", move=False, align="left", font=("Courier",15, "normal"))
button.goto(-235,180)
button.write("Press command (Mac) or control (Windows) and minus", move=False, align="left", font=("Courier",12, "normal"))
button.goto(-260,160)
button.write("until you can see the entire black outline of the game!", move=False, align="left", font=("Courier",12, "normal"))


screen.update()
  
turtle.mainloop()