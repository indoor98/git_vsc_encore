import sys, math

T = int(sys.stdin.readline())

for _ in range(T):
    position = list(map(int, sys.stdin.readline().split()))

    A = position[:2]
    B = position[2:4]
    C = position[4:]

    rad1 = math.sqrt( (A[0] - C[0])**2 + (A[1] - C[1])**2)
    rad2 = math.sqrt( (B[0] - C[0])**2 + (B[1] - C[1])**2)
    between = math.sqrt( (A[0] - B[0])**2 + (A[1] - B[1])**2)


    print(rad1, rad2, between)

    if (rad1 + rad2) < between :
        print(0)
    
    elif (rad1 + rad2) == between :
        print(1)
    
    elif (rad1 + rad2) > between :
        if (min(rad1, rad2) + between) < max(rad1, rad2) :
            print(-1)
        elif (min(rad1, rad2) + between) == max(rad1, rad2) :
            print(1)
        else: print(2)
