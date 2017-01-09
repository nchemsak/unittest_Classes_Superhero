class Superhero(object):

    def __init__(self, name):
      self.powers = set()
      self.name = name
      self.gender = ""
      self.super_friends = set()
      self.evil_enemies = set()
      self.sidekicks = set()
      self.weaknesses = set()
      self.lair = ""
      self.biological_parents = tuple()

    def fight(self):
      pass

    def get_powers(self):
      return self.powers

    def add_power(self, new_power):
      self.powers.add(new_power)

    def remove_power(self, power_to_remove):
      self.powers.remove(power_to_remove)

    def __str__(self):
      power_output = ""

      for power in self.get_powers():
        power_output += power + ","

      return "{} the superhero with the powers: {}".format(self.name, power_output[0:-1])
