""" # Program prompts the user for a greeting, converting to lowercases, and removing comma
answer = input("Enter a greeting: ").lower().replace(",", "")
# Splits user input, answer, into a list of words or substrings based on spaces
answer1 = answer.split()

for texts in answer1:
    #checks if the first word in the list is equal to the string "hello"
    if answer1[0] == "hello":
        print("$0")
        break

    #checks if the first character of the first word is "h."
    elif answer1[0][0:1] == "h":
        print("$20")
        break

    else:
        print("$100")
        break """

# bank.py

# Prompt the user for a greeting
greeting = input("Enter a greeting: ")

# Strip any leading whitespace and convert to lowercase
greeting = greeting.lstrip().lower()

# Check if the greeting starts with "hello"
if greeting.startswith("hello"):
    # Output $0
    print("$0")
# Check if the greeting starts with an "h" (but not "hello")
elif greeting.startswith("h"):
    # Output $20
    print("$20")
# Otherwise
else:
    # Output $100
    print("$100")
