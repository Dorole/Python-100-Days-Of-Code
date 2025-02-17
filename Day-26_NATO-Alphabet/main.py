import pandas

data = pandas.read_csv("./nato_phonetic_alphabet.csv")

# required to convert the data from .csv to a dictionary using dict. comprehension, not .to_dict() method
alphabet_dict = {}
for (index, row) in data.iterrows():
    alphabet_dict[row.letter] = row.code

while True:
    user_input = input("Enter a word: ")

    if user_input.upper() == "OUT":
        break

    input_list = [letter.upper() if letter.isalpha() else letter for letter in user_input]
    code_list = [alphabet_dict[char] if char in alphabet_dict else "-" for char in input_list]

    print(code_list)
    print("(Enter 'out' to exit.)\n")

