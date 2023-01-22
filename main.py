import random

prob = {'A': 0.1, 'C': 0.1, 'G': 0.1, 'T': 0.1}

def weightedDie(Probabilities):
    count = 0
    p = random.uniform(0, 1)
    for keys, values in Probabilities.items():
        count = count + values
        if p < count:
            return keys


print(weightedDie(prob))
