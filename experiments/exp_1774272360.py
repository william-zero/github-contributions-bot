#!/usr/bin/env python3
"""
Reverse Polish Notation (RPN) calculator experiment
A whimsical exploration of postfix notation math!
"""

def rpn_calc(expression):
    """Evaluate a reverse polish notation expression."""
    stack = []
    operators = {'+': lambda a, b: a + b,
                 '-': lambda a, b: a - b,
                 '*': lambda a, b: a * b,
                 '/': lambda a, b: a / b if b != 0 else float('inf')}
    
    for token in expression.split():
        if token in operators:
            if len(stack) < 2:
                return "Error: Invalid expression"
            b, a = stack.pop(), stack.pop()
            stack.append(operators[token](a, b))
        else:
            try:
                stack.append(float(token))
            except ValueError:
                return f"Error: Unknown token '{token}'"
    
    return stack[0] if stack else 0

# Test it out!
test_cases = [
    "3 4 +",      # 7
    "10 2 /",     # 5
    "5 3 * 2 +",  # 17
    "7 7 7 + +",  # 21
]

print("🧮 RPN Calculator Experiment 🧮")
for test in test_cases:
    result = rpn_calc(test)
    print(f"  {test:15} = {result}")
