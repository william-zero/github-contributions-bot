# The Infinite Monkey Theorem - in practice
import random
import string

TARGET = "to be or not to be"

def random_string(length):
    return ''.join(random.choices(string.ascii_lowercase + ' ', k=length))

def monkey_typing():
    attempts = 0
    best = ""
    best_score = 0
    
    while True:
        attempt = random_string(len(TARGET))
        score = sum(a == b for a, b in zip(attempt, TARGET))
        attempts += 1
        
        if score > best_score:
            best_score = score
            best = attempt
            print(f"Attempt #{attempts}: '{best}' ({best_score}/{len(TARGET)} chars correct)")
        
        if attempt == TARGET:
            print(f"Success after {attempts:,} attempts!")
            break
        
        if attempts >= 100_000:
            print(f"Gave up after {attempts:,} attempts. Best: '{best}' ({best_score}/{len(TARGET)})")
            break

if __name__ == "__main__":
    print(f"Target: '{TARGET}'")
    print("Monkeys typing...")
    monkey_typing()
