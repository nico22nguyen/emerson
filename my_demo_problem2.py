n = int(input('Enter an integer: '))

while n > 0:
    count = 0
    while n > 1:
        n = n // 2
        count += 1

    print('Number of divides for n=', n, ': ', count, sep='')
    n = int(input('Enter an integer: '))

print('Thank you!')
    
##the problem is it always prints n = 1,
#we probably need to save a copy of the original input so we can print
# the right thing at the end