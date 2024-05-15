import time
import sys
import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.Font(None, 50)
littlefont = pygame.font.Font(None, 25)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LBLUE = (115, 177, 244)

fightb = pygame.Rect(SCREEN_WIDTH/6, 100, 75, 75)
homeb = pygame.Rect(SCREEN_WIDTH/6, 200, 75, 75)
shopb = pygame.Rect(SCREEN_WIDTH/6, 300, 75, 75)
casinob = pygame.Rect(SCREEN_WIDTH/6,400, 75, 75)
gymb = pygame.Rect(SCREEN_WIDTH/6,500, 75, 75)

def draw_text(text, font, color, surface, x, y):
  text = str(text)
  text_obj = font.render(text, True, color)
  text_rect = text_obj.get_rect()
  text_rect.center = (x, y)
  surface.blit(text_obj, text_rect)

class logic:

  def __init__(self):
    self.running = True

  def screen(self):
    screen.fill(WHITE)
    draw_text("what would you like to do?", font, BLACK, screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/5-50)
    pygame.draw.rect(screen, LBLUE, fightb)
    pygame.draw.rect(screen, LBLUE, homeb)
    pygame.draw.rect(screen, LBLUE, shopb)
    pygame.draw.rect(screen, LBLUE, casinob)
    pygame.draw.rect(screen, LBLUE, gymb)
    draw_text("fight rats", font, BLACK, screen, (SCREEN_WIDTH/3)+50,150)
    draw_text("go home", font, BLACK, screen, (SCREEN_WIDTH/3)+50,250)
    draw_text("go shopping", font, BLACK, screen, (SCREEN_WIDTH/3)+50, 350)
    draw_text("gamble", font, BLACK, screen, (SCREEN_WIDTH/3)+50,450)
    draw_text("go to the gym", font, BLACK, screen, (SCREEN_WIDTH/3)+50,550)
    pygame.display.flip()
    while self.running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self.running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            if fightb.collidepoint(event.pos):
                from fighting import fight
                f1 = fight()
                f1.Fight()
            elif homeb.collidepoint(event.pos):
                self.home()
            elif shopb.collidepoint(event.pos):
                self.shop()
            elif casinob.collidepoint(event.pos):
                self.casino()
            elif gymb.collidepoint(event.pos):
                from gym import Gym
                g1 = Gym()
                g1.EnterGym()

  def home(self):
    pass

  def shop(self):
    pass

  def casino(self):
    pass

