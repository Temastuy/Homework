numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
p = 0
y = 0
for y in range(len(numbers)):
    if numbers[y] == 1:
        continue
    is_prime = True
    p=numbers[y]
    if p<2:
        print(p)
        continue
    else:
        q = 2
        t = 0
    while p>= q*q and t!=1:
        if p%q==0:
            t = 1
            is_prime = False
            break
        q = q+1
    if not is_prime:
        not_primes.append(p)
    else:
        primes.append(p)
is_prime = True
print('Primes:', primes, 'Not_primes:', not_primes)
