import math


def main():
    """
    Use the Gauss-Legendre Algorithm to estimate Pi. Perform 10 approximation loops. Once complete, return the approximation.
    :return:
    """


    ### Your code here ###
    import math
    ao = 1
    bo = 1 / (math.sqrt(2))
    to = 1 / 4
    po = 1
    counter = 0
    pi_1 = 0
    while counter < 10:
        an_1 = (ao + bo) / 2
        bn_1 = math.sqrt(ao * bo)
        tn_1 = to - po * ((ao - an_1) ** 2)
        pn_1 = 2 * po
        pi_2 = ((an_1 + bn_1) ** 2) / (4 * tn_1)
        ao = an_1
        bo = bn_1
        to = tn_1
        po = pn_1
        pi_1 = pi_2
        counter += 1

    # set pi_estimate to whatever variable you were using for pi
    pi_estimate = pi_1

    # return the estimated value of pi
    return pi_estimate


if __name__ == "__main__":

    # call the student function
    result = main()

    # print results
    error = abs(math.pi - result)

    # print out the results
    print("You returned the value: ", result)
    print("This has error of: ", error)
    if error < 1E-9:
        print("This is acceptable...")
    else:
        print("The error is too much. Are you looping 10 times?")
