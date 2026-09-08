# Cellular automaton: Rule 110 — known to be Turing complete
import sys

def rule110(state, width=80, steps=30):
    RULE = {
        (1,1,1): 0, (1,1,0): 1, (1,0,1): 1, (1,0,0): 0,
        (0,1,1): 1, (0,1,0): 1, (0,0,1): 1, (0,0,0): 0,
    }
    for _ in range(steps):
        print(''.join('█' if c else ' ' for c in state))
        next_state = [0] * width
        for i in range(width):
            left = state[(i - 1) % width]
            center = state[i]
            right = state[(i + 1) % width]
            next_state[i] = RULE[(left, center, right)]
        state = next_state

if __name__ == '__main__':
    width = 79
    # Single cell seed in the middle
    state = [0] * width
    state[width // 2] = 1
    rule110(state, width)
