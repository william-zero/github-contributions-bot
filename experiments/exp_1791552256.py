"""
Markov Chain Text Generator - a tiny text predictor
that learns from its own training data.
"""
import random
from collections import defaultdict


def build_chain(text, order=2):
    chain = defaultdict(list)
    words = text.split()
    for i in range(len(words) - order):
        key = tuple(words[i:i + order])
        chain[key].append(words[i + order])
    return chain


def generate(chain, order=2, length=30, seed=None):
    if seed:
        key = tuple(seed.split()[:order])
    else:
        key = random.choice(list(chain.keys()))
    output = list(key)
    for _ in range(length):
        next_words = chain.get(key)
        if not next_words:
            break
        next_word = random.choice(next_words)
        output.append(next_word)
        key = tuple(output[-order:])
    return " ".join(output)


CORPUS = (
    "the quick brown fox jumps over the lazy dog "
    "the fox ran quickly over the hill and the dog "
    "chased the fox over the river but the fox was too quick "
    "the lazy dog slept under the old oak tree while the fox "
    "danced in the moonlight over the misty river"
)

chain = build_chain(CORPUS)
print("Generated text:")
print(generate(chain, length=25))
