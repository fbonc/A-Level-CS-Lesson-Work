def freq_of_mode(num_list):
    freqs = {}

    for i in num_list:
        if i not in freqs:
            freqs[i] = 1
        else:
            freqs[i] += 1

    max_freq = max(freqs.values())
    multimodal = sum(1 for freq in freqs.values() if freq == max_freq)

    if multimodal > 1:
        return "Data was multimodal"
    else:
        return max_freq


if __name__ == "__main__":
    while True:
        digit_num = int(input("How many numbers would you like to input? "))
        num_list = []
        for i in range(digit_num):
            num_list.append(int(input(f"Enter number #{i + 1}: ")))

        print(freq_of_mode(num_list))
        