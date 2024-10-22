import itertools


def letterCombinations(digits: str) -> list[str]:
    listt = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i'],
        ['j', 'k', 'l'],
        ['m', 'n', 'o'],
        ['p', 'q', 'r', 's'],
        ['t', 'u', 'v'],
        ['w', 'x', 'y', 'z'],
    ]
# No, I did not have the patience to type this listt. Chatgpt did. Below is me though.
    final = [""]
    if digits == "":
        return []
    else:
        for i in digits:
            final = [''.join(combo) for combo in itertools.product(final, listt[int(i) - 2])]
            print(final)
            print(listt[int(i) - 2])
    return final


