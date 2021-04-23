ex = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def get_subset(s, l, c=[]):
    results = []
    if len(c) >= l:
        return [c]
    for i, e in enumerate(s):
        new = c + [e]
        results += get_subset(s[i+1:], l, new)
    return results

total = 0
for i in range(1, len(ex) + 1):
    sub = get_subset(ex, i)
    total += len(sub)
    print(get_subset(ex, i))
print(total)