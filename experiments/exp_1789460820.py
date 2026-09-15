"""Run-Length Encoding - compressing the compressible since 1967"""

def encode_rle(text):
    if not text:
        return ""
    result = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count += 1
        else:
            result.append(f"{count}{text[i-1]}" if count > 1 else text[i-1])
            count = 1
    result.append(f"{count}{text[-1]}" if count > 1 else text[-1])
    return ''.join(result)

def decode_rle(encoded):
    result = []
    i = 0
    while i < len(encoded):
        if encoded[i].isdigit():
            count = int(encoded[i])
            result.append(encoded[i+1] * count)
            i += 2
        else:
            result.append(encoded[i])
            i += 1
    return ''.join(result)

if __name__ == '__main__':
    tests = ["AAABBBCCDDDDEEEE", "ABCDEF", "AAAAAAAAAAAAAAA"]
    for t in tests:
        enc = encode_rle(t)
        dec = decode_rle(enc)
        ratio = len(enc) / len(t) * 100
        print(f"'{t}' -> '{enc}' -> '{dec}' ({ratio:.0f}% of original)")
