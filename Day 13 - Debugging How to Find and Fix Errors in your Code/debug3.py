for number in range(1, 101):
    # Firstly we should write 'and' instead of 'or'
    if number % 3 == 0 or number % 5 == 0:
        print("FizzBuzz")
    # Secondly we should write 'elif' instead of 'if' 
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    else:
        print([number]) # And finally we delete square brackets