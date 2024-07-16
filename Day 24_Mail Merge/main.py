NAMES_PATH = "Input/Names/invited_names.txt"
LETTER_PATH = "Input/Letters/starting_letter.txt"
OUTPUT_PATH = "Output/ReadyToSend/"
PLACEHOLDER_TEXT = "[name]"
EXTENSION = ".txt"

with open(NAMES_PATH) as names_file:
    names = names_file.read().splitlines()

with open(LETTER_PATH) as blueprint:
    text = blueprint.read()

for name in names:
    with open(f"{OUTPUT_PATH}Letter for {name}{EXTENSION}", mode="w") as new_letter:
        new_letter.write(text.replace(PLACEHOLDER_TEXT, name))
