"""
Brainfuck Interpreter - because why not?
Implements the classic esoteric language in Python.
"""

def brainfuck(code, input_str=""):
    tape = [0] * 30000
    ptr = 0
    code_ptr = 0
    input_ptr = 0
    output = []
    
    brackets = {}
    stack = []
    for i, c in enumerate(code):
        if c == '[':
            stack.append(i)
        elif c == ']':
            j = stack.pop()
            brackets[i] = j
            brackets[j] = i
    
    while code_ptr < len(code):
        cmd = code[code_ptr]
        if cmd == '>':
            ptr = (ptr + 1) % 30000
        elif cmd == '<':
            ptr = (ptr - 1) % 30000
        elif cmd == '+':
            tape[ptr] = (tape[ptr] + 1) % 256
        elif cmd == '-':
            tape[ptr] = (tape[ptr] - 1) % 256
        elif cmd == '.':
            output.append(chr(tape[ptr]))
        elif cmd == ',':
            tape[ptr] = ord(input_str[input_ptr]) if input_ptr < len(input_str) else 0
            input_ptr += 1
        elif cmd == '[' and tape[ptr] == 0:
            code_ptr = brackets[code_ptr]
        elif cmd == ']' and tape[ptr] != 0:
            code_ptr = brackets[code_ptr]
        code_ptr += 1
    
    return ''.join(output)

# Hello World in Brainfuck
hello_world = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
print("Hello World via Brainfuck:", brainfuck(hello_world))

# Count to 5
count_to_5 = "+++++[->++++++++++<]>."*5  # outputs 5 times chr(50)='2' — just a demo
print("Brainfuck interpreter ready!")
