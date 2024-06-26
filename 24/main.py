# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names_list = []

with open("Input/Names/invited_names.txt") as names:
    for name in names:
        names_list.append(name.strip())

with open("Input/Letters/starting_letter.txt") as text:
    letter = text.read()

for name in names_list:
    invite = letter.replace("[name]", name)

    with open(f"Output/ReadyToSend/{name}.txt", mode="w") as txt:
        txt.write(invite)
