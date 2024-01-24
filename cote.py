import sys, math

T = int(sys.stdin.readline())

for _ in range(T):
    position = list(map(int, sys.stdin.readline().split()))

    A = position[:2]
    B = position[2:4]
    C = position[4:]

    rad1 = math.sqrt( (A[0] - C[0])**2 + (A[1] - C[1])**2)
    rad2 = math.sqrt( (B[0] - C[0])**2 + (B[1] - C[1])**2)
    bet = math.sqrt( (A[0] - B[0])**2 + (A[1] - B[1])**2)

    large = max(rad1, rad2)
    small = min(rad1, rad2)

    ## 두 원의 중심이 같은 경우
    if bet == 0:
        if rad1 == rad2:
            print(-1)
        else:
            print(0)
        continue

    if (rad1+rad2) < bet:
        print(0)
        continue

    elif (rad1+rad2) == bet:
        print(1)
        continue
    
    else: # rad1 + rad2 > bet 
    