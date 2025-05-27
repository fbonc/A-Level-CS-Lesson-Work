def map_func(f, orig_list : list) -> list:
    return [f(i) for i in orig_list]
print(map_func(lambda x : x * 2, [1,2,3,4]))