import pandas as pd


student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass

# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pd.read_csv("nato_phonetic_alphabet.csv")

# data_dict = {}
# for (index, rows) in data.iterrows():
#     data_dict[rows.letter] = rows.code
data_dict = {rows.letter: rows.code for (index, rows) in data.iterrows()}


# 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    user_in = input("Enter the word: ").upper()
    # while not user_in.isalpha():
    #     print("Sorry, only letter sin the alphabet please.")
    #     user_in = input("Enter the word: ").upper()
    try:
        result = [data_dict[ch] for ch in user_in]
    except KeyError:
        print("Sorry, only letter sin the alphabet please.")
        generate_phonetic()
    else:
        print(result)


generate_phonetic()
