from sense_hat from SenseHat
import time
import math

# ask the user to provide some useful information about the device

platform _name = input("Please enter the name of the platform hosting the device")
platform_location = # TODO ask the user for the platform location


# TODO update details of the door / window the door sensor is hosted on
platform = {
   "name" : "",
   "locatedAt" : ""
}

# TODO ask the user for any details about the feature of interest if needed
foi_name = # TODO complete this

# details of the thing being observed
foi = {
  "name":"",
}
  
  
# TODO ask the user for any details about the sensor

# TODO Complete the details of the sensor
sensor = {
  id = "",
  type = "RPi Sense HAT based door / window sensor",
  madeObservation = []
}

sense = SenseHat()

# calculating the magnetic field strength
def calc_mag_field():
  raw = sense.get_compass_raw()
  x = raw["x"]
  y = raw["y"]
  z = raw["z"]
  sum_squares = 0 # TODO replace with code to calculate the sum of x squared, y squared, and z squared
  force = math.sqrt(num)
  return force
  
# get the current reading, assuming the door is open
baseline = calc_mag_field()

# current state
current_state = "OPEN"


# lets start making the observations
while True:
  try:
    # TODO get the current value
    # TODO - if the current value is greater than the (baseline + a threashold) and the current_state is "OPEN"
    # (experiment with values for threshold - start with 5000 and see if thats enough or if it needs to be larger)
      #  then change current_state to "CLOSED"
    
      # complete the template for the observations action and the result and add to
      observation = {
        # when the observation action finished - to be set when making observations
        "resultTime" : "",
        # the thing we're monitoring - i.e. the door / window
        "featureOfInterest" : foi
        # TODO change to something more relevant to what we're recording about the door / window
        "observedProperty" : "",
        # what was recorded
        "hasResult" :  {
            "value" : current_state
            } 
        # append observation to sensor["madeObservation"] list
      }
    # else if current_value is less than (baseline + threshold0 current_state is "CLOSED" 
     # then change the current_state to "OPEN" and append and observation to sensor["madeObservation"] list
  except KeyboardInterrupt:
    # exist the while loop, but before that, print sensor to see what it looks like
    print(sensor)
