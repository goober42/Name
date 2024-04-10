import pygame
import sys
import random
import time
from Enemy import Enemy

# Initialize Pygame
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

# Fonts
font = pygame.font.Font(None, 50)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def start_screen():
    while True:
        screen.fill(WHITE)
        draw_text("Welcome to My Game", font, BLACK, screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/4)
        draw_text("Press Space to Start", font, BLACK, screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        draw_text("Press Esc to Quit", font, BLACK, screen, SCREEN_WIDTH/2, SCREEN_HEIGHT * 3/4)

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
def difficulty_selection():
    selected_difficulty = None
    while not selected_difficulty:
        screen.fill(WHITE)
        draw_text("Choose Difficulty", font, BLACK, screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/4)
        draw_text("1. Easy", font, BLACK, screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 50)
        draw_text("2. Medium", font, BLACK, screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        draw_text("3. Hard", font, BLACK, screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50)
        draw_text("4. Insane", font, BLACK, screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 100)
        draw_text("5. OK", font, BLACK, screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 150)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected_difficulty = "Easy"
                elif event.key == pygame.K_2:
                    selected_difficulty = "Medium"
                elif event.key == pygame.K_3:
                    selected_difficulty = "Hard"
                elif event.key == pygame.K_4:
                    selected_difficulty = "Insane"
                elif event.key == pygame.K_5:
                    selected_difficulty = "OK"

    print("Selected Difficulty:", selected_difficulty)

def character_customization():
  player_name = ""
  player_physique = None

  while not player_name or not player_physique:
      screen.fill(WHITE)
      draw_text("Enter Your Name:", font, BLACK, screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/4)
      draw_text(player_name, font, BLACK, screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/4 + 50)

      draw_text("Choose Physique:", font, BLACK, screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 50)
      draw_text("1. Glass Cannon", font, BLACK, screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
      draw_text("2. Balanced", font, BLACK, screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50)
      draw_text("3. Tank", font, BLACK, screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 100)

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
start_screen()
difficulty_selection()
character_customization()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Player on New York Map")

# Load player sprite
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("New York City")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Load player sprite
player_image = pygame.image.load("player.png")
player_rect = player_image.get_rect()

map_image = pygame.image.load("basemap.png")
map_rect = map_image.get_rect()

# Generate initial map
MAP_WIDTH = 3000
MAP_HEIGHT = 3000
MAP_SIZE = (MAP_WIDTH, MAP_HEIGHT)

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    # Calculate the offset to center the player in the screen

    player_rect.x = max(0, min(player_rect.x, MAP_WIDTH - player_rect.width))
    player_rect.y = max(0, min(player_rect.y, MAP_HEIGHT - player_rect.height))

  # Draw the visible portion of the map
    screen.blit(map_image, (-player_rect.x, -player_rect.y))

  # Draw the player
    screen.blit(player_image, player_rect)

  # Update the display
    pygame.display.flip()

    move_up = False
    move_down = False
    move_left = False
    move_right = False
  
      # Event handling for continuous movement
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False
          elif event.type == pygame.KEYDOWN:
              # Set the movement flags to True when a key is pressed
              if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                  move_left = True
              elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                  move_right = True
              elif event.key == pygame.K_UP or event.key == pygame.K_w:
                  move_up = True
              elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                  move_down = True
          elif event.type == pygame.KEYUP:
              # Set the movement flags to False when a key is released
              if event.key != pygame.K_LEFT or event.key == pygame.K_a:
                  move_left = False
              elif event.key != pygame.K_RIGHT or event.key == pygame.K_d:
                  move_right = False
              elif event.key != pygame.K_UP or event.key == pygame.K_w:
                  move_up = False
              elif event.key != pygame.K_DOWN or event.key == pygame.K_s:
                  move_down = False
  
    # Move the player continuously based on movement flags
    if move_left:
        player_rect.x -= 10
    if move_right:
        player_rect.x += 10
    if move_up:
        player_rect.y -= 10
    if move_down:
        player_rect.y += 10
  
      # Update the display
    pygame.display.flip()
  
      # Cap the frame rate
    pygame.time.Clock().tick(60)


  # 269 - 375 is the x
  # 56 - 75 is the y
    HOUSE_MAP_WIDTH = 712
    HOUSE_MAP_HEIGHT = 826
    HOUSE_MAP_SIZE = (HOUSE_MAP_WIDTH, HOUSE_MAP_HEIGHT)

    HOUSE_MAP = pygame.image.load("homemap.png")
  
    if player_rect.x > 269 and player_rect.x < 375 and player_rect.y < -56 and player_rect.y > -75:
      print("house")
      screen.fill(WHITE)
      draw_text("Would you like to enter your house?", font, BLACK, screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/4)
      draw_text("1. Yes", font, BLACK, screen, SCREEN_WIDTH/2-100, SCREEN_HEIGHT/2)
      draw_text("2. No", font, BLACK, screen, SCREEN_WIDTH/2+100, SCREEN_HEIGHT/2)
      pygame.display.flip()

      for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
              print("yes")
              draw_text("You enter your house", font, BLACK, screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/10)
              time.sleep(3)
              screen.blit(HOUSE_MAP, (offset_x, offset_y), (player_rect.x, player_rect.y, SCREEN_WIDTH, SCREEN_HEIGHT))

              player_rect.x = max(0, min(player_rect.x, HOUSE_MAP_WIDTH - player_rect.width))
              player_rect.y = max(0, min(player_rect.y, HOUSE_MAP_HEIGHT - player_rect.height))
              
  
  # Quit Pygame
pygame.quit()
sys.exit()