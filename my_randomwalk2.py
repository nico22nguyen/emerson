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

def avg_step_count(start, L):
    # WRITE CODE here to perform 10000 trials where
    # in each trial you start at "start" (the middle)
    # and count as valid only those trials where you hit L.
    # Amongst these valid trials, we seek an estimate of
    # the number of steps (on average).
    valid_trials = 0
    total_steps = 0
    for i in range(10000):
        num_steps = count_num_steps(start, L)
        if num_steps > 0:
            valid_trials+= 1
            total_steps += num_steps
    return total_steps/valid_trials

L = 20
start = 10

avg = avg_step_count(start, L)
print('average # steps to hit L =', avg)

# Should get about 100
