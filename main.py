from alphabet import alphabets
def binary_converter(character):
    return str(bin(alphabets.index(character) + 1))[2:]


def fixed_length_bin(inputs, length):
    remainer_length = length - len(inputs)
    return remainer_length * "0" + inputs


plain_text = "hello"
key = "compu"
result = ""
for index, character in enumerate([*plain_text]):
    bin_text = fixed_length_bin(binary_converter(character), 5)
    bin_key = fixed_length_bin(binary_converter(key[index]), 5)
    # bin_key = str(bin(alphabets.index(key[index]) + 1))[2:]
    result_bin = ""
    for indexs, binary in enumerate([*bin_text]):
        if binary == "0" and binary == bin_key[indexs]:
            result_bin += "0"
        elif binary == "1" and binary == bin_key[indexs]:
            result_bin += "0"
        else:
            result_bin += "1"
    result += alphabets[(int(result_bin, 2) - 1) % 26]
    # print(alphabets[int(result_bin, 2) -1])

print(result)
