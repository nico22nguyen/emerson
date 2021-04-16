import random

def count_num_steps(start, L):
    # Return the number-of-steps (number of coin-flips)
    # if you hit L without hitting 0 first. Otherwise if
    # you hit 0 first, return -1
    num_steps = 0
    while start > 0 and start < L:
        if random.choice(['H','T']) == 'H':
            start += 1
        else:
            start -= 1
        num_steps += 1
        
    if start == 0:
        return -1
    else:
        return num_steps

def test_count_num_steps(start, L):
    random.seed(123)
    num_steps = count_num_steps(start, L)
    print('Test #1: num_steps =', num_steps)
    random.seed(1234)
    num_steps = count_num_steps(start, L)
    print('Test #2: num_steps =', num_steps)

L = 20
start = 10

test_count_num_steps(start, L)
# Should print:
# Test #1: num_steps = -1
# Test #2: num_steps = 20