#!/usr/bin/env python3
"""
Reverse Engineering DNA to ASCII Art: A Silly Bioinformatics Adventure
"""

DNA_TO_ART = {
    'A': '▲',
    'T': '▼',
    'G': '●',
    'C': '○'
}

def dna_to_art(sequence):
    """Convert DNA bases to abstract art symbols."""
    return ''.join(DNA_TO_ART.get(base.upper(), '?') for base in sequence)

# Sample DNA (first 20 bases of H. sapiens chromosome 1)
sample_dna = "NNNNNNNNNNACACACCCCC"
art = dna_to_art(sample_dna)

print(f"DNA: {sample_dna}")
print(f"Art: {art}")
print("\nThe universe is fundamentally symmetric except when it's not.")
