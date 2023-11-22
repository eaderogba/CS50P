# Program prompts user for a sentence
sentence = input("Enter a sentence: ")

# Sentence is converted to 'slowed down sentence by replacing spaces in the texts with ...
slowed_sentence = sentence.replace(' ', '...')

# Print the slowed down sentence
print("Your sentence, slowed down is:", slowed_sentence)