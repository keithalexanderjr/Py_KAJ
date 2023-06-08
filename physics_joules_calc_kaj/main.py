#Keith Alexander Jr
#Joules Physics Calculation

train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 
#function created to convert temp. Fahrenheit to Celsius
def f_to_c(f_temp):
  cel_deg = (f_temp - 32) * 5/9
  return cel_deg

#use case of 100 degrees fahrenheit
f100_in_celsius = f_to_c(100)

print(f100_in_celsius)

print("-------------------------")

#function created to convert temp. Celsius to Fahrenheit
def c_to_f(c_temp):
    fahren = (c_temp * (9/5)) + 32
    return fahren

c0_in_fahrenheit = c_to_f(0)

print(c0_in_fahrenheit)

print("-------------------------")


def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)

print(train_force)

print("The GE train supplies " + str(train_force) + " Newtons of force")

print("-------------------------")

def get_energy(mass, c=3*10**8):
  return mass * c**2

bomb_energy = get_energy(bomb_mass)

print(bomb_energy)

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

print("-------------------------")

def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    return force * distance
  #return ((mass * acceleration) * distance)

train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters")
