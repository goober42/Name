class Enemy:
  def __init__(self, name, health, damage):
      self.name = name
      self.health = health
      self.damage = damage

  def attack(self):
      return self.damage

  def take_damage(self, damage):
      self.health -= damage


class BaseEnemy(Enemy):
  def __init__(self):
      super().__init__(name="Base Enemy", health=100, damage=20)


class FireEnemy(Enemy):
  def __init__(self):
      super().__init__(name="Fire Enemy", health=120, damage=15)

  def attack(self):
      return self.damage

  def apply_fire_debuff(self):
      return 5  # For example, this could return the number of turns the fire debuff lasts


class StrongEnemy(Enemy):
  def __init__(self):
      super().__init__(name="Strong Enemy", health=150, damage=30)


class HealerEnemy(Enemy):
  def __init__(self):
      super().__init__(name="Healer Enemy", health=100, damage=0)

  def heal(self):
      return 20  # For example, this could return the amount of health the healer restores to other enemies