import re

BAD_WORDS = ['poo', 'frack', 'poppycock', 'dunderhead', 'lordy']

# def censor(sentence: str):
#     words = sentence.split()
#     for i in range(len(words)):
#         if words[i] in BAD_WORDS:
#             words[i] = words[i][0] + "*" * (len(words[i]) - 2) + words[i][-1]

#     return " ".join(words)


def censor(sentence: str):
    censored = sentence
    for i in BAD_WORDS:
        censored = re.sub(i, i[0] + "*" * (len(i) - 2) + i[-1], censored, flags=re.IGNORECASE)

    return censored
