import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data.to_dict())
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dict)
# new_dict = {new_key:new_value for (index, row) in student_data_frame.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def phonetic_generate():
  word= input("enter the word: ").upper()
  try:
    NATO_list = [phonetic_dict[letter] for letter in word]
  except KeyError:
    print("Sorry only alphabets can be used")
    phonetic_generate()
  else:
    print(NATO_list)

phonetic_generate()
