#!/usr/bin/env python3

def character_frequency(filename):
    # try to open the file

    try:
        f = open(filename)
    except OSError:
        return None
    
    # process the file

    characters = {}
    for line in f:
        for char in line:
            characters[char] = characters.get(char, 0) + 1
    f.close()
    print(characters)
    return characters

