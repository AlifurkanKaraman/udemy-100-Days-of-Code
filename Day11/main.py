############### Blackjack Project #####################
import random
from art import logo
from replit import clear


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return f"You went over. You lose 😤"
    if user_score == computer_score:
        return f"Draw 🙃"
    elif computer_score == 0:
        return f"Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return f"Win with a Blackjack 😎"
    elif user_score > 21:
        return f"You went over. You lose 😭"
    elif computer_score > 21:
        return f"Opponent went over. You win 😁"
    elif user_score > computer_score:
        return f"You win 😃"
    else:
        return f"You lose 😤"


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    print(logo)
    

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\tYour cards: {user_cards}, current score: {user_score}")
        print(f"\tDealer's first card: {computer_cards[0]}")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            is_game_over = True
        else:
            get_or_pass = input("Type 'y' to get another card, type 'n' to pass: ")
            if get_or_pass == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\tYour final hand: {user_cards}, final score: {user_score}")
    print(f"\tDealer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()

