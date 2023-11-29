def sum_of_intervals(intervals):
    intervals_tested = []
    total = 0
    intervals = list(dict.fromkeys(intervals))
    
    for i in intervals:
        intervals_tested.append(i)
        initial_value = i[1] - i[0]
        
        for j in intervals_tested:
            if i[0] < j[1] and i[1] > j[1]:
                initial_value -= j[1] - i[0]

            elif i[0] < j[0] and i[1] > j[0]:
                initial_value -= j[1] - i[1]
            
        total += initial_value
        
        
    return total
        


result = sum_of_intervals([(0, 20), (-100000000, 10), (30, 40)])
print(f"Result: {result}")
assert result == 100000030