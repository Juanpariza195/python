 """Functions used in preparing Guido's gorgeous lasagna.
Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

"""
    constant that returns how many minutes the lasagna should bake in the oven. According to your cookbook, the Lasagna should be in the oven for 40 minutes:
"""
EXPECTED_BAKE_TIME = 40


def bake_time_remaining(minutes):
    """
    function that takes the actual minutes the lasagna     has been in the oven as an argument and returns         how many minutes the lasagna still needs to bake         based on the EXPECTED_BAKE_TIME.
    """
    return EXPECTED_BAKE_TIME - minutes


def preparation_time_in_minutes(capas):
    """
Function that takes the number of layers you want to add to the lasagna as an argument and returns how many minutes you would spend making them. Assume each layer takes 2 minutes to prepare.
"""
    return capas * 2


def elapsed_time_in_minutes(capas, minutes):
    """
    Return elapsed cooking time.
    This function takes two numbers representing the       number of layers & the time already spent
    baking and calculates the total elapsed minutes        spent cooking the lasagna.
    """
    return minutes + preparation_time_in_minutes(capas)