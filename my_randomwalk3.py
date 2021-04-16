import random

#this funnction is fucked up i cant figure out why tho
#its short by 20 or so every time for some reason
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
    
def test_count_num_steps2(start, L):
    random.seed(123)
    num_steps = count_num_steps2(start, L)
    print('Test #1: num_steps =', num_steps)
    random.seed(1234)
    num_steps = count_num_steps2(start, L)
    print('Test #2: num_steps =', num_steps)

L = 20
start = 10
test_count_num_steps2(start, L)

# Should print
# Test #1: num_steps = 384
# Test #2: num_steps = -1