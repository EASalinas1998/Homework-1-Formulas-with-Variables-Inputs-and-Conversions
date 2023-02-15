#########################
# CSCI 1380.04
# Spring 2022
# Homework 01
# Eduardo Salinas
#########################

# Declares PI to value 3.14.
PI = 3.14

# Declares radius_input to be an input.
radius_input = input("Enter a radius: ")

# Declares radius as radius_input in integer format.
radius = int(radius_input)

# Declares area_circle variable equation.
area_circle = (PI * radius**2)

# Displays the inputted radius and area_circle equation.
print(f"The area of a circle with radius = {radius} is {area_circle}")

# Declares SPEED_OF_LIGHT formula.
SPEED_OF_LIGHT = 3 * 10**8

# Declares mass_input to be an input.
mass_input = input("Enter a mass: ")

# Declares mass as mass_input in float format.
mass = float(mass_input)

# Declares mass_energy_equivalence variable equation.
mass_energy_equivalence = mass * SPEED_OF_LIGHT**2

# Displays the inputted mass and mass_energy_equivalence equation.
print(
    f"The value of Albert Einstein's mass-energy equivalence with mass = {mass} is {mass_energy_equivalence}"
)

# Declares UNIVERSAL_GRAVITATION_CONSTANT.
UNIVERSAL_GRAVITATION_CONSTANT = 6.673 * 10**-11

# Declares mass_1_input to be an input.
mass_1_input = input("Enter the first mass: ")

# Declares mass_1 as mass_1_input in float format.
mass_1 = float(mass_1_input)

# Declares mass_2_input to be an input.
mass_2_input = input("Enter the second mass: ")

# Declares mass_2 as mass_2_inputin float format.
mass_2 = float(mass_2_input)

# Declares distance_between_masses_input as an input.
distance_between_masses_input = input("Enter the distance between masses: ")

# Declares distance_between_masses as distance_between_masses_input float format.
distance_between_masses = float(distance_between_masses_input)

# Declares law_of_universal_gravitation variable equation.
law_of_universal_gravitation = UNIVERSAL_GRAVITATION_CONSTANT * mass_1 * mass_2 / distance_between_masses**2

# Displays the inputted mass_1, mass_2, distance_between_masses, and law_of_universal_gravitation variable equation.
print(
    f"The value of Isaac Newton's law of universal gravitation with mass_1 = {mass_1}, mass_2 = {mass_2}, and distance_between_masses = {distance_between_masses} is {law_of_universal_gravitation}"
)
