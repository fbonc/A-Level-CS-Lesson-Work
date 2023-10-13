def to_camel_case(text):
    temp = text.split("_")

    for i in range(len(temp)):
        if i == 0:
            continue
        temp[i] = temp[i].capitalize()

    temp = "".join(temp)
    
    return temp


print(to_camel_case("the_stealth_warrior"))