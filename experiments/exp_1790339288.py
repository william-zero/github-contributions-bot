"""
Brainfuck interpreter in Python.
Because sometimes you want to make your code harder to read,
not easier.
"""

def brainfuck(code):
    tape = [0] * 30000
    ptr = 0
    ip = 0
    output = []
    brackets = {}

    # Pre-compute bracket matches
    stack = []
    for i, c in enumerate(code):
        if c == '[':
            stack.append(i)
        elif c == ']':
            j = stack.pop()
            brackets[i] = j
            brackets[j] = i

    while ip < len(code):
        cmd = code[ip]
        if cmd == '>': ptr += 1
        elif cmd == '<': ptr -= 1
        elif cmd == '+': tape[ptr] = (tape[ptr] + 1) % 256
        elif cmd == '-': tape[ptr] = (tape[ptr] - 1) % 256
        elif cmd == '.': output.append(chr(tape[ptr]))
        elif cmd == ',': tape[ptr] = ord(input()[0]) if input else 0
        elif cmd == '[' and tape[ptr] == 0: ip = brackets[ip]
        elif cmd == ']' and tape[ptr] != 0: ip = brackets[ip]
        ip += 1

    return ''.join(output)

# Hello World in Brainfuck
hello = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
print(f"Output: {brainfuck(hello)}")
