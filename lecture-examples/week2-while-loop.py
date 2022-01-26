# an initial deposit
balance = 1000

# interest rate (as a fraction)
rate = 0.023

# year to run calculation
n = 10

# a counter variable to keep track of the loop
counter = 0

while counter < n:
    balance = balance * (1 + rate)
    counter = counter + 1

    print("At the end of Year " + str(counter)
          + " the balance is " + str(balance))


