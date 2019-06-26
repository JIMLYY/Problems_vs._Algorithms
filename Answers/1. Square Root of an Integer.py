def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # corner case handling
    if number == 0:
        return 0
    
    # initialization
    left,right = 1, number

    # binary search
    while left <= right:
        mid = (left + right) // 2
        if mid ** 2 <= number and (mid + 1) **2 > number:
            return mid
        elif mid ** 2 > number:
            right = mid - 1
        elif mid ** 2 < number:
            left = mid + 1

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
