import pygame, keyboard

import pygame
import sys
import random

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

# Function to draw random streets
def draw_streets():
  for _ in range(500):  # Adjust the number of streets as needed
      x1 = random.randint(0, MAP_WIDTH)
      y1 = random.randint(0, MAP_HEIGHT)
      x2 = random.randint(0, MAP_WIDTH)
      y2 = random.randint(0, MAP_HEIGHT)
      pygame.draw.line(map_surface, BLACK, (x1, y1), (x2, y2), 5)  # Adjust line thickness as needed

# Generate initial map
draw_streets()

# Main game loop
running = True
while running:
  screen.fill(WHITE)

  # Calculate the offset to center the player in the screen
  offset_x = SCREEN_WIDTH // 2 - player_rect.centerx
  offset_y = SCREEN_HEIGHT // 2 - player_rect.centery

  # Blit the visible portion of the map onto the screen
  screen.blit(map_surface, (offset_x, offset_y), (player_rect.x, player_rect.y, SCREEN_WIDTH, SCREEN_HEIGHT))

  # Draw player at the center of the screen
  screen.blit(player_image, (SCREEN_WIDTH // 2 - player_rect.width // 2, SCREEN_HEIGHT // 2 - player_rect.height // 2))

  pygame.display.flip()

  # Event handling
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
      elif event.type == pygame.KEYDOWN:
          # Move the player based on arrow keys
          if event.key == pygame.K_LEFT:
              player_rect.x -= 10
          elif event.key == pygame.K_RIGHT:
              player_rect.x += 10
          elif event.key == pygame.K_UP:
              player_rect.y -= 10
          elif event.key == pygame.K_DOWN:
              player_rect.y += 10

  # Clamp player position to the map boundaries
  player_rect.x = max(0, min(player_rect.x, MAP_WIDTH - player_rect.width))
  player_rect.y = max(0, min(player_rect.y, MAP_HEIGHT - player_rect.height))

# Quit Pygame
pygame.quit()
sys.exit()