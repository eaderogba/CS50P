# Define the body of the code
def main():

    # Prompt the user to enter the mass
    mass = int(input("Enter Mass to be converted: "))
    # Call the enerfy_joules function to convert the mass to energy
    converted_mass = energy_joules(mass)
    # Print the result of the user input
    print("Your energy equivalent is", converted_mass)

# Define a function to convert user input to energy
def energy_joules(n):

    # Artithmetic to calculate energy (joules) using E = mc^2
    energy = n*300000000*300000000
    return energy

main()