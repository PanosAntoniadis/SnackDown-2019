import sys
# Read number of test cases
T = int(input())
for _ in range(T):
    # Read N, M, K, L
    line =list(map(int,input().split()))
    N = line[0]
    M = line[1]
    K = line[2]
    L = line[3]
    # Read list A that contains the times that a new
    # person will enter the queue
    A =list(map(int,input().split()))
    # We sort the times in a ascending order
    A.sort()
    # Initilize max_time
    min_time = sys.maxsize
    # We know that the answer will be to enter the queue in the same time
    # with a new person from A or in time K.
    # Check the best time to enter the queue through all A[i] times.
    for i in range(N):
        # Compute waiting time if we enter the queue in A[i]
        time = (M + i)*L -A[i] + L
        if time < min_time:
            min_time = time
    # Check if it is better to enter the queue in K
    if A[N-1] < K:
        time = (M + N)*L - K + L
        if time < min_time:
            min_time = time
    print(min_time)
