import random
from replit import clear
from art import logo, vs
from game_data import data

score = 0
a = random.choice(data)
b = random.choice(data)

# We do it to prevent similar data
while b == a:
    b = random.choice(data)

def compare_print(a, b):
    print(f'Compare A: {a["name"]}, a{a["description"]}, from {a["country"]}.')
    print(vs)
    print(f'Against B: {b["name"]}, a{b["description"]}, from {b["country"]}.')

def compare(guess, x, y):
    global score
    global a, b
    if x['follower_count'] > y['follower_count']:
        if guess == 'a':
            score += 1
        else:
            return 0
    else:
        if guess == 'b':
            score += 1
        else:
            return 0
    
    a = b
    b = random.choice(data)
    while b == a:
        b = random.choice(data)
            
    return score

def game():
    clear()
    global a, b
    final_score = 1
    while final_score != 0:    
        print(logo)
        if score > 0:
            print(f"You're right! Current score: {score}.")


        compare_print(a, b)
        user_guess = input("Who has more followers? Type 'A' or 'B':").lower()
        final_score = compare(user_guess, a, b)

        if final_score == 0:
            clear()
            print(f"Sorry, that's wrong. Final score: {score}")
        else:
            clear()


while input("Do you want to play Higher-Lower Game? Type 'y' for yes or 'n' for no: ").lower() == 'y':
    game()
