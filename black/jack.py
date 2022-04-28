def value_of_card(card):
    if(card == 'A' or card == 'a'):
        return 1
    if(card == 'J' or card == 'Q' or card == 'K'):
        return 10
    if(int(card) <= 10 and int(card) >= 2):
        return int(card)

def higher_card(card_one, card_two):
    if(value_of_card(card_one) > value_of_card(card_two)):
        return card_one

    elif (value_of_card(card_one) == value_of_card(card_two)):
        return card_one, card_two

    else:
        return card_two

def value_of_ace(card_one, card_two):
    if(value_of_card(card_one) == 1 or value_of_card(card_two) == 1):
        return 1
    elif(value_of_card(card_one) + value_of_card(card_two) < 11):
        return 11
    else:
        return 1

def is_blackjack(card_one, card_two):
    if(value_of_card(card_one) == 1 or value_of_card(card_two) == 1):
        if(value_of_card(card_one) + value_of_card(card_two) == 11):
            return True

    return False

def can_split_pairs(card_one, card_two):
    if(value_of_card(card_one) == value_of_card(card_two)):
        return True

    return False

def can_double_down(card_one, card_two):
    sum = value_of_card(card_one) + value_of_card(card_two)

    if(sum <= 11 and sum >= 9):
        return True

    return False