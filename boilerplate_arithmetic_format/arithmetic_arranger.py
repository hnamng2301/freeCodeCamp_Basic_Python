import re

def arithmetic_arranger(problems, solve = False):
    if len(problems) > 5:
        return "Error: Too many problems."

    #arranged_problems = ""
    first = ""
    second = ""
    lines = ""
    sumx = ""
    strg = ""
    for problem in problems:
        if re.search("[^\s0-9.+-]",problem):
            if re.search("[/]",problem) or re.search("[*]", problem):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."
        firstNumber = problem.split(" ")[0]
        oper = problem.split(" ")[1]
        secondNumber = problem.split(" ")[2]
        res = ""
        if len(firstNumber) >= 5 or len(secondNumber) >= 5:
            return "Error: Numbers cannot be more than four digits."

        if oper == '+':
            res = str(int(firstNumber) + int(secondNumber))
        elif oper == '-':
            res = str(int(firstNumber) - int(secondNumber))

        length = max(len(firstNumber), len(secondNumber)) + 2
        top = str(firstNumber).rjust(length)
        bottom = oper + str(secondNumber).rjust(length-1)
        line = ""

        sum = str(res).rjust(length)

        for s in range(length):
            line += "-"

        if problem != problems[-1]:
            first += top + '    '
            second += bottom + '    '
            lines += line + '    '
            sumx += sum + '    '
        else:
            first += top
            second += bottom
            lines += line
            sumx += sum
    if solve:
        strg = first + "\n" + second + "\n"+ lines + "\n" + sumx
    else:
        strg = first + "\n" + second + "\n" + lines
    return strg
