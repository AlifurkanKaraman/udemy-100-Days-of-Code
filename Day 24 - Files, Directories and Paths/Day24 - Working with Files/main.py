# For reading a file we use mode='r', it used as a default, so we can not write it.
with open("../../Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

# For overwriting a file we use mode='w'.
 with open("my_file.txt", mode='w') as file:
     file.write("HELLO.")

# For adding additional text to file, we use mode='a'. 'a' stays for append like we do in list.
 with open("my_file.txt", mode='a') as file:
     file.write('\nNew text.')

# If we choose file that doesn't exist in writing mode, its creates a new file.
 with open("new_file.txt", mode='w') as file:
     file.write("HEllo I'm a new file")