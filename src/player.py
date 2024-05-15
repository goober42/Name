from gym import Gym

g1 = Gym()

class Player:

  def __init__(self):
    self.health = g1.pdur
    self.damage = g1.pstr
    self.speed = g1.pspeed
    self.weakness = 0

  def takedamage(self,damage):
    self.health = selfhealth-damage
