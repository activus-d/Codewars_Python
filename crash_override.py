"""
Every budding hacker needs an alias! The Phantom Phreak, Acid Burn, Zero Cool and Crash Override are some notable examples from the film Hackers.

Your task is to create a function that, given a proper first and last name, will return the correct alias.

Notes:
Two objects that return a one word name in response to the first letter of the first name and one for the first letter of the surname are already given. See the examples below for further details.

If the first character of either of the names given to the function is not a letter from A - Z, you should return "Your name must start with a letter from A - Z."

Sometimes people might forget to capitalize the first letter of their name so your function should accommodate for these grammatical errors.

Examples
FIRST_NAME = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache', ...}
SURNAME = {'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst' ...}

alias_gen('Larry', 'Brentwood') == 'Logic Bomb'
alias_gen('123abc', 'Petrovic') == 'Your name must start with a letter from A - Z.'
# These two dictionaries are preloaded, you need to use them in your code
FIRST_NAME = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache', ...}
SURNAME = {'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst' ...}

alias_gen('Larry', 'Brentwood') == 'Logic Bomb'
alias_gen('123abc', 'Petrovic') == 'Your name must start with a letter from A - Z.'
"""

def alias_gen(f_name, l_name):
    f_char = f_name[0].upper()
    l_char = l_name[0].upper()

    try:
        return FIRST_NAME[f_char.upper()] + " " + SURNAME[l_char.upper()]
    except KeyError:
        return "Your name must start with a letter from A - Z."

#method two
def alias_gen(f_name, l_name):
    f_char = f_name[0]
    l_char = l_name[0]

    if f_char.isnumeric() or l_char.isnumeric():
        return "Your name must start with a letter from A - Z."
    else:
        return FIRST_NAME[f_char.upper()] + " " + SURNAME[l_char.upper()]