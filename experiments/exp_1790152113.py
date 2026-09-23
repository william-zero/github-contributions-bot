# ROT13 encoder/decoder — Caesar cipher's lazier cousin
import codecs

messages = [
    "Hello, world!",
    "The answer is 42",
    "Never gonna give you up",
    "To be or not to be",
]

print("=== ROT13 Encoder/Decoder ===")
for msg in messages:
    encoded = codecs.encode(msg, 'rot_13')
    decoded = codecs.encode(encoded, 'rot_13')
    print(f"Original : {msg}")
    print(f"Encoded  : {encoded}")
    print(f"Decoded  : {decoded}")
    print()

# rot13 is its own inverse — encoding twice returns the original
secret = "Gur pbqr vf nyernql vafvqr gur znpuvar"
print(f"Mystery message: {codecs.encode(secret, 'rot_13')}")
