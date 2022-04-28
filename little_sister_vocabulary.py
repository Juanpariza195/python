import re


def add_prefix_un(word):
    return f"un{word}"

def make_word_groups(array):
    pre = array[0]
    string = pre + " :: "

    for i in range(len(array)):
        if(i > 0):
            if(i == len(array) - 1):
                string += pre + array[i]
            else:
                string += pre + array[i] + " :: "


    return string

def remove_suffix_ness(word):
    word = word[0: -4]
    if(word[-1] == 'i'):
        word = word.replace(word[-1], 'y')
    return word

def adjective_to_verb(sentence, index):
    arreglo = sentence.split(' ')
    word = re.sub(r'[^\w\s]','',arreglo[index])


    return f"{word}en"

print(remove_suffix_ness('artiness'))