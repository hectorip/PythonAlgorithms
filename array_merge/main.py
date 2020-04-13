def merge(A, current_sum):
    if len(A) > 1:
        rest = merge(A[1:], sum(A))
        performs_merge = 1 if rest > 0 else 0
        return (current_sum + rest) * performs_merge
    return current_sum

def solution(A):
    A.sort()
    A.reverse()
    print(merge(A, 0))

solution([1000, 100, 250])
solution([0, 0, 100])