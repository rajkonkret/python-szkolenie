def solution(A):
    sum = 0
    for value in A:
        if value%2==0:
            sum = (sum +value)
    return sum
print(solution([-6,-91,1011,-100,84,-22,0,1,473]))
