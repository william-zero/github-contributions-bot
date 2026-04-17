# Run-length encoding: compress consecutive repeated characters
def run_length_encode(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(f"{count}{s[i-1]}" if count > 1 else s[i-1])
            count = 1
    result.append(f"{count}{s[-1]}" if count > 1 else s[-1])
    return "".join(result)

def run_length_decode(s):
    result = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            num = ""
            while i < len(s) and s[i].isdigit():
                num += s[i]
                i += 1
            result.append(s[i] * int(num))
        else:
            result.append(s[i])
        i += 1
    return "".join(result)

samples = ["AAABBBCCDDDDEA", "hello", "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"]
for s in samples:
    enc = run_length_encode(s)
    dec = run_length_decode(enc)
    print(f"Original : {s}")
    print(f"Encoded  : {enc}")
    print(f"Decoded  : {dec}")
    print(f"Match    : {s == dec}\n")
