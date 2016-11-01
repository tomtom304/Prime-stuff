primes=[]
primesdif=0
counter=1
a=1
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
        if counter-primes[len(primes)-2]>primesdif:
            primesdif=counter-primes[len(primes)-2]
            print(primesdif)
