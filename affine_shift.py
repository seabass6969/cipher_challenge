def affine_reverse(strings, a, b):
    shifted_alphabets = []
    for letter in alphabets:
        shifted_alphabets.append(alphabets[(alphabets.index(letter) * a + b) % 26])

    print(alphabets)
    print(shifted_alphabets)
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
file = open("test.txt", "r").read()

cleaned_chars_file = re.sub(just_alphabet, "", file)

chars = Counter([*cleaned_chars_file])

most_common = chars.most_common(2)
print(most_common)
a_coefficient = 0
# b_constant = 0
final_mod = 0

# xa + b = (final) % 26
# xa + b = (final) % 26

disgusted_index_first = alphabets.index(most_common[0][0])
real_index_first = alphabets.index(frequency_sorted[0])

disgusted_index_second = alphabets.index(most_common[1][0])
real_index_second = alphabets.index(frequency_sorted[1])

a_coefficient_1 = real_index_first - real_index_second
a_coefficient_2 = real_index_second - real_index_first
final_mod_1 = disgusted_index_first - disgusted_index_second
final_mod_2 = disgusted_index_second - disgusted_index_first

if a_coefficient_1 > 0:
    a_coefficient = a_coefficient_1
    final_mod = final_mod_1
else:
    a_coefficient = a_coefficient_2
    final_mod = final_mod_2

modded = final_mod % 26
print("{}a = {} mod 26".format(a_coefficient, final_mod))
print("{}a = {} ".format(a_coefficient, modded))

a = (modded * abs(final_mod)) % 26
print("a =", a)

b = modded - a_coefficient
print("b =", b)


print(affine_reverse(file, a, b))
