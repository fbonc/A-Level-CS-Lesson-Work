import skeleton4 as tc

tests = [("(2+3)*5","2 3 + 5 *"),
         ("((2+3)*5)", "2 3 + 5 *"),
         ("((2+3)*5)/5+(3+4)*(1+1)", "2 3 + 5 * 5 / 3 4 + 1 1 + * +"),
         ("1+2", "1 2 +")
         ]

for test in tests:
    infix = test[0]
    rpn_string = ' '.join(tc.ConvertToRPN(test[0]))
    print(f'{infix:>25} => {rpn_string}')
    # print(' '.join(tc.ConvertToRPN(test[0])))
    assert test[1] == rpn_string
    # assert tc.ConvertToRPN(test[0]) == test[1].split(' ')
