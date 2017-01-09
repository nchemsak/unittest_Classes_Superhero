from superhero import *
from flying import *
from running import *
from swimming import *
from sidekick import *
from bulletproof import *

class Superman(Superhero, Flying, Running, Swimming, Bulletproof):

  def __init__(self):
    Superhero.__init__(self, "Superman")
    Bulletproof.__init__(self)
    self.air_speed = 1000000
    self.water_speed = 250


