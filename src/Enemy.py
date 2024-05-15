from player import Player
from gym import Gym

p1 = Player()
g1 = Gym()

damage = g1.pdur

class Enemy:
  def __init__(self):
      self.name = ""
      self.health = ""
      self.damage = ""

  def attack(self, adamage):
      return self.damage

  def take_damage(self, damage):
      self.health -= damage


  def FireEnemy(self):
    self.name = "fire rat"
    if player.weakness == 1:
      self.damage = 5 * p1.dif
    elif player.weakness == 2:
      self.damage = (g1.damage/2)
      self.health = 90

  def NormalEnemy(self):
    self.name = "normal rat"
    self.health = 100
    self.damage = 10 * p1.dif

  def IceEnemy(self):
    self.name = "ice rat"
    self.health = 125
    if player.weakness == 1:
      self.damage = (g1.damage/2)
    elif player.weakness == 2:
      self.damage = 5 * p1.dif

  def BossEnemy(self):
    self.name = "boss rat"
    self.health = 50 * p1.dif
    self.damage = 50


    
