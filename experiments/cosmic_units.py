#!/usr/bin/env python3
"""Convert cosmic distances to fun units."""

def distance_to_fun_units(meters):
    """Convert meters to increasingly absurd cosmic units."""
    units = [
        ("millimeters", 0.001),
        ("shoelaces", 0.3),
        ("dolphin lengths", 2.5),
        ("blue whale lengths", 25),
        ("football fields", 100),
        ("kilometers", 1000),
        ("light-seconds", 299_792_458),
        ("light-years", 9.461e15),
        ("parsecs", 3.086e16),
    ]
    
    print(f"Distance: {meters:,.0f} meters equals:\n")
    for name, size in units:
        count = meters / size
        if count >= 0.1:
            print(f"  {count:,.2f} {name}")

if __name__ == "__main__":
    # How far is the sun?
    distance_to_fun_units(149_597_870_700)  # 1 AU
