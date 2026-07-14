# temperature_converter.py — converts between Celsius, Fahrenheit, and Kelvin
# with unsolicited opinions about each scale

def celsius_to_fahrenheit(c):
    """Nobody asked but 0°C being 32°F is genuinely cursed."""
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f):
    """Undoing the damage."""
    return (f - 32) * 5 / 9

def celsius_to_kelvin(c):
    """Absolute zero: where all vibes cease."""
    return c + 273.15

def kelvin_to_celsius(k):
    """Coming back from the void."""
    return k - 273.15

def fahrenheit_to_kelvin(f):
    """The cursed path: F -> C -> K. Two wrongs, one right."""
    return celsius_to_kelvin(fahrenheit_to_celsius(f))

def temperature_opinion(c):
    if c < 0:
        return "❄️ Unacceptable. Stay inside."
    elif c < 10:
        return "🧥 Technically survivable."
    elif c < 20:
        return "😐 Tolerable with layers."
    elif c < 28:
        return "☀️ Peak human operating range."
    elif c < 35:
        return "😓 Getting existential."
    else:
        return "🔥 The sun has won."

if __name__ == "__main__":
    temps = [0, 20, 37, 100, -40, 273.15]
    print(f"{'°C':>8} {'°F':>8} {'K':>8}  {'Vibe'}")
    print("-" * 55)
    for c in temps:
        print(f"{c:>8.2f} {celsius_to_fahrenheit(c):>8.2f} {celsius_to_kelvin(c):>8.2f}  {temperature_opinion(c)}")
