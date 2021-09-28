import re


regex = re.compile('[^a-zA-Z]')


with open('sample-english.txt', 'r') as f:
    all_text = regex.sub('', f.read()).upper()


quadgram_frequencies = {}


for i in range(len(all_text) - 5):
    quadgram = all_text[i:i+4]
    if quadgram in quadgram_frequencies:
        quadgram_frequencies[quadgram] += 1
    else:
        quadgram_frequencies[quadgram] = 1


with open('quadgrams.txt', 'w+') as f:
    lines = []

    quadgram_frequencies = list(quadgram_frequencies.items())

    for (quadgram, frequency) in sorted(quadgram_frequencies, key=lambda x: x[1], reverse=True):
        lines.append("{} {}\n".format(quadgram, frequency))

    f.writelines(lines)
