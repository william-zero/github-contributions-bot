# Cellular automaton: Rule 110
# Rule 110 is known to be Turing complete

def rule110(state):
    """Apply Rule 110 to a state string of 0s and 1s."""
    new_state = []
    n = len(state)
    for i in range(n):
        left = int(state[(i - 1) % n])
        center = int(state[i])
        right = int(state[(i + 1) % n])
        pattern = (left << 2) | (center << 1) | right
        # Rule 110 binary: 01101110
        rule = 0b01101110
        new_state.append(str((rule >> pattern) & 1))
    return ''.join(new_state)

def visualize(state):
    return ''.join('█' if c == '1' else ' ' for c in state)

width = 60
state = '0' * (width // 2) + '1' + '0' * (width - width // 2 - 1)

print("Rule 110 Cellular Automaton")
print("-" * width)
for _ in range(30):
    print(visualize(state))
    state = rule110(state)
