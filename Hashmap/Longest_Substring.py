from collections import deque


def func(s):
    q = deque()
    ret = 0
    for i in s:
        if i in q:
            while q.popleft() != i:
                pass
        q.append(i)
        ret = max(ret, len(q))
    return ret


# New Concept -> deque() - Useful.