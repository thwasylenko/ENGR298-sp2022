from primality import primality
from utils import generate_random_int_list

# generate a long random list of integers
randoms = generate_random_int_list(1000, 10000000)

# iterate through the list check for all prime numbers
# if you see the magic number '100', gremlins are present and
# exit the loop. Keep track of how many we found
primes_found = 0
for p in randoms:

    # anything less than 2 is not prime
    if p < 2:
        continue

    # check to specific, dangerous numbers
    if p == 100:
        print("Danger!!")
        break

    # check to see if p is prime or not
    primality_test = primality.isprime(p)

    if primality_test == True:
        print("The value "+str(p)+ " is prime!")
        primes_found = primes_found + 1

# loop is now done. Print out the results....
print("The list contained " + str(len(randoms)) + " elements. We found " + str(primes_found) + " primes!")

