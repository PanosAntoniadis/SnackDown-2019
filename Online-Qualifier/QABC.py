# read number of test cases
T = int(input())
for _ in range(T):
    # read length
    N = int(input())
    # read two lists A and B
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    flag = True
    for i in range(N-2):
        # if A[i] > B[i] then A can't be transformed in A cause our operation
        # only adds numbers to the elements of A
        if (A[i] > B[i]):
            flag = False
            break
        # we apply the operation to A[i] as many times as needed.
        dif = B[i]-A[i]
        A[i] += 1 * dif
        A[i+1] += 2 * dif
        A[i+2] += 3 * dif
    if (A[N-2] == B[N-2]) and (A[N-1] == B[N-1]) and flag:
        print("TAK")
    else:
        print("NIE")
