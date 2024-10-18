import pandas

our_dict = {row.letter: row.code for (index, row) in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}


def Nato_Converter():
    user_input = input("Enter a word: ").upper()
    try:
        our_list = [our_dict[letter] for letter in user_input]

    except KeyError:
        print("Sorry, only letters in the alphabet please")
        Nato_Converter()

    else:
        print(our_list)

Nato_Converter()