from sense_hat import SenseHat
import datetime
import math

# ask the user to provide some useful information about the device

platform_name = input("Please enter the name of the platform hosting the device")
platform_location = input("Please enter the location of the platform")


# update details of the door / window the door sensor is hosted on
platform = {
   "name" : platform_name,
   "locatedAt" :platform_location
}

# ask the user for any details about the feature of interest if needed
foi_name = input("Enter a name for the door / window being monitored")

# details of the thing being observed
foi = {
  "name":foi_name,
}
  
  
# ask the user for any details about the sensor
sensor_name = input("Enter a name for the device")


# Complete the details of the sensor
sensor = {
  "id" : sensor_name,
  "type" : "RPi Sense HAT based door / window sensor",
  "madeObservation" : []
}

platform["hosts"] = [sensor]

sense = SenseHat()

# calculating the magnetic field strength
def calc_mag_field():
  raw = sense.get_compass_raw()
  x = raw["x"]
  y = raw["y"]
  z = raw["z"]
  sum_squares = x*x + y*y + z*z
  force = math.sqrt(sum_squares)
  return force
  
# get the current reading, assuming the door is open
baseline = calc_mag_field()

# current state
current_state = "OPEN"

# threshold for required change to baseline
mag_change_threshold = 60

# lets start making the observations
while True:
  try:
      # get the current mag field value
      field_strength = calc_mag_field()

      # if the current value is greater than the (baseline + a threashold) and the current_state is "OPEN"
      # (experiment with values for threshold - start with 5000 and see if thats enough or if it needs to be larger)
      #  then change current_state to "CLOSED"
      if field_strength > (baseline + mag_change_threshold) and current_state == "OPEN":
          current_state = "CLOSED"
    
          # complete the template for the observations action and the result and add to
          observation = {
              # when the observation action finished - to be set when making observations
              "resultTime" : datetime.datetime.now().isoformat(),
              # the thing we're monitoring - i.e. the door / window
              "featureOfInterest" : foi,
              # change to something more relevant to what we're recording about the door / window
              "observedProperty" : "State",
              # what was recorded
              "hasResult" :  {
                  "value" : current_state
              }
          }
          # append observation to sensor["madeObservation"] list
          sensor["madeObservation"].append(observation)
      # else if current_value is less than (baseline + threshold0 current_state is "CLOSED" 
      # then change the current_state to "OPEN" and append and observation to sensor["madeObservation"] list
      elif field_strength < (baseline + mag_change_threshold) and current_state == "CLOSED":
         current_state = "OPEN"
         # complete the template for the observations action and the result and add to
         observation = {
             # when the observation action finished - to be set when making observations
             "resultTime" : datetime.datetime.now().isoformat(),
             # the thing we're monitoring - i.e. the door / window
             "featureOfInterest" : foi,
             # change to something more relevant to what we're recording about the door / window
             "observedProperty" : "State",
             # what was recorded
             "hasResult" :  {
                 "value" : current_state
             }
         }
         # append observation to sensor["madeObservation"] list
         sensor["madeObservation"].append(observation)
    
     
  except KeyboardInterrupt:
    # exist the while loop, but before that, print sensor to see what it looks like
    print(sensor)
    exit()
