def reverse_vowels(user_word):
    vowels = 'aeiou'
    user_word = list(user_word)
    final_word = user_word[:]
    vowel_position = []

    for i in range(len(user_word)):
        if user_word[i] in vowels:
            vowel_position.append(i)

    for i in range(len(vowel_position)):
        final_word[vowel_position[i]] = user_word[vowel_position[len(vowel_position) - 1 - i]]
        
    return ''.join(final_word)


if __name__ == "__main__":
    while True:
        user_word = input("Please input a string to reverse vowels: ")
        print(reverse_vowels(user_word))
