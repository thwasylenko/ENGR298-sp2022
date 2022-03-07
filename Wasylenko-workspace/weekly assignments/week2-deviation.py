# bring in randomness cause we need it in our lives
import random


# copy in Dr. Forsyth's random list function for use
def generate_random_int_list(max_length, upper_bound):
    # generate random length between 2 and max_length
    list_length = int(random.uniform(2, max_length))

    # given the length above, sample the Natural Numbers up to upper_bound that many times
    vars = random.sample(range(upper_bound), list_length)

    # return the generated list
    return vars


def main(list_A, list_B):
    """
    Examine list_A and list_B. Determine which has the largest standard deviation and return it as largest_list

    :param list_A: A list of random integers
    :param list_B: A list of random integers
    :return: The list that has the greatest standard deviation
    """

    # iterate through each list and determine which one has the largest value
    # depending on which one you find, set it equal to "largest_list"
    largest_list = []

    ### YOUR CODE HERE ###
    def standard_dev_calc(nums):
        std_dev = 0
        if len(nums) == 0:
            return std_dev
        else:
            sum_1 = 0
            sum_2 = 0
            mean_1 = 0
            mean_2 = 0
            tot = len(nums)
            for digit in nums:
                sum_1 += digit
            mean_1 = sum_1 / tot
            for digit_2 in nums:
                sum_2 += (digit_2 - mean_1) ** 2
            mean_2 = sum_2 / tot
            std_dev = mean_2 ** 2
        return std_dev

    list_1 = standard_dev_calc(list_A)
    list_2 = standard_dev_calc(list_B)

    if list_1 > list_2:
        largest_list = list_A
    else:
        largest_list = list_B

    # do not modify this line
    return largest_list


if __name__ == "__main__":
    # generate two random lists of integers
    max_length = 10
    upper_bound = 100
    A = generate_random_int_list(max_length, upper_bound)

    B = generate_random_int_list(max_length, upper_bound)

    result = main(A, B)

    print("Your code was passed two lists, A:", A, " and B: ", B)

    if result == A:
        print("You reported list A has the largest standard deviation. Use your calculator to check :) ")
    elif result == B:
        print("You reported list B has the largest standard deviation. Use your calculator to check :) ")
    else:
        print("You returned something than either list... Are you updating the largest_list variable? "
              "Did you modify the return line?")
