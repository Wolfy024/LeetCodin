def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
    nums1_len = len(nums1) - 1
    nums2_len = len(nums2) - 1
    final = []
    counter1 = counter2 = 0
    while True:
        n1 = nums1[counter1] if counter1 <= nums1_len else None
        n2 = nums2[counter2] if counter2 <= nums2_len else None
        if n1 is None and n2 is None:
            break
        if n1 is None:
            final.append(n2)
            counter2 += 1
        elif n2 is None:
            final.append(n1)
            counter1 += 1
        elif n1 > n2:
            final.append(n2)
            counter2 += 1
        elif n2 > n1:
            final.append(n1)
            counter1 += 1
        elif n2 == n1:
            final.append(n2)
            final.append(n1)
            counter2 += 1
            counter1 += 1
    if len(final) % 2 == 0:
        return (final[len(final) // 2] + final[len(final) // 2 - 1]) / 2
    else:
        return final[len(final) // 2]
