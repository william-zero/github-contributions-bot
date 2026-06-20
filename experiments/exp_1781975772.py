"""
Infinite monkey theorem — how long would it take a random keyboard-
mashing monkey to type "to be or not to be"? Let's find out by
simulating it (but cheating with a genetic-style approach so we
don't actually wait until the heat death of the universe).
"""
import random
import string

TARGET = "to be or not to be"
CHARS = string.ascii_lowercase + " "


def random_string(length):
    return "".join(random.choice(CHARS) for _ in range(length))


def fitness(candidate):
    return sum(c == t for c, t in zip(candidate, TARGET))


def mutate(candidate, mutation_rate=0.05):
    return "".join(
        random.choice(CHARS) if random.random() < mutation_rate else c
        for c in candidate
    )


def evolve(population_size=200, max_generations=10_000):
    population = [random_string(len(TARGET)) for _ in range(population_size)]

    for gen in range(max_generations):
        scored = sorted(population, key=fitness, reverse=True)
        best = scored[0]
        best_score = fitness(best)

        if gen % 500 == 0 or best_score == len(TARGET):
            print(f"Gen {gen:5d} | Best: '{best}' | Score: {best_score}/{len(TARGET)}")

        if best == TARGET:
            print(f"\n✓ Found '{TARGET}' after {gen} generations!")
            return gen

        # Keep top 20%, breed the rest from survivors + mutation
        survivors = scored[:population_size // 5]
        population = survivors + [
            mutate(random.choice(survivors)) for _ in range(population_size - len(survivors))
        ]

    print("Ran out of generations — Shakespeare remains safe.")
    return max_generations


if __name__ == "__main__":
    print(f"Target: '{TARGET}' ({len(TARGET)} chars, {len(CHARS)} possible each)\n")
    print("Pure random would need ~27^18 ≈ 10^25 tries. Evolution cheats.\n")
    evolve()
