import quadgram_scorer
import random

ciphertext = "PAXRAKZLPNYLARRYKZYKUTAMFHLYKGPYKULFHYENGPACUPGGAPNMLNHRZAGYZFMNLFOOACMNXAKZNMYKUXPOYZAKGICGTOFMTMACKZOACMXFYLGEATTFGPNZCEPNLLLFYZFRGNMFIFCLNGPNMNFLAKYLEATTFGPFGYTZACVGRCHFVACGGPNGNTINMAROACMRHFTYKUAZAGLPFHHYGMOGPNNSINMYTNKGPNTYUPGVYGNEATTFFHYENEFCGYACLHOMNIHYNZEATTFKAGRNNHYKUFGFHHFKSYACLGAPFQNGPNNSINMYTNKGGMYNZZAGQNMOGMCNEATTFLFYZGPNZCEPNLLRHFTYKUANLFKZTCLGFMZVAGPVYGNZAGFKZGPNTAMFHARGPFGYLVYMZLARFRNFGPNMRHAEWGAUNGPNM"

quadgram_frequencies, score_floor = quadgram_scorer.load_quadgram_frequencies("quadgrams.txt")

alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
top_key = None
top_score = None

parent_key = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def substitution_decrypt(ciphertext, key):
    plaintext = ""
    for c in ciphertext:
        plaintext += key[alphabet.index(c)]
    return plaintext

def swap_two_random_elements(list_):
    swap_a, swap_b = random.sample(range(len(list_)), 2)
    list_[swap_a], list_[swap_b] = list_[swap_b], list_[swap_a]

while True:
    random.shuffle(parent_key)

    parent_plaintext = substitution_decrypt(ciphertext, parent_key)
    parent_score = quadgram_scorer.quadgram_score(quadgram_frequencies, score_floor, parent_plaintext)

    iterations_without_improvement = 0
    while iterations_without_improvement < 1000:
        child_key = parent_key[:]
        swap_two_random_elements(child_key)

        child_plaintext = substitution_decrypt(ciphertext, child_key)
        child_score = quadgram_scorer.quadgram_score(quadgram_frequencies, score_floor, child_plaintext)

        if child_score > parent_score:
            parent_score = child_score
            parent_key = child_key
            iterations_without_improvement = 0
        else:
            iterations_without_improvement += 1

    if top_score is None or parent_score > top_score:
        top_score = parent_score
        top_key = parent_key[:]

        print("Top score:", top_score)
        print("Top key:", top_key)
        print("Top message:", substitution_decrypt(ciphertext, top_key))
