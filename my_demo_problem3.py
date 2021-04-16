n = int(input('Enter an integer: '))

while n > 0:
    count = 0
    original = n
    while n > 1:
        n = n // 2
        count += 1

    print('Number of divides for n=', original, ': ', count, sep='')
    n = int(input('Enter an integer: '))

print('Thank you!')