def romanToInt(s: str) -> int:
    sum = 0
    key1 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    key2 = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    for i in key2:
        if i in s:
            s = s.replace(i, "")
            sum += key2[i]
        else:
            continue
    for i in s:
        sum += key1[i]
    return sum

