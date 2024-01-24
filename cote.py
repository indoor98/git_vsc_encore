import sys, math

T = int(sys.stdin.readline())

for _ in range(T):
    position = list(map(int, sys.stdin.readline().split()))

    A = position[:2]
    B = position[3:5]
    r1 = position[2]
    r2 = position[5]
    r3 = math.sqrt( (A[0] - B[0])**2 + (A[1] - B[1])**2)

    ## 두 원의 중심이 같은 경우
    if r3 == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
        continue

    ## 두 원의 중심이 다른 경우

    # 포함 관계가 아닌 경우
    if r3 > max(r1, r2):
        if (r1 + r2) < r3:
            print(0)
        elif (r1 + r2) == r3:
            print(1)
        else :
            print(2)
    elif r3 < max(r1, r2): # 한 원이 다른 원에 포함되는 경우
        if max(r1, r2) > (r3 + min(r1, r2)) :
            print(0)
        elif max(r1, r2) == (r3+min(r1, r2)) :
            print(1)
        else:
            print(2)
    else:
        print(2)
        