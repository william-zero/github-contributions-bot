# A small script that generates ASCII bar charts from a list of values

def ascii_bar_chart(data: dict, width: int = 40) -> str:
    max_val = max(data.values()) if data else 1
    lines = []
    for label, value in data.items():
        bar_len = int((value / max_val) * width)
        bar = "#" * bar_len
        lines.append(f"{label:15s} | {bar:<{width}} {value}")
    return "\n".join(lines)


if __name__ == "__main__":
    scores = {
        "Python":    92,
        "JavaScript": 88,
        "Rust":       75,
        "Go":         80,
        "Haskell":    60,
        "COBOL":      15,
    }
    print("Language Popularity Bar Chart")
    print("-" * 60)
    print(ascii_bar_chart(scores))
