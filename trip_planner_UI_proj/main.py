
def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 - " + name)

trip_planner_welcome("Keith")

#calculate a rounded time value based on a decimal for our user’s trip
def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

#user's trip will take approx. 2.6 hrs
estimate = estimated_time_rounded(2.6)

#printing user's trip information
def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  print("Your trip starts off in " + str(origin))
  print("And you are traveling to " + str(destination))
  print("You will be traveling by " + str(mode_of_transport))
  print("It will take approximately " + str(estimated_time) + " hours")

#user origin & destination
destination_setup("austin","houston", estimate)
