import matplotlib.pyplot as plt
def isPrime(num):
    prime = True
    if num>=5:
        maxLim=(num//2)+1
    else:
        maxLim = num
    for i in range(2, maxLim):
        if num%i==0:
            prime = False
            break
    return int(prime)
numbers = 10000
nums, primes = [], []
for i in range(2, numbers+1):
    nums.append(i)
    primes.append(isPrime(i))
plt.plot(nums, primes)
plt.show()