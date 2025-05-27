def evaluateRPN(exp):
    tmp = exp
    while len(tmp) > 1:
        for i, j in enumerate(exp):
            if j in ['*', '+', '-', '/']:
                curr = eval(tmp[i-2] + tmp[i] + tmp[i-1])
                del tmp[i]
                del tmp[i-1]
                tmp[i-2] = str(curr)
    return tmp[0]

print(evaluateRPN(['8', '7', '10', '*', '+']))