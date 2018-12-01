# Read number of test cases
T = int(input())
for _ in range(T):
    # Read number of heaps
    line = list(map(int,input().split()))
    N = line[0]
    M = line[1]
    # Read number of stones in each heap
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    # Remove heaps with zero stones cause they are useless
    while(0 in A):
        A.remove(0)
    while(0 in B):
        B.remove(0)
    # Sort each list in ascending order
    A.sort()
    B.sort()
    # Bob wins only if the two players have exactly the same number of
    # stones in each heap.
    if len(A) == len(B):
        flag = True
        for i in range(len(A)):
            if A[i] != B[i]:
                print("Alice")
                flag = False
                break
        if flag:
            print("Bob")
    else:
        print("Alice")
