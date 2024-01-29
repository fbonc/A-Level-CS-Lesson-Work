def permutations(numbers):

    if len(numbers) == 0:
        return []
    
    elif len(numbers) == 1:
        return [numbers]
    
    permutations_list = []

    for i in range(len(numbers)):
        first = numbers[i]
        remaining = numbers[:i] + numbers[i+1:]
        for j in permutations(remaining):
            permutations_list.append([first] + j)

    return permutations_list

def permutations2(numbers):
    pass

print(permutations([0,1,2]))


        






