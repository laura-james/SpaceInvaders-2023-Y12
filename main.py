import pygame
import random
import time

class Alien:
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.dir = "right" #starting direction
    self.width = 30
    self.height = 30
    self.points = 10

  def draw(self):
    screen.blit(alienImg,(self.x,self.y))
  def move(self):    
    if self.x <= -10:
      self.dir = "right" #switch direction
      self.y = self.y + 40 #shift down
    elif self.x > 570:
      self.dir = "left" #shift down
      self.y = self.y + 40  #shift down
      
    if self.dir == "left":
       self.x = self.x - 2       
    else:
       self.x = self.x + 2
      
class MegaAlien(Alien):
  def __init__(self,x,y):
    super().__init__(x, y)
    self.points = 50
    
  def move(self):
    self.x = self.x + 5
    if self.x > 570:
      self.x = 0

  def draw(self):
    screen.blit(megaAlienImg,(self.x,self.y))

class Gun:
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.width = 30
    self.height = 30
    
  def draw(self):
    screen.blit(gunImg,(self.x,self.y))
    
  def move(self,dir):    
    if self.x > 0 and dir == "right":
      self.x = self.x + 10
    if self.x < 600 and dir == "left":
      self.x = self.x - 10
  
class Bullet:
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.width = 5
    self.height = 10
   
  def draw(self):
    screen.blit(bulletImg,(self.x,self.y))

  def move(self):
    self.y = self.y - 2

  def checkCollide(self, otherthing):
  #returns True or False if Bullet has collided with other object
    if self.x < otherthing.x + otherthing.width and self.x + self.width > otherthing.x and self.y < otherthing.y + otherthing.height and self.y+self.height > otherthing.y:
      print ("collide")
      return True
    return False

class AlienBullet(Bullet):
  def move(self):
    self.y = self.y + 1

def writeText(text, x,y):
  font = pygame.font.SysFont(None, 24)
  img = font.render(text, True, (255,255,255))
  screen.blit(img, (x, y))

pygame.init()
BLACK   = (20,20,20)
backgroundcolour = BLACK
size    = [600,400]
screen  = pygame.display.set_mode(size)
alienImg = pygame.image.load("alien2.png")
megaAlienImg = pygame.image.load("megaalien.png")
gunImg = pygame.image.load("gun.png")
bulletImg = pygame.image.load("bullet.png")
pygame.display.set_caption('Space Invaders 2023')
clock = pygame.time.Clock()
score = 0
#create 10 aliens
aliens = []
for i in range(15):
  aliens.append(Alien(i*35,30))

megaAl1 = MegaAlien(50,100)
megaAl2 = MegaAlien(250,100)
aliens.append(megaAl1)
aliens.append(megaAl2)
#create Gun
mygun = Gun(290,365)
bullets = [] #array to hold all the bullets
alienbullets = []
## Game loop start---------
done = False
while not done:
## check for events start--
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
      mygun.move("left")
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
      mygun.move("right")
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
      bullets.append(Bullet(mygun.x+13, mygun.y-2))
          
## check for events end-----
## game logic start---------
  for al in  aliens:
    al.move()
    if random.randint(1,500) == 1:
      alienbullets.append(AlienBullet(al.x, al.y))
      

  for i in range(len(bullets)):
    bullets[i].move()
  for i in range(len(alienbullets)):
    alienbullets[i].move()
## game logic end-----------
## drawing start------------
  screen.fill(backgroundcolour)
  for al in aliens: #used to have for i in range(10)
    al.draw() #aliens[i].draw()
  mygun.draw()
  
  for bul in bullets:
    # loop through the aliens
    for al in aliens:
      # check if bullet has hit the alien
      if bul.checkCollide(al):
        score = score + al.points
        print("You hit one! Score = "+str(score))
        aliens.remove(al) #remove the alien
        bullets.remove(bul) #remove the bullet
        
    bul.draw()

  for albul in alienbullets:
  # loop through the aliens

    if albul.checkCollide(mygun):
      print("GAME OVER")
      backgroundcolour = (255,0,0)
      writeText("GAME OVER", 200,200)
      pygame.time.delay(1000)
     #done = True

    albul.draw()
  writeText("SCORE: "+str(score), 200,10)

  pygame.display.flip()
## drawing end -------------
  clock.tick(60)
## Game loop end------------
pygame.quit()

#useful links? 
#https://www.makeuseof.com/pygame-games-control-time-how-to/
#ideas for questions:
# whats the maximum number of points you can score
# what type of structure is the colour variable (tuple)
# How to stop the game if aliens reach the player
# keep a count of bullet s used and deduct from score
# adjust the frequncy of teh alien bullets
# make them drop at a random speed?
# 
# end the game when there are no more aliens
# keep a track of the time spent playing using Ticks

