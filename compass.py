from sense_hat import SenseHat
import math

sense = SenseHat()
while True:
  raw = sense.get_compass_raw()
  x = raw["x"]
  y = raw["y"]
  z = raw["z"]

  field_strength = math.sqrt((x*x + y*y + z*z)) 

  print(field_strength)
