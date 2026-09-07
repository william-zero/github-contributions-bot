# Markov chain text generator trained on famous opening lines
import random

transitions = {
    "It": ["was", "is", "seemed", "began"],
    "was": ["the", "a", "dark", "an", "once"],
    "the": ["best", "worst", "dark", "age", "beginning", "end", "sound", "night"],
    "best": ["of", "time,", "day", "thing"],
    "of": ["times,", "the", "wisdom,", "folly,"],
    "times,": ["it", "we", "the"],
    "Call": ["me", "it", "him"],
    "me": ["Ishmael.", "what", "crazy,"],
    "In": ["the", "a", "my", "beginning"],
    "beginning": ["was", "there", "of"],
    "a": ["dark", "bright", "cold", "far", "time"],
    "dark": ["and", "night,", "stormy"],
    "and": ["stormy", "gloomy", "bright", "cold", "a"],
    "stormy": ["night.", "night,", "evening."],
    "night.": ["She", "He", "The", "It"],
    "far": ["away", "future", "land"],
    "away": ["in", "from", "there"],
}

starters = ["It", "Call", "In", "a", "far"]

def generate(length=12):
    word = random.choice(starters)
    sentence = [word]
    for _ in range(length - 1):
        nexts = transitions.get(word, ["the", "a", "and", "of"])
        word = random.choice(nexts)
        sentence.append(word)
    return " ".join(sentence).capitalize()

if __name__ == "__main__":
    print("=== Markov Opening Line Generator ===")
    for _ in range(5):
        print("-", generate(random.randint(8, 14)))
