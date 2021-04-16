import random

def count_num_steps2(start, L):
    # Return # steps if you hit L but only after hitting 0
    # at least once. If you hit L without hitting 0 at least once
    # then return -1
    num_steps = 0
    hit_0 = False
    while start < L:

        if random.choice(['H','T']) == 'H' or start == 0:
            start += 1
        else:
            start -= 1

        if start == 0:
            hit_0 = True
            
        num_steps += 1
        
    if not hit_0:
        return -1
    else:
        return num_steps

def avg_step_count2(start, L):
    # WRITE CODE here to perform 10000 trials where
    # in each trial you start at "start" (the middle)
    # and count as valid only those trials where you hit L
    # AFTER you hit 0 at least once.
    # Amongst these valid trials, we seek an estimate of
    # the number of steps (on average).
    valid_trials = 0
    total_steps = 0
    for i in range(10000):
        num_steps = count_num_steps2(start, L)
        if num_steps > 0:
            valid_trials+= 1
            total_steps += num_steps
    return total_steps/valid_trials

L = 20
start = 10
avg2 = avg_step_count2(start, L)
print('average # steps to hit L =', avg2)

# Should get approximately 500.