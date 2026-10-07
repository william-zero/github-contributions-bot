"""
Brainf*** interpreter - because sometimes the esoteric is the exotic.
"""

def brainfuck(code, input_data=""):
    cells = [0] * 30000
    ptr = 0
    ip = 0
    input_pos = 0
    output = []
    bracket_map = {}

    # Build bracket map
    stack = []
    for i, c in enumerate(code):
        if c == '[':
            stack.append(i)
        elif c == ']':
            j = stack.pop()
            bracket_map[j] = i
            bracket_map[i] = j

    while ip < len(code):
        c = code[ip]
        if c == '>': ptr = (ptr + 1) % 30000
        elif c == '<': ptr = (ptr - 1) % 30000
        elif c == '+': cells[ptr] = (cells[ptr] + 1) % 256
        elif c == '-': cells[ptr] = (cells[ptr] - 1) % 256
        elif c == '.': output.append(chr(cells[ptr]))
        elif c == ',':
            if input_pos < len(input_data):
                cells[ptr] = ord(input_data[input_pos])
                input_pos += 1
        elif c == '[' and cells[ptr] == 0: ip = bracket_map[ip]
        elif c == ']' and cells[ptr] != 0: ip = bracket_map[ip]
        ip += 1

    return ''.join(output)

# Hello World in Brainfuck
hello = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
print("Brainfuck says:", brainfuck(hello))
