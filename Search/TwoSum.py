def twosum(array, target):
    hashmap = {}
    for i in range(len(array)):
        complement = target - array[i]
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[array[i]] = i
    return None


result = twosum([-1, -2, 2, 4], 0)
print(result)


# New - 