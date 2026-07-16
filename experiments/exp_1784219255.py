# Run-length encoding — compress repeated characters
def rle_encode(s):
    if not s:
        return ""
    result, count = [], 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(f"{count}{s[i-1]}" if count > 1 else s[i-1])
            count = 1
    result.append(f"{count}{s[-1]}" if count > 1 else s[-1])
    return "".join(result)

def rle_decode(s):
    import re
    return re.sub(r'(\d+)(.)', lambda m: m.group(2) * int(m.group(1)), s)

tests = ["AABBBCCDDDDEE", "hello", "WWWWWWWWWWWW", "abcdefg"]
for t in tests:
    enc = rle_encode(t)
    dec = rle_decode(enc)
    print(f"{t!r:30s} -> {enc!r:25s} -> {dec!r} ({'OK' if dec == t else 'FAIL'})")
