# Function that computes [a*(a+1)* ... *b] mod 10**9+7
def fastMul(a, b):
    n = b-a + 1
    p = 1
    for i in range(a,b+1):
        p = p%(10**9+7) * i
    return p
# Funtion that computes the result
def maxProd(n, k):
    prod = 1
    # The elements that will maximize the specific product should be as close
    # to n//k as possible. So we can compute rightmost and leftmost element.
    # All the remaining elements will be between these two.
    right = n//k + k//2
    left = n//k - k//2
    # TODO: add more comments 
    if n%k == 0:
        if k%2 == 1:
            prod *= fastMul(left-1,right-1 ) * fastMul(left, right)
        else:
            prod *= fastMul(left, n//k -1) * fastMul(left-1, n//k-2)
            prod *= fastMul(n//k+1, right) * fastMul(n//k, right-1)
    else:
        if k%2 == 1:
            prod *= fastMul(right - n%k +1, right) * fastMul(right-n%k +2, right+1)
            prod *= fastMul(left, right-n%k) * fastMul(left-1, right -n%k -1)
        else:
            if n%k < k//2:
                prod *= fastMul(n//k+1, right) * fastMul(n//k, right-1)
                prod *= fastMul(left, n//k-1-n%k) * fastMul(left-1, n//k-2-n%k)
                prod *= fastMul(n//k-n%k+1, n//k ) * fastMul(n//k - n%k , n//k-1)
            else:
                prod *= fastMul(left+1, n//k) * fastMul(left, n//k-1)
                prod *= fastMul(n//k+1, right-n%k+k//2) * fastMul(n//k, right-n%k-1+k//2)
                prod *= fastMul(right - n%k+k//2 +2, right+1) * fastMul(right -n%k +k//2+1, right)
    return prod

# Read number of test cases
T = int(input())
for _ in range(T):
    # Read N, K
    line =list(map(int,input().split()))
    N = line[0]
    K = line[1]
    # If sum from 1 to K is less than N we print -1 cause N can't be expressed
    # as the sum of K distinct positive integers.
    if N < K*(K+1)/2:
        print(-1)
    else:
        max_A = maxProd(N,K)
        print(max_A%(10**9+7))
