# Initial values for physics calculations
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Temperature conversion: Fahrenheit to Celsius
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9  # Formula: (F - 32) × 5/9
  return c_temp

f100_in_celsius = f_to_c(100)  # Convert 100°F to Celsius

# Temperature conversion: Celsius to Fahrenheit
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32  # Formula: C × 9/5 + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)  # Convert 0°C to Fahrenheit

# Newton's Second Law: Force = mass × acceleration
def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)

print("The GE train supplies " + str(train_force) + " Newtons of force.")

# Einstein's Energy Formula: E = mc²
def get_energy(mass, c = 3*10**8):  # c = speed of light
  return mass * c ** 2

bomb_energy = get_energy(bomb_mass)

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules")

# Work Formula: Work = Force × distance
def get_work(mass, acceleration, distance):
  return (mass * acceleration) * distance  # Force × distance

train_work = get_work(train_mass, train_acceleration, train_distance)

print('The GE train does ' + str(train_work) + ' Joules of work over ' + str(train_distance) + ' meters')