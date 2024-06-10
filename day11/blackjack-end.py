import random
from art import logo


def clear():
    print("\n" * 20)


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    new_card = random.choice(cards)
    return new_card


def get_score(hand):
    total_score = 0
    for card in hand:
        if card == 11:
            if total_score == 21 and len(hand) == 2:
                return 0
            elif total_score > 21:
                total_score += 1
            else:
                total_score += 11
        else:
            total_score += card
    return total_score


def game_result(player_score, dealer_score):
    if player_score == dealer_score:
        return "Draw 🙃"
    elif player_score > 21 and dealer_score > 21:
        return "You went over. You lose 😤"
    elif dealer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif player_score == 0:
        return "Win with a Blackjack 😎"
    elif player_score > 21:
        return "You went over. You lose 😭"
    elif dealer_score > 21:
        return "Opponent went over. You win 😁"
    elif player_score > dealer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def game_play():
    print(logo)
    player_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card(), deal_card()]
    game_over = False

    while not game_over:
        print(f"Your cards: {player_cards}, current score: {get_score(player_cards)}")
        print(f"Computer's first card: {dealer_cards[0]}")

        if get_score(player_cards) == 0 or get_score(dealer_cards) == 0 or get_score(player_cards) > 21:
            game_over = True
        else:
            action = input("Type 'y' to get another card, type 'n' to pass:")
            if action.lower() == "y":
                player_cards.append(deal_card())
            else:
                game_over = True

        while get_score(dealer_cards) != 0 and get_score(dealer_cards) < 17:
            dealer_cards.append(deal_card())

    print(f"Your final hand: {player_cards}, final score: {get_score(player_cards)}")
    print(f"   Computer's final hand: {dealer_cards}, final score: {get_score(dealer_cards)}")
    print(game_result(get_score(player_cards), get_score(dealer_cards)))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    game_play()




