"""A minimal Brainfuck interpreter — because why not?"""

def interpret(code, input_data=""):
    tape = [0] * 30000
    ptr = 0
    output = []
    inp = iter(input_data)
    i = 0
    bracket_map = {}

    stack = []
    for pos, ch in enumerate(code):
        if ch == '[':
            stack.append(pos)
        elif ch == ']':
            start = stack.pop()
            bracket_map[start] = pos
            bracket_map[pos] = start

    while i < len(code):
        cmd = code[i]
        if cmd == '>': ptr = (ptr + 1) % 30000
        elif cmd == '<': ptr = (ptr - 1) % 30000
        elif cmd == '+': tape[ptr] = (tape[ptr] + 1) % 256
        elif cmd == '-': tape[ptr] = (tape[ptr] - 1) % 256
        elif cmd == '.': output.append(chr(tape[ptr]))
        elif cmd == ',': tape[ptr] = ord(next(inp, '\x00'))
        elif cmd == '[' and tape[ptr] == 0: i = bracket_map[i]
        elif cmd == ']' and tape[ptr] != 0: i = bracket_map[i]
        i += 1

    return ''.join(output)

# Hello World in Brainfuck
hello = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
print("Hello World program output:", interpret(hello))

# Cat program (echo input back)
cat_program = "+[,.]"
test_input = "bot"
print(f"Cat program with '{test_input}':", interpret(cat_program, test_input))
