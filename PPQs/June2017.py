def RLE(string):
    if not string:
        return ''
    
    last = string[0]
    curr = 1
    encoded_str = ''

    for i in string[1:] + '\0':
        if i == last:
            curr += 1

        else:
            encoded_str += f'{last} {curr} '
            curr = 1
            last = i

    return encoded_str

if __name__ == "__main__":
    while True:
        user_word = input("String to encode: ")
        print(RLE(user_word))
