# read number of test cases
T = int(input())
for _ in range(T):
    # read N, K
    line =list(map(int,input().split()))
    N = line[0]
    K = line[1]
    # read list A
    A =list(map(int,input().split()))
    # the condition is true only all numbers are equal to 1, so we just
    # check if we have K or less numbers that are not equal to 1
    count = 0
    for x in A:
        if x != 1:
            count += 1
    if count > K:
        print("NO")
    else:
        print("YES")
