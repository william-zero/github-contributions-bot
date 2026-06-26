"""
Cellular Automaton Rain Simulator
Simulates falling rain and puddle formation in a terminal grid.
"""
import random

WIDTH = 40
HEIGHT = 20
RAIN_CHANCE = 0.04

def make_grid():
    return [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]

def step(grid):
    new_grid = make_grid()
    for y in range(HEIGHT - 1, 0, -1):
        for x in range(WIDTH):
            if grid[y - 1][x] == '|':
                new_grid[y][x] = '|'
            elif grid[y][x] == '|' and y == HEIGHT - 1:
                # Splash on ground
                new_grid[y][x] = '~'
                if x > 0: new_grid[y][x - 1] = '.'
                if x < WIDTH - 1: new_grid[y][x + 1] = '.'
            elif grid[y][x] in ('~', '.'):
                pass  # puddles fade
    # New raindrops at top
    for x in range(WIDTH):
        if random.random() < RAIN_CHANCE:
            new_grid[0][x] = '|'
    return new_grid

def render(grid):
    border = '+' + '-' * WIDTH + '+'
    print(border)
    for row in grid:
        print('|' + ''.join(row) + '|')
    print(border)

if __name__ == '__main__':
    grid = make_grid()
    for frame in range(30):
        grid = step(grid)
    render(grid)
    print("Rain simulation complete. Puddles forming...")
