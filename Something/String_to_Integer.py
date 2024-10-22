def myAtoi(s: str) -> int:
    s = s.strip()
    a = ['-', '+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['+', '-']
    final_num = []
    counter = 0
    converter = 1
    final_number = 0

    for i in s:
        if i in a:
            final_num.append(i)
        else:
            break

    for i in final_num:
        if i in symbols:
            if counter == 0 and i == '-':
                converter = -1
            elif counter == 0 and i == '+':
                converter = 1
            elif counter > 0 and final_number > 0:
                break
            else:
                return 0
        else:
            final_number = final_number * 10 + int(i)
        counter += 1

    max_a = 2 ** 31 - 1
    min_a = -max_a - 1
    a = converter * final_number
    if a > max_a:
        return max_a
    elif a < min_a:
        return min_a
    else:
        return a
