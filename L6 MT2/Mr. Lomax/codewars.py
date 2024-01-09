def custom_christmas_tree(chars, n):
    tree = ""

    char_index = 0
    for i in range(0,(n+1)):
        tree += f"\n{' ' * (n-i)}"

        for _ in range(i):
            tree += chars[char_index] + " "
            char_index = (char_index + 1) % len(chars)

    trunkheight = n//3
    for i in range(1, trunkheight+1):
        tree += f"\n{(n - 1)*' '}|"
    
    
    return tree

print(custom_christmas_tree("*x", 6))