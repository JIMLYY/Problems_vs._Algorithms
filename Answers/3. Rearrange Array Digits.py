def quicksort(input_list, start, end):
    if end <= start:
        return
    left = start
    right = end
    while left < right:
        if input_list[left] < input_list[right]:
            left += 1
        else:
            temp_1 = input_list[left]
            temp_2 = input_list[right - 1]
            pivot = input_list[right]
            input_list[right] = temp_1
            input_list[left] = temp_2
            input_list[right - 1] = pivot
            right -= 1
    quicksort(input_list,start, right - 1)
    quicksort(input_list,right + 1, end)
    
def get_num(input_list):
    """
    Get a number from a list of digits
    Args:
        input_list(list): Input List
    Returns:
        result(int): Result(A number)
    """
    result = 0
    for digit in input_list:
        result *= 10
        result += digit
    return result

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    quicksort(input_list, 0, len(input_list)-1)
    print("Sorted input_list is {}".format(input_list))
    num_1_list = [input_list[i] for i in range(len(input_list) - 1, -1, -2)]
    print("List for first number is {}".format(num_1_list))
    num_2_list = [input_list[i] for i in range(len(input_list) - 2, -1, -2)]
    print("List for first number is {}".format(num_2_list))
    return [get_num(num_1_list), get_num(num_2_list)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("The result is 'Pass'")
    else:
        print("The result is 'Fail'")


        
# Test cases       
test_case_2 = [[4,0,0,1], [40, 10]]
test_case_3 = [[8,8,8,6,6,6], [886, 866]]
test_case_4 = [[4, 6, 2, 5, 9, 8], [964, 852]]
# Test case 1
print("Test case 1")
test_function([[1, 2, 3, 4, 5], [542, 31]])
# Test case 2
print("Test case 2")
test_function(test_case_2)
# Test case 3
print("Test case 3")
test_function(test_case_3)
# Test case 4
print("Test case 4")
test_function(test_case_4)
# reference @ Eric Melz github:https://github.com/ericmelz/DSND/blob/master/project3-problems-vs-algorithms/problem_3.py
