import random

card_objects = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_cards():
    for i in range(2):
        card = random.choice(card_objects)
        if card == 11:
            if calculate_points(player_hand) + card > 21:
                player_hand.append(1)
            else:
                player_hand.append(card)
        else:
            player_hand.append(card)
    for i in range(2):
        card = random.choice(card_objects)
        if card == 11:
            if calculate_points(computer_hand) + card > 21:
                computer_hand.append(1)
            else:
                computer_hand.append(card)
        else:
            computer_hand.append(card)
    return


def draw_card(character):
    card = random.choice(card_objects)
    if card == 11:
        if calculate_points(character) + card > 21:
            character.append(1)
        else:
            character.append(card)
    else:
        i = 0
        while calculate_points(character) + card > 21:
            if character[i] == 11:
                character[i] = 1
            if i == len(character) - 1:
                break
            i += 1
        character.append(card)
    return card


def calculate_points(charcter):
    total = 0
    for card in charcter:
        total += card
    return total


end_game = False
while not end_game:
    computer_hand = []
    player_hand = []
    deal_cards()

    computer_hand_show = ["*", computer_hand[1]]

    print(computer_hand_show)
    print(player_hand)

    while calculate_points(player_hand) < 21:
        draw_choice = input("Would you like to draw or stand? (d/s) ")
        if draw_choice == "d":
            print(f"Player draw a {draw_card(player_hand)}")
            print(computer_hand_show)
            print(player_hand)
        elif draw_choice == "s":
            break

    if calculate_points(player_hand) > 21:
        print("Sorry, you lost!")
        end_game = False if input("Would you like to continue game? ") == "y" else True
        continue

    while calculate_points(computer_hand) < 17:
        print(f"Computer draw a {draw_card(computer_hand)}")
        print(computer_hand)
        print(player_hand)

    while calculate_points(computer_hand) <= calculate_points(player_hand) and calculate_points(computer_hand) < 20:
        draw_choice = random.randint(1, 4)
        if draw_choice % 4 == 0:
            print(f"Computer draw a {draw_card(computer_hand)}")
            print(computer_hand)
            print(player_hand)
        else:
            break

    print("Final: ")
    print(f"{computer_hand} : {calculate_points(computer_hand)}")
    print(f"{player_hand} : {calculate_points(player_hand)}")

    if calculate_points(computer_hand) > 21:
        print("Congratulations! You won the game")
        end_game = False if input("Would you like to continue game? ") == "y" else True
        continue

    if calculate_points(player_hand) > calculate_points(computer_hand):
        print("Congratulations! You won the game")
        end_game = False if input("Would you like to continue game? ") == "y" else True
        continue
    elif calculate_points(player_hand) == calculate_points(computer_hand):
        print("Draw")
        end_game = False if input("Would you like to continue game? ") == "y" else True
        continue
    else:
        print("Sorry, you lost!")
        end_game = False if input("Would you like to continue game? ") == "y" else True
        continue




