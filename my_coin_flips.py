import random

def sample_coin_flips():
    for i in range(10):
        if random.choice(['H','T']) == 'H':
            print('Heads')
        else:
            print('Tails')

sample_coin_flips()