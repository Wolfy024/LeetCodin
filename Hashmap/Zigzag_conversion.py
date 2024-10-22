def convert(s: str, numRows: int) -> str:
    if numRows < 2:
        return s
    hashmap = [[] for i in range(numRows)]
    counter = perma_counter = 0
    changer = 1
    length = len(s)
    final_parts = []
    while s != "":
        if perma_counter == length:
            break
        hashmap[counter].append(s[perma_counter])
        if counter == numRows - 1:
            changer = -1
        elif counter == 0:
            changer = 1
        counter += changer
        perma_counter += 1
    for parts in hashmap:
        final_parts.append("".join(parts))
    return "".join(final_parts)


# numRows *2 -2
# P      I      N
# A    L S    I G
# Y  A   H  R
# P      I

# P         H
# A      S  I
# Y    I    R
# P  L      I
# A         N
