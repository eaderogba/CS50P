def main():
    # Prompt the user to input a string
    usr_emotion = input("Write how you feel: ")

    # Call the 'convert' function to replace emoticons with emojis
    converted_emotion = convert(usr_emotion)

    # Print the original and converted strings
    print("Converted input:", converted_emotion)

# Define a function called 'convert' that takes an input string 'input_str'
def convert(input_str):
    # Replace occurrences of ":)" with "🙂", and ":(", with  "🙁" in the input string
    converted_str = input_str.replace(":)", "🙂").replace(":(", "🙁")

    # Return the string with emoticon replacements
    return converted_str

main()