def num_divides(n):
    count = 0
    while n > 1:
        n = n // 2
        count += 1
    return count

n = int(input('Enter an integer: '))

while True:
    n = int(input('Enter an integer: '))
    if n <= 0:
        break
    
    count = num_divides(n)
    print('Number of divides for n=', n, ': ', count, sep='')
        

print('Thank you!')