# Reverse alphabet picker - fun string manipulation
import random
alphabet = "abcdefghijklmnopqrstuvwxyz"
reversed_alphabet = alphabet[::-1]
print(f"Forward:  {alphabet}")
print(f"Reversed: {reversed_alphabet}")
print(f"Random pick: {random.choice(reversed_alphabet)}")
