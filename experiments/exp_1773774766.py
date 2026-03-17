#!/usr/bin/env python3
"""
Random permutation maze solver - test various pathfinding strategies
"""

def shuffle_list_fisher_yates(items):
    """Fisher-Yates shuffle for random maze paths"""
    import random
    for i in range(len(items) - 1, 0, -1):
        j = random.randint(0, i)
        items[i], items[j] = items[j], items[i]
    return items

def find_exit(maze_size=10):
    """Simulate pathfinding through permuted maze"""
    import random
    paths = list(range(1, maze_size + 1))
    shuffled = shuffle_list_fisher_yates(paths)
    return shuffled

if __name__ == "__main__":
    result = find_exit(8)
    print(f"Maze solution path: {result}")
    print(f"Steps taken: {len(result)}")
