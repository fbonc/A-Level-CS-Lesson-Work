def denarytobinary(number):
    binary = ''

    while number != 0:
        binary_digit = number % 2
        binary += str(binary_digit)
        number = number//2

    return binary[::-1]

def denarytohex(number):
    hex_str = ''
    digits = '0123456789ABCDEF'

    while number != 0:
        hex_digit = number % 16
        hex_str += digits[hex_digit]
        number = number // 16
    
    return hex_str[::-1]

def denarytobase(number, base):
    base_str = ''
    digits = base

    mod = len(base)

    while number != 0:
        base_digit = number % mod
        base_str += digits[base_digit]
        number = number // mod
    return base_str[::-1]

def generate_unicode_chars(start, end):
    characters = []
    for code_point in range(start, end + 1):
        try:
            character = chr(code_point)
            if character.isprintable():
                characters.append(character)
        except ValueError:
            continue
    return characters

def write_unicode_to_txt(filepath):
    with open(filepath, 'w', encoding="utf-8") as file:
        characters = generate_unicode_chars(0x0000, 0xFFFF)
        file.write(''.join(characters))

with open(r'L6 LT1\Dr. Willis\unicode.txt', 'r', encoding="utf-8") as file:
    
    
