def reverse(x: int) -> int:
    max_num = 2 ** 31 - 1
    min_num = -max + 1
    if x >= 0:
        num = int(str(x)[::-1])
    else:
        num = -int(str(-x)[::-1])
    if min_num < num < max_num:
        return num
    else:
        return 0
