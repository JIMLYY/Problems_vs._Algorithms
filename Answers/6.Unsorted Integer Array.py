def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return (None, None)
    maxVal = ints[0]
    minVal = ints[0]
    for val in ints:
        if val > maxVal:
            maxVal = val
        if val < minVal:
            minVal = val
    return (minVal,maxVal)


# Test case 1
import random
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Test case 2
l2 = []
print ("Pass" if (None, None) == get_min_max(l2) else "Fail")

# Test case 3
l3 = [5,5]
print ("Pass" if (5, 5) == get_min_max(l3) else "Fail")

# Test case 4
l4 = [1, -1, 0]
print ("Pass" if (-1,1) == get_min_max(l4) else "Fail")

# Test case 5
l5 = [i for i in range(0, 1000000)]  # a list containing 0 - 9
random.shuffle(l5)
print ("Pass" if ((0, 999999) == get_min_max(l5)) else "Fail")
