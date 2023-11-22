# Program prompts user for the answer to the Great Question of Life, the Universe and Everything
answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

# Removes any spaces from the user's input and convert it to lowercase
answer = answer.replace(" ", "").lower()

# Condition checks if the answer is 42 or forty-two or forty two
if answer == "42" or answer == "forty-two" or answer == "fortytwo":
    # Output Yes if above condition is met
    print("Yes")
else:
    # Output No if above condition is not met
    print("No")