from sense_hat import SenseHat

sense = SenseHat()
while True:
  raw = sense.get_compass_raw()
  x = raw["x"]
  y = raw["y"]
  z = raw["z"]

  field_strength = 0 # TODO - calculate the magnetic field

  print(x, y, z, field_strngth)
