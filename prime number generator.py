primes=[]
counter=1
while True:
    counter+=1
    checker=0
    for i in range(0,len(primes)):
        if counter % primes[i] == 0:
            checker=1
            break
        if primes[i]**2>counter:
            break
    if checker == 0:
        primes.append(counter)
        print(counter)
