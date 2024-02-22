import math

def decimal_to_binary(original_fraction):
    binary = ''
    original_decimal = math.modf(original_fraction)[0]
    curr = original_decimal * 2

    seen = []

    while curr != original_fraction and curr != 0:

        integer = int(math.modf(curr)[1])
        decimal = math.modf(curr)[0]

        binary += str(integer)

        if curr in seen:
            break

        seen.append(curr)

        curr = decimal * 2
        

    return binary

print(decimal_to_binary(0.8))