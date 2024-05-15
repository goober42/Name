import pygame
import keyboard
import sys
import time

from pygame.constants import K_ESCAPE

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

font = pygame.font.Font(None, 50)

littlefont = pygame.font.Font(None, 25)


def draw_text(text, font, color, surface, x, y):
  text = str(text)
  text_obj = font.render(text, True, color)
  text_rect = text_obj.get_rect()
  text_rect.center = (x, y)
  surface.blit(text_obj, text_rect)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

exw = 20
exh = 20
ex = pygame.display.set_mode((exw, exh))


class Gym:

  def __init__(self):
    self.running = True
    self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    self.pspeed = 5
    self.pdur = 100
    self.pstr = 5
    self.runcount = 0
    self.repcount = 0
    self.deadcount = 0    
    self.runButton_rect = pygame.Rect(((self.screen.get_width() // 2)-(1/4)*self.screen.get_width()) -75,
                                      275, 150, 100)
    self.deadButton_rect = pygame.Rect((self.screen.get_width() // 2)-75 , 275,
                                       150, 100)
    self.liftButton_rect = pygame.Rect(((self.screen.get_width()) - (1/4) * self.screen.get_width()) - 75, 275,
                                       150, 100)
    self.speedButton_rect = pygame.Rect(((self.screen.get_width() // 2)-75) , 275, 150, 100)
    self.dlButton_rect = pygame.Rect(((self.screen.get_width() // 2)-75) , 275, 150, 100)
    self.stayButton_rect = pygame.Rect(((self.screen.get_width() // 2)-(1/4)*self.screen.get_width()) -75,
                                      275, 150, 150)
    self.leaveButton_rect = pygame.Rect(((self.screen.get_width()) - (1/4) * self.screen.get_width()) - 75, 275,
                                       150, 150)
    self.dliftButton_rect = pygame.Rect(((self.screen.get_width() // 2)-75) , 275, 150, 100)
    self.nliftButton_rect = pygame.Rect(((self.screen.get_width() // 2)-75) , 275, 150, 100)

    self.w1Button_rect = pygame.Rect(150, 100, 100, 100)
    self.w2Button_rect = pygame.Rect(150, 250, 100, 100)
    self.w3Button_rect = pygame.Rect(150, 400, 100, 100)

  def MaxStat(self):
    self.screen.fill(WHITE)
    draw_text("You have maxed out this stat", font, BLACK, screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/6)
    draw_text("Would you like to go back to the gym entrance or leave the gym?", littlefont, BLACK, screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/3)
    pygame.draw.rect(self.screen, BLUE , self.stayButton_rect)
    draw_text("Stay", font, BLACK, self.screen, SCREEN_WIDTH/2 - ((1/4)*SCREEN_WIDTH), 350)
    pygame.draw.rect(self.screen, BLUE, self.leaveButton_rect)
    draw_text("Leave", font, BLACK, self.screen, SCREEN_WIDTH - ((1/4)*SCREEN_WIDTH), 350)
    pygame.display.flip()
    while self.running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False
          pygame.quit()
          sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            if self.stayButton_rect.collidepoint(event.pos):
              self.EnterGym()
            elif self.leaveButton_rect.collidepoint(event.pos):
              from logic import logic
              l = logic()
              l.screen()

  def EnterGym(self):
    screen.fill(WHITE)
    pygame.display.flip()
    draw_text("You Are Now in The Gym", font, BLACK, screen, SCREEN_WIDTH / 2,
              SCREEN_HEIGHT / 6)
    draw_text(
        "You can train speed by running,"
        "durability by deadlifting,"
        "and strength by lifting weights",
        littlefont, BLACK, screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2.75)
    draw_text("what would you like to do?", font, BLACK, screen,
              SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 4))
    pygame.draw.rect(self.screen, (115, 177, 244), self.runButton_rect)
    pygame.draw.rect(self.screen, (115, 177, 244), self.deadButton_rect)
    pygame.draw.rect(self.screen, (115, 177, 244), self.liftButton_rect)
    pygame.display.flip()
    self.Choice()

  def Choice(self):
    while self.running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False
          pygame.quit()
          sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            if self.runButton_rect.collidepoint(event.pos):
              if self.pspeed == 15:
                self.EnterGym()
              else:
                self.Running()
            elif self.deadButton_rect.collidepoint(event.pos):
              if self.pdur >= 310:
                self.EnterGym()
              else:
                self.DeadLifts()
            elif self.liftButton_rect.collidepoint(event.pos):
              if self.pstr >= 20:
                self.EnterGym()
              else:
                self.Lifting()

      self.hello_text = font

  def Running(self):
    screen.fill(WHITE)
    pygame.display.set_caption("Running")
    draw_text("Running", font, BLACK, screen, SCREEN_WIDTH / 2,
              SCREEN_HEIGHT / 4)
    draw_text("Press SPACEBAR to train", littlefont, BLACK, screen,
              SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    pygame.display.flip()
    while self.running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
              self.EnterGym()
          elif event.key == pygame.K_SPACE:
            print("you are running")
            self.running = True
            screen.fill(WHITE)
            if screen:
              while self.running:

                # Draw a rectangle
                rect_width, rect_height = 200, 100
                rect_x, rect_y = (SCREEN_WIDTH - rect_width) // 2, ((SCREEN_HEIGHT - rect_height) // 2)+200
                pygame.draw.rect(screen, WHITE, (rect_x, rect_y, rect_width, rect_height))

                # Draw the updated text on top of the rectangle
                draw_text(self.runcount, font, BLACK, screen, rect_x + 100, rect_y + 25)
                draw_text(self.pspeed, font, BLACK, screen, rect_x + 100, rect_y + 75)

                pygame.display.flip()
                for event in pygame.event.get():
                  pygame.display.flip()
                  draw_text("You Are Running Now",font, BLACK, screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT/6)
                  pygame.draw.rect(self.screen, (115, 177, 244), self.speedButton_rect)
                  pygame.display.flip()
                  if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                  elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                      if self.speedButton_rect.collidepoint(event.pos):
                        self.runcount = self.runcount + 1
                        if self.runcount == 20:
                          self.runcount = 0
                          self.pspeed = self.pspeed + 1
                          print(self.pspeed)
                          print(self.runcount)
                          if self.pspeed == 15:
                            self.MaxStat()

  def DeadLifts(self):
    screen.fill(WHITE)
    pygame.display.set_caption("DeadLifts")
    draw_text("DeadLifts", font, BLACK, screen, SCREEN_WIDTH / 2,
              SCREEN_HEIGHT / 4)
    draw_text("Press SPACEBAR to train", littlefont, BLACK, screen,
              SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    pygame.display.flip()
    while self.running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
              self.EnterGym()
          elif event.key == pygame.K_SPACE:
            print("you are Lifting Now")
            self.running = True
            screen.fill(WHITE)
            while self.running:
              for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  self.running = False
                  pygame.quit()
                  sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                  if event.button == 1:
                    if self.pdur < 150:
                      screen.fill(WHITE)
                      pygame.draw.rect(screen, (115, 177, 244), self.w1Button_rect)
                      draw_text("100 pounds", font, BLACK,screen, SCREEN_WIDTH/2, 150)
                      pygame.draw.rect(screen, BLACK, self.w2Button_rect)
                      draw_text("LOCKED",font, BLACK,screen, SCREEN_WIDTH/2, 300)
                      pygame.draw.rect(screen, BLACK, self.w3Button_rect)
                      draw_text("LOCKED", font, BLACK,screen, SCREEN_WIDTH/2, 450)
                      pygame.display.flip()
                      if self.w1Button_rect.collidepoint(event.pos):
                        print("good")
                        self.W1()
                      elif self.w2Button_rect.collidepoint(event.pos):
                        print("no")
                      elif self.w3Button_rect.collidepoint(event.pos):
                        print("no")
                    elif self.pdur >= 150 and self.pdur < 200:
                      screen.fill(WHITE)
                      pygame.draw.rect(screen, (115, 177, 244), self.w1Button_rect)
                      draw_text("100 pounds", font, BLACK,screen, SCREEN_WIDTH/2, 150)
                      pygame.draw.rect(screen, (155,177,244), self.w2Button_rect)
                      draw_text("150 pounds",font, BLACK ,screen, SCREEN_WIDTH/2, 300)
                      pygame.draw.rect(screen, BLACK, self.w3Button_rect)
                      draw_text("LOCKED", font, BLACK,screen, SCREEN_WIDTH/2, 450)
                      if self.w1Button_rect.collidepoint(event.pos):
                        print("good")
                        self.W1()
                      elif self.w2Button_rect.collidepoint(event.pos):
                        print("good")
                        self.W2()
                      elif self.w3Button_rect.collidepoint(event.pos):
                        print("no")
                      pygame.display.flip()
                    elif self.pdur >= 200:
                      screen.fill(WHITE)
                      pygame.draw.rect(screen, (115, 177, 244), self.w1Button_rect)
                      draw_text("100 pounds", font, BLACK,screen, SCREEN_WIDTH/2, 150)
                      pygame.draw.rect(screen, (115, 177, 244), self.w2Button_rect)
                      draw_text("150 pounds",font, BLACK,screen, SCREEN_WIDTH/2, 300)
                      pygame.draw.rect(screen, (115, 177, 244), self.w3Button_rect)
                      draw_text("200 pounds", font, BLACK,screen, SCREEN_WIDTH/2, 450)
                      if self.w1Button_rect.collidepoint(event.pos):
                        print("good")
                        self.W1()
                      elif self.w2Button_rect.collidepoint(event.pos):
                        print("good")
                        self.W2()
                      elif self.w3Button_rect.collidepoint(event.pos):
                        print("good")
                        self.W3()
                      pygame.display.flip()

  def NW(self):
    screen.fill(WHITE)
    draw_text("You have unlocked a new weight", font, BLACK, screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/6)
    draw_text("would you like to continue using this weight, or use the new one?", littlefont, BLACK, screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/3)
    pygame.draw.rect(self.screen, BLUE , self.stayButton_rect)
    draw_text("New", font, BLACK, self.screen, SCREEN_WIDTH/2 - ((1/4)*SCREEN_WIDTH), 350)
    pygame.draw.rect(self.screen, BLUE, self.leaveButton_rect)
    draw_text("Continue", font, BLACK, self.screen, SCREEN_WIDTH - ((1/4)*SCREEN_WIDTH), 350)
    pygame.display.flip()
    while self.running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False
          pygame.quit()
          sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            if self.stayButton_rect.collidepoint(event.pos):
              self.DeadLifts()
            elif self.leaveButton_rect.collidepoint(event.pos):
              pass



  def W1(self):
    screen.fill(WHITE)
    while self.running:
      rect_width, rect_height = 200, 100
      rect_x, rect_y = (SCREEN_WIDTH - rect_width) // 2, ((SCREEN_HEIGHT - rect_height) // 2)+200
      pygame.draw.rect(screen, WHITE, (rect_x, rect_y, rect_width, rect_height))

      # Draw the updated text on top of the rectangle
      draw_text(self.deadcount, font, BLACK, screen, rect_x + 100, rect_y + 25)
      draw_text(self.pdur, font, BLACK, screen, rect_x + 100, rect_y + 75)

      pygame.display.flip()
      for event in pygame.event.get():
        pygame.display.flip()
        pygame.draw.rect(self.screen, (115, 177, 244), self.dlButton_rect)
        pygame.display.flip()
        if event.type == pygame.QUIT:
          self.running = False
          pygame.quit()
          sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            if self.dlButton_rect.collidepoint(event.pos):
              self.deadcount = self.deadcount + 1
              if self.deadcount == 20:
                self.deadcount = 0
                self.pdur = self.pdur + 10
                print(self.pdur)
                print(self.deadcount)
                if self.pdur == 150:
                  self.NW()
                if self.pdur == 250:
                  self.MaxStat()

  def W2(self):
    screen.fill(WHITE)
    while self.running:
      rect_width, rect_height = 200, 100
      rect_x, rect_y = (SCREEN_WIDTH - rect_width) // 2, ((SCREEN_HEIGHT - rect_height) // 2)+200
      pygame.draw.rect(screen, WHITE, (rect_x, rect_y, rect_width, rect_height))

      # Draw the updated text on top of the rectangle
      draw_text(self.deadcount, font, BLACK, screen, rect_x + 100, rect_y + 25)
      draw_text(self.pdur, font, BLACK, screen, rect_x + 100, rect_y + 75)

      pygame.display.flip()
      for event in pygame.event.get():
        pygame.display.flip()
        pygame.draw.rect(self.screen, (115, 177, 244), self.dlButton_rect)
        pygame.display.flip()
        if event.type == pygame.QUIT:
          self.running = False
          pygame.quit()
          sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            if self.dlButton_rect.collidepoint(event.pos):
              self.deadcount = self.deadcount + 1
              if self.deadcount == 20:
                self.deadcount = 0
                self.pdur = self.pdur + 20
                print(self.pdur)
                print(self.deadcount)
                if self.pdur == 210:
                  self.NW()
                if self.pdur == 300:
                  self.MaxStat()

  def W3(self):
    screen.fill(WHITE)
    while self.running:
      rect_width, rect_height = 200, 100
      rect_x, rect_y = (SCREEN_WIDTH - rect_width) // 2, ((SCREEN_HEIGHT - rect_height) // 2)+200
      pygame.draw.rect(screen, WHITE, (rect_x, rect_y, rect_width, rect_height))

      # Draw the updated text on top of the rectangle
      draw_text(self.deadcount, font, BLACK, screen, rect_x + 100, rect_y + 25)
      draw_text(self.pdur, font, BLACK, screen, rect_x + 100, rect_y + 75)

      pygame.display.flip()
      for event in pygame.event.get():
        pygame.display.flip()
        pygame.draw.rect(self.screen, (115, 177, 244), self.dlButton_rect)
        pygame.display.flip()
        if event.type == pygame.QUIT:
          self.running = False
          pygame.quit()
          sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            if self.dlButton_rect.collidepoint(event.pos):
              self.deadcount = self.deadcount + 1
              if self.deadcount == 20:
                self.deadcount = 0
                self.pdur = self.pdur + 25
                print(self.pdur)
                print(self.deadcount)
                if self.pdur >= 300:
                  self.MaxStat()

  def Lifting(self):
    screen.fill(WHITE)
    pygame.display.set_caption("Lifting")
    draw_text("Lifting", font, BLACK, screen, SCREEN_WIDTH / 2,
              SCREEN_HEIGHT / 4)
    draw_text("Press SPACEBAR to train", littlefont, BLACK, screen,
              SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    pygame.display.flip()
    while self.running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
              self.EnterGym()
          elif event.key == pygame.K_SPACE:
            print("you are lifting")
            self.running = True
            screen.fill(WHITE)
            if screen:
              while self.running:

                # Draw a rectangle
                rect_width, rect_height = 200, 100
                rect_x, rect_y = (SCREEN_WIDTH - rect_width) // 2, ((SCREEN_HEIGHT - rect_height) // 2)+200
                pygame.draw.rect(screen, WHITE, (rect_x, rect_y, rect_width, rect_height))

                # Draw the updated text on top of the rectangle
                draw_text(self.repcount, font, BLACK, screen, rect_x + 100, rect_y + 25)
                draw_text(self.pstr, font, BLACK, screen, rect_x + 100, rect_y + 75)

                pygame.display.flip()
                for event in pygame.event.get():
                  pygame.display.flip()
                  draw_text("You Are Lifting Now",font, BLACK, screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT/6)
                  pygame.draw.rect(self.screen, (115, 177, 244), self.nliftButton_rect)
                  pygame.display.flip()
                  if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                  elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                      if self.nliftButton_rect.collidepoint(event.pos):
                        self.repcount = self.repcount + 1
                        if self.repcount == 20:
                          self.repcount = 0
                          self.pstr = self.pstr + 1
                          print(self.pstr)
                          print(self.repcount)
                          if self.pstr == 15:
                            self.MaxStat()
