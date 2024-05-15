import random
import pygame
from Enemy import Enemy
from player import Player
e1=Enemy()
p1=Player()

pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Start Screen")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Buttons

a1 = pygame.Rect(150 , 500, 150, 75)
a2= pygame.Rect(400 , 500, 150, 75)
b = pygame.Rect(650 , 500, 150, 75)

#ratButton_rect = pygame.Rect()
contButton_rect = pygame.Rect(((screen.get_width() // 2)-75) , 275, 150, 100)

# Fonts
font = pygame.font.Font(None, 50)
littlefont = pygame.font.Font(None, 25)


def draw_text(text, font, color, surface, x, y):
  text_obj = font.render(text, True, color)
  text_rect = text_obj.get_rect()
  text_rect.center = (x, y)
  surface.blit(text_obj, text_rect)

class fight:

  def __init__(self):
    self.turn = 0
    self.pmove = False
    self.emove = False

  def RatType(self):
    rat = random.randint(0,100)
    if rat < 50:
      e1.NormalEnemy(self)
    elif rat >= 50 and rat < 70:
      e1.FireEnemy()
    elif rat >=70 and rat < 90:
      e1.IceEnemy
    else:
      e1.BossEnemy()
  

  def PTurn(self):
    self.turn = 1
    self.pmove = True
    self.emove = False

  def ETurn(self):
    self.turn = 2
    self.emove = True
    self.pmove = False
    er = random.randint(1,3)
    elif er =1:
      ea = 1
      atype = "light attack"
    elif er =2:
      ea = 2
      atype = "heavy attack"
    elif er = 3:
      ea = 3
      atype = "block"

  def Damages(self):
    e1.take_damage(p1.damage)
    p1.takedamage(e1.damage)

  def Fight(self):
    screen.fill(WHITE)
    draw_text("you have encountered a " + e1.name, font, BLACK, screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/8)
    pygame.draw.rect(screen, RED, contButton_rect)
    pygame.display.flip()
    while self.running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False
          pygame.quit()
          sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            if contButton_rect.collidepoint(event.pos):
              pass
    
    


    
