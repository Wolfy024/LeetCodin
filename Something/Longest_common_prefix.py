def longestCommonPrefix(strs: list[str]) -> str:
    final = ""
    temp = strs[0]
    for i in strs:
        for j in range(len(temp)):
            if j > (len(i) - 1) or temp[j] != i[j]:
                temp = temp[:j]
                break
            else:
                continue
    final = temp
    return final
