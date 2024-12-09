def affine_reverse(strings, a, b):
    shifted_alphabets = []
    for letter in alphabets:
        shifted_alphabets.append(alphabets[(alphabets.index(letter) * a + b) % 26])
    result_string = ""
    for letter in [*strings]:
        if re.match(r"[A-Z]", letter):
            result_string += alphabets[shifted_alphabets.index(letter)]
        else:
            result_string += letter
    return result_string


import re
import math
from collections import Counter
from constants import alphabets
from constants import frequency_sorted

just_alphabet = r"[\s,!\.?\"\']"

common_texts = open("common.txt").readlines()
common_text = []
file = open("test.txt", "r").read()

for i in common_texts:
    common_text.append(i.replace("\n","").upper())


for a in range(1, 26, 2):
    for b in range(1, 26):
        try:
            reverse = affine_reverse(file, a, b)
            splitted = reverse.split(" ")
            happens_0 = math.floor(abs(len(splitted)/ 100 * 2))
            if splitted.count(common_text[0]) > 2:
                print(reverse)
        except:
            pass

# affine_reverse(file, )