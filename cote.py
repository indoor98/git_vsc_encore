import sys, math

T = int(sys.stdin.readline())

for _ in range(T):
    position = list(map(int, sys.stdin.readline().split()))

    A = position[:2]
    B = position[2:4]
    C = position[4:]

    radius1 = math.sqrt( (A[0] - C[0])**2 + (A[1] - C[1])**2)
    radius2 = 
    print(radius1)