import numpy as np

def get_rounds(round_number):
    return [round_number, round_number+1, round_number+2]

#print(get_rounds(27))

def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2

#print(concatenate_rounds([27, 28, 29], [35, 36]))

def list_contains_round(rounds, round_number):
    return round_number in rounds

#print(list_contains_round([27, 28, 29, 35, 36], 29))

# def card_average(hand):
#     hand = np.array(hand)
#     return hand.mean()

def card_average(hand):
    sum = 0
    for i in hand:
        sum += i
    return sum / len(hand)

#print(card_average([5, 6, 7]))

def approx_average_is_average(hand):
    promedio = (hand[0] + hand[-1]) / 2
    mediana = hand[int(len(hand) / 2)]

    return (promedio == card_average(hand) or mediana == card_average(hand))

print(approx_average_is_average([0, 1, 5]))

def average_even_is_average_odd(hand):
    acumuladorPares = 0
    conteoPares = 0
    promedioPares = 0

    acumuladorImpares = 0
    conteoImpares = 0
    promedioImpares = 0

    for i in hand:
        if(i % 2 == 0):
            acumuladorPares += i
            conteoPares += 1
        else:
            acumuladorImpares += i
            conteoImpares += 1

    promedioPares = acumuladorPares / conteoPares
    promedioImpares = acumuladorImpares / conteoImpares

    return promedioPares == promedioImpares

#print(average_even_is_average_odd([1, 2, 3]))


def maybe_double_last(hand):
    if(hand[-1] == 11):
        hand.append(hand[-1] * 2)
        hand.pop(-2)

    return hand

#print(maybe_double_last([5, 9, 11]))