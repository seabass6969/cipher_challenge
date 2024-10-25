import re
from collections import Counter
file = open("test.txt").read()

just_alphabet = r"[\s,!\.?\"\']"

cleaned_chars_file = re.sub(just_alphabet, "", file)
print(Counter(cleaned_chars_file))