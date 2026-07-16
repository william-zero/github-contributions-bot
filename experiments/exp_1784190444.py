"""
Markov chain text generator: build a model from seed text and generate new sentences.
"""
import random
import re

SEED_TEXT = """
The quick brown fox jumps over the lazy dog. The dog barked at the fox.
The fox ran away quickly into the forest. The forest was dark and deep.
Deep in the forest lived a wise old owl. The owl watched the fox run past.
Past the trees and through the stream the fox escaped. The stream was cold and clear.
"""

def build_chain(text, order=2):
    words = re.findall(r'\w+', text.lower())
    chain = {}
    for i in range(len(words) - order):
        key = tuple(words[i:i + order])
        next_word = words[i + order]
        chain.setdefault(key, []).append(next_word)
    return chain

def generate(chain, order=2, length=20, seed=42):
    random.seed(seed)
    keys = list(chain.keys())
    current = random.choice(keys)
    result = list(current)
    for _ in range(length - order):
        next_words = chain.get(current)
        if not next_words:
            break
        next_word = random.choice(next_words)
        result.append(next_word)
        current = tuple(result[-order:])
    return ' '.join(result).capitalize() + '.'

if __name__ == "__main__":
    for order in [1, 2, 3]:
        chain = build_chain(SEED_TEXT, order=order)
        print(f"Order-{order}: {generate(chain, order=order, length=25)}")
