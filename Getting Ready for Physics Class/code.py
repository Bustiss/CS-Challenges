# You are a physics teacher preparing for the upcoming semester. You want to provide your students with some functions that will help them calculate some fundamental physical properties.

# Constants for train mass, acceleration and distance
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Function to convert Fahrenheit to Celsius
def f_to_c(f_temp): 
  c_temp = (f_temp - 32) * 5/9  # Formula to convert Fahrenheit to Celsius
  return c_temp

f100_in_celsius = f_to_c(100)  # Convert 100 degrees Fahrenheit to Celsius
print(f100_in_celsius)

# Function to convert Celsius to Fahrenheit
def c_to_f(c_temp): 
  f_temp = c_temp * (9/5) + 32  # Formula to convert Celsius to Fahrenheit
  return f_temp

c0_in_fahrenheit = c_to_f(0)  # Convert 0 degrees Celsius to Fahrenheit
print(c0_in_fahrenheit)

# Function to calculate force
def get_force(mass, acceleration):
  return mass * acceleration  # Formula to calculate force

train_force = get_force(train_mass, train_acceleration)  # Calculate force for the train
print("The GE train supplies " + str(train_force) +  " Newtons of force.")

# Function to calculate energy
def get_energy(mass, c = 3*10**8):
  return mass * c**2  # Formula to calculate energy

bomb_energy = get_energy(bomb_mass)  # Calculate energy for the bomb
print("A 1kg bomb supplies " + str(bomb_mass) +  " Joules")

# Function to calculate work
def get_work(mass,acceleration,distance):
  force = get_force(mass, acceleration)  # Calculate force
  work = force * distance  # Formula to calculate work
  return work
  
train_work = get_work(train_mass, train_acceleration, train_distance)  # Calculate work for the train

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")