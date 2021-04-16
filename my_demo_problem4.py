def num_divides(n):
    count = 0
    while n > 1:
        n = n // 2
        count += 1
    return count

n = int(input('Enter an integer: '))

while n > 0:
    count = num_divides(n)
    print('Number of divides for n=', n, ': ', count, sep='')
    n = int(input('Enter an integer: '))

print('Thank you!')

#you can use n in the function and outside the function because of scope.
#in the function it uses the "local" n wheras the outside one uses the "global" n
#if you dont know what that means learn it bc its important