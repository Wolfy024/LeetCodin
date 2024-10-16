def max_sub_array(array):
    max_sum = float('-inf')
    current_sum = 0
    max_array = []
    current_array = []
    for i in array:
        current_sum += i
        current_array.append(i)
        if current_sum > max_sum:
            max_sum = current_sum
            max_array = current_array.copy()
        if current_sum < 0:
            current_sum = 0
            current_array = []
    return max_sum, max_array


print(max_sub_array([1, -4, 5, 6, -7, 8, 9, 10]))
