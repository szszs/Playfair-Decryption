import math


def load_quadgram_frequencies(quadgrams_file_name):
    quadgram_frequencies = {}

    with open(quadgrams_file_name, 'r') as f:
        for line in f.readlines():
            quadgram, frequency = line.split()
            frequency = float(frequency)
            quadgram_frequencies[quadgram] = frequency

    floor = min(quadgram_frequencies.values())

    return quadgram_frequencies, floor


def quadgram_score(quadgram_frequencies, floor, text):
    score = 0

    for i in range(len(text) - 5):
        quadgram = text[i:i+4]
        if quadgram in quadgram_frequencies:
            score += math.log(quadgram_frequencies[quadgram])
        else:
            score += floor
    
    return score
