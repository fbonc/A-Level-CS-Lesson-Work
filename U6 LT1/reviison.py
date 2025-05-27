def valid_string():
    valid = False
    while not valid:
        valid = True
        string = input("Enter a valid string: ")

        if len(string) < 5 or len(string) > 7: valid = False
        if string != string.upper(): valid = False

        for i in string:
            if string.count(i) > 1:
                valid = False

        ascii_sum = sum([ord(i) for i in string])
        if ascii_sum < 420 or ascii_sum > 600: valid = False
        if valid == False:
            print("Invalid string!")

    print("Valid string!")


def reverse_vowels(user_string):
    string = list(user_string)
    vowels = ["a", "e", "i", "o", "u"]

    front_ptr = 0
    front_ptr_found = False

    back_ptr = len(string) - 1
    back_ptr_found = False

    while front_ptr < back_ptr:
        if string[front_ptr] in vowels:
            front_ptr_found = True
        if string[back_ptr] in vowels:
            back_ptr_found = True
        
        if back_ptr_found and front_ptr_found:
            temp = string[front_ptr]
            string[front_ptr] = string[back_ptr]
            string[back_ptr] = temp
            front_ptr_found = False
            back_ptr_found = False

        if not back_ptr_found:
            back_ptr -= 1
        if not front_ptr_found:
            front_ptr += 1
        

    print("".join(string))


def nth_harshad_number(n):
    harshad_n = 1
    curr = 1
    while harshad_n != n:
        if is_harshad(curr):
            harshad_n += 1
        curr += 1
    curr += 1
    return curr


def is_harshad(number):
    digit_sum = sum([int(i) for i in str(number)])
    if number % digit_sum == 0: return True
    return False

if __name__ == "__main__":
    print(nth_harshad_number(600))