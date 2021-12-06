PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    # With readlines() function we turn content inside file into list of contents
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        # strip() function delete string which inside parenthesis if it is in the name string
        stripped_name = name.strip('\n')
        # replace() function replace string that we don't want with string that we want
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode='w') as example:
            example.write(new_letter)
