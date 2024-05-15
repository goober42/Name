import pygame
import sys
import random
import time
from player import Player
p1 = Player()

# Initialize Pygame
pygame.init()


# Buttons
iceButton = pygame.Rect(150, 300, 100, 100)
fireButton = pygame.Rect(150, 450, 100, 100)
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

# Fonts
font = pygame.font.Font(None, 50)
littlefont = pygame.font.Font(None, 25)


def draw_text(text, font, color, surface, x, y):
  text_obj = font.render(text, True, color)
  text_rect = text_obj.get_rect()
  text_rect.center = (x, y)
  surface.blit(text_obj, text_rect)


class opening:

  def __init(self):
    self.weakness = 0
    self.running = True
    self.dif = 0
  
  
  def start_screen(self):
    while True:
      screen.fill(WHITE)
      draw_text("Welcome to My Game", font, BLACK, screen, SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 4)
      draw_text("Press Space to Start", font, BLACK, screen, SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2)
      draw_text("Press Esc to Quit", font, BLACK, screen, SCREEN_WIDTH / 2,
                SCREEN_HEIGHT * 3 / 4)
  
      pygame.display.flip()
  
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            # Start the game
            return
          elif event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
  
  
  def difficulty_selection(self):
    selected_difficulty = None
    while not selected_difficulty:
      screen.fill(WHITE)
      draw_text("Choose Difficulty", font, BLACK, screen, SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 4)
      draw_text("1. Easy", font, BLACK, screen, SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2 - 50)
      draw_text("2. Medium", font, BLACK, screen, SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2)
      draw_text("3. Hard", font, BLACK, screen, SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2 + 50)
      draw_text("4. Insane", font, BLACK, screen, SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2 + 100)
      draw_text("5. OK", font, BLACK, screen, SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2 + 150)
  
      pygame.display.flip()
  
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_1:
            selected_difficulty = "Easy"
            self.dif = 1
          elif event.key == pygame.K_2:
            selected_difficulty = "Medium"
            self.dif = 2
          elif event.key == pygame.K_3:
            selected_difficulty = "Hard"
            self.dif = 3
          elif event.key == pygame.K_4:
            selected_difficulty = "Insane"
            self.dif = 4
          elif event.key == pygame.K_5:
            selected_difficulty = "OK"
            self.dif = 5
  
    print("Selected Difficulty:", selected_difficulty)
  
  
  def character_customization(self):
    player_name = ""
    player_physique = None
  
    while not player_name or not player_physique:
      screen.fill(WHITE)
      draw_text("Enter Your Name:", font, BLACK, screen, SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 4)
      draw_text(player_name, font, BLACK, screen, SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 4 + 50)
  
      draw_text("Choose Physique:", font, BLACK, screen, SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2 - 50)
      draw_text("1. Glass Cannon", font, BLACK, screen, SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2)
      draw_text("2. Balanced", font, BLACK, screen, SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2 + 50)
      draw_text("3. Tank", font, BLACK, screen, SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2 + 100)
  
      pygame.display.flip()
  
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RETURN:
            if player_name and player_physique:
              print("Player Name:", player_name)
              print("Player Physique:", player_physique)
              return
          elif event.key == pygame.K_BACKSPACE:
            player_name = player_name[:-1]
          elif event.key == pygame.K_1:
            player_physique = "Glass Cannon"
            phys = 1
          elif event.key == pygame.K_2:
            player_physique = "Balanced"
            phys = 2
          elif event.key == pygame.K_3:
            player_physique = "Tank"
            phys = 3
          elif event.key in range(97, 123):  # A-Z
            player_name += event.unicode
  
  def weakness(self):
    screen.fill(WHITE)
    draw_text("What is your weakness?", font, BLACK, screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT/ 6)
    pygame.draw.rect(screen, (115, 177, 244), iceButton)
    draw_text("ice", font, BLACK,screen, SCREEN_WIDTH/2, 350)
    pygame.draw.rect(screen, (115, 177, 244), fireButton)
    draw_text("fire",font, BLACK,screen, SCREEN_WIDTH/2, 500)
    pygame.display.flip()
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            if iceButton.collidepoint(event.pos):
              self.weakness = 1
              p1.weakness = 1
              print("1")
              return
            elif fireButton.collidepoint(event.pos):
              self.weakness = 2
              p1.weakness = 2
              print("2")
              return
  
  
  
        
