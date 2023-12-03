'''
Text from https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

Sift the Twos's and Sift the Three's:
   The Sieve of Eratosthenes.
   When the multiples sublime,
   The numbers that remain are Prime.

                                    Anonymous

To find all the prime numbers less than or equal to a given integer n by Eratosthenes' method:
1. Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
2. Initially, let p equal 2, the smallest prime number.
3. Enumerate the multiples of p by counting in increments of p from 2p to n, and mark them in the list (these will be 2p, 3p, 4p, ...; the p itself should not be marked).
4. Find the smallest number in the list greater than p that is not marked. If there was no such number, stop. Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.
5. When the algorithm terminates, the numbers remaining not marked in the list are all the primes below n.

As a refinement, it is sufficient to mark the numbers in step 3 starting from p^2, as all the smaller multiples of p will have already been marked at that point.
This means that the algorithm is allowed to terminate in step 4 when p^2 is greater than n.

Pseudocode

algorithm Sieve of Eratosthenes is
    input: an integer n>1.
    output: all prime numbers from 2 through n.

    let A be an array of Boolean values, indexed by integers 2 to n,
    initially all set to true.

    for i = 2, 3, 4, ..., not exceeding sqrt(n) do
        if A[i] is true
            for j = i^2, i^2 + i, i^2 + 2i, i^2 + 3i, ..., not exceeding n do
                set A[j] := false
        
    return all i such that A[i] is true.
'''

n = int(input('Choose the integer n that defines the range of prime numbers from 2 to n: '))

A = []
for a in range(0,n+1):
    A.append(True)

stop = int(n**0.5) + 1
for i in range(2,stop):
    if A[i] == True:
        for j in range(i**2,n,i):
            A[j] = False

primes = []

for k in range(2,n):
    if A[k] == True:
        primes.append(k)

print('Prime numbers smaller than {} are: \n{}'.format(n,primes))

f = open('primes.txt', 'w')
f.write('Prime numbers smaller than {} are: \n{}'.format(n,primes))
f.close()

# Printing the prime numbers according to https://jaketae.github.io/study/prime-spirals/

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')

def get_coordinate(num):
    return num * np.cos(num), num * np.sin(num)

def create_plot(nums, figsize=8, s=None, show_annot=False):
    nums = np.array(list(nums))
    x, y = get_coordinate(nums)
    plt.figure(figsize=(figsize, figsize))
    plt.axis("off")
    plt.scatter(x, y, s=s)
    plt.show()

create_plot(primes,6,0.15,False)