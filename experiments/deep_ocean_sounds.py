# Simulate deep ocean ambient sound frequencies
import math, random

def sine_wave(freq, t, amplitude=1.0):
    return amplitude * math.sin(2 * math.pi * freq * t)

def generate_ambient(duration_s=5, sample_rate=44100):
    # Deep ocean layers: low rumble, whale-range, bubble pops
    frequencies = [18, 42, 110, 220]
    amplitudes  = [0.6, 0.3, 0.08, 0.02]
    samples = []
    for i in range(duration_s * sample_rate):
        t = i / sample_rate
        val = sum(sine_wave(f, t, a) for f, a in zip(frequencies, amplitudes))
        val += random.gauss(0, 0.005)  # deep-sea thermal noise
        samples.append(max(-1.0, min(1.0, val)))
    return samples

if __name__ == "__main__":
    data = generate_ambient(duration_s=3)
    peak = max(abs(s) for s in data)
    print(f"Generated {len(data)} samples | peak amplitude: {peak:.4f}")
    print("Sounds like: slow creaking metal, distant whale song, darkness.")
