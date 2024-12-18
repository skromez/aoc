import re

input = """
Register A: 63281501
Register B: 0
Register C: 0

Program: 2,4,1,5,7,5,4,5,0,3,1,6,5,5,3,0
"""
a, b, c, *program = map(int, re.findall(r"\d+", input))

pointer = 0
output = []

def combo(operand):
    if 0 <= operand <= 3: return operand
    if operand == 4: return a
    if operand == 5: return b
    if operand == 6: return c
    raise AssertionError(f"unrecognized combo operand {operand}")

while pointer < len(program):
    ins = program[pointer]
    operand = program[pointer + 1]
    if ins == 0: # adv
        a = a >> combo(operand)
    elif ins == 1: # bxl
        b = b ^ operand
    elif ins == 2: # bst
        b = combo(operand) % 8
    elif ins == 3: # jnz
        if a != 0:
            pointer = operand
            continue
    elif ins == 4: # bxc
        b = b ^ c
    elif ins == 5: # out
        output.append(combo(operand) % 8)
    elif ins == 6: # bdv
        b = a >> combo(operand)
    elif ins == 7: # cdv
        c = a >> combo(operand)
    pointer += 2

print(*output, sep=",")