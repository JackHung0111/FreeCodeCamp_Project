# https://replit.com/@JackHung0111/boilerplate-arithmetic-formatter-1

def arithmetic_arranger(problems, ans=False):
    operands = []
    # check length of the list
    if len(problems) > 5:
        return "Error: Too many problems."
    # check operator
    if False in [("+" in s or "-" in s) for s in problems]:
        return "Error: Operator must be '+' or '-'."
    else:
        operands = [s.split() for s in problems]
    # check digits
    if False in [s[0].isdigit() and s[2].isdigit() for s in operands]:
        return "Error: Numbers must only contain digits."
    # check length of operands
    if False in [len(k) <= 4 for s in operands for k in s]:
        return "Error: Numbers cannot be more than four digits."

    underscore = [max(len(s[0]), len(s[2])) + 2 for s in operands]

    s1 = ""
    # print first line
    for i in range(len(operands)):
        s1 += operands[i][0].rjust(underscore[i])
        if i != len(operands) - 1:
            s1 += "    "
        else:
            s1 += "\n"
    # print second line
    for i in range(len(operands)):
        s1 += operands[i][1]
        s1 += operands[i][2].rjust(underscore[i] - 1)
        if i != len(operands) - 1:
            s1 += "    "
        else:
            s1 += "\n"
    # print underscores
    for i in range(len(operands)):
        for j in range(underscore[i]):
            s1 += '-'
        if i != len(operands) - 1:
            s1 += "    "

    # check second argument
    output = 0
    if ans == True:
        s1 += '\n'
        output = [
            int(s[0]) + int(s[2]) if s[1] == '+' else int(s[0]) - int(s[2])
            for s in operands
        ]
        for i in range(len(output)):
            s1 += str(output[i]).rjust(underscore[i])
            if i != len(operands) - 1:
                s1 += "    "

    return s1
