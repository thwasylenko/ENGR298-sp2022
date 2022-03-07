import math

### your function definition here
def calculate_pi(error):
    error_upper = math.pi + error
    error_lower = math.pi - error

    ao = 1
    bo = 1 / (math.sqrt(2))
    to = 1 / 4
    po = 1

    counter = 0
    while True:
        an_1 = (ao + bo) / 2
        bn_1 = math.sqrt(ao * bo)
        tn_1 = to - po * ((ao - an_1) ** 2)
        pn_1 = 2 * po

        pi_2 = ((an_1 + bn_1) ** 2) / (4 * tn_1)
        if pi_2 < error_upper and pi_2 > error_lower:
            return pi_2
        ao = an_1
        bo = bn_1
        to = tn_1
        po = pn_1
        counter += 1


# main (body) here to call your function. Do not modify below this line
desired_error = 1E-10

approximation = calculate_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
