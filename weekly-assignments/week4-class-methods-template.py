import random
from math import sqrt


class Vector:
    """
    A simple class to hold a 3D points
    """

    def __init__(self, _x=0, _y=0, _z=0):
        """
        Constructor a vector with (x,y,z) values. (0,0,0) unless specified.

        :param _x: Initial x value is 0 unless specified
        :param _y: Initial y value is 0 unless specified
        :param _z: Initial z value is 0 unless specified
        """
        self.x = _x
        self.y = _y
        self.z = _z

    def __str__(self):
        """
        Function overload to ensure that vector will print 'cleanly'
        :return: Printable string for vector
        """
        return "<" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ">"

    def dot(self, v):
        """
        Return the dot product of this object and the passed vector v1
        :param v: Another vector in three-space
        :return: Dot product of two vectors
        """
        dot_product = 0

        ### your code here ###
        ### self will be this object, v will be the other vector that is pass to you
        ### calculate the dot product between this/self vector and the passed vector v

        return dot_product

    def distance(self, v):
        """
        Calculate the distance between this point and another
        :param v: Another vector/point in three-space
        :return: Distance between passed point and this one
        """

        dist = 0

        ### your code here ###
        ### self will be this object, v will be the other vector that is pass to you
        ### calculate the distance product between this/self vector and the passed vector v

        return dist


### Main program begins here... ###
if __name__ == "__main__":
    # create two simple vectors
    a = Vector(3, 1, -2)
    b = Vector(9, 2, 4)

    # use class methods to computer the distance (a,b). Should be 8.54
    distance = a.distance(b)
    print("Distance between ", a, " and ", b, " is ", distance)

    # use class methods to compute the product a * b. Should be 21.
    dot_product = a.dot(b)
    print("Dot product between ", a, " and ", b, " is ", dot_product)

    # generate two random vectors and perform the same operations
    # check your results by hand
    (x, y, z) = random.sample(range(100), 3)
    v1 = Vector(x, y, z)

    (x, y, z) = random.sample(range(100), 3)
    v2 = Vector(x, y, z)

    # treat the vectors as point as compute the distance between (check result by hand)
    distance = v1.distance(b)
    print("Distance between ", v1, " and ", v2, " is ", distance)

    # treat vectors as vectors and compute the dot product (check result by hand)
    dot_product = v1.dot(b)
    print("Dot product between ", v1, " and ", v2, " is ", dot_product)

