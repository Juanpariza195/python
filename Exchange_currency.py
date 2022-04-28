import math

def exchange_money(budget, exchange_rate):
    return budget / exchange_rate

def get_change(budget, exchanging_value):
    return  budget - exchanging_value

def get_value_of_bills(denomination, number_of_bills):
    return denomination * number_of_bills

def get_number_of_bills(budget, denomination):
    return math.floor(budget / denomination)

def exchangeable_value(budget, exchange_rate, spread, denomination):
    spread = spread / 100
    newExchange_rate = exchange_rate + (exchange_rate * spread)

    newBudget = budget / newExchange_rate

    division = math.floor(newBudget / denomination)
    return division * denomination

def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    exchangeableValue = exchangeable_value(budget, exchange_rate, spread, denomination)

    spread = spread / 100
    newExchange_rate = exchange_rate + (exchange_rate * spread)

    newBudget = budget / newExchange_rate

    return math.floor(newBudget - exchangeableValue)