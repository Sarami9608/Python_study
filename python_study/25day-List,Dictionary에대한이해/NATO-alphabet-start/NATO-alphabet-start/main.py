import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == 'Angenla':
        print(row.score)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
# pandas를 활용한 csv 형태의 데이터 읽기
csv_data = pandas.read_csv(
    './python_study/25day-List,Dictionary에대한이해/NATO-alphabet-start/NATO-alphabet-start/nato_phonetic_alphabet.csv')
print(csv_data)
# 위에서 제안한 형태의 딕션어리 만들기
new_dictionary = {value.letter: value.code for (
    index, value) in csv_data.iterrows()}
print(new_dictionary)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
strings = input('Enter a word : ').upper()
new_list = [new_dictionary[letter] for letter in strings]
print(new_list)
