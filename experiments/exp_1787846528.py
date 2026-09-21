"""Caesar cipher — shifting letters around since 100 BC."""

def caesar(text, shift):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

msg = "Hello, world!"
for s in [3, 13, 25]:
    encoded = caesar(msg, s)
    decoded = caesar(encoded, -s)
    print(f"shift={s:>2}: {encoded!r} → {decoded!r}")
