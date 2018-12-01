# a list containing all semiprimes between 1 to 200
semiprimes = [6, 10, 14, 15, 21, 22, 26, 33, 34, 35, 38, 39, 46, 51, 55, 57, 58, 62, 65, 69, 74,
              77, 82, 85, 86, 87, 91, 93, 94, 95, 106, 111, 115, 118, 119, 122, 123, 129, 133, 134,
              141, 142, 143, 145, 146, 155, 158, 159, 161, 166, 177, 178, 183, 185, 187, 194]

# function that checks all the possible sums of two semiprimes from
# the list above
def check(N):
    for i in range(0,len(semiprimes)):
        flag = False
        for j in range(0,len(semiprimes)):
            # if N is equal to the sum of two semiprimes we return true
            if (N == semiprimes[i] + semiprimes[j]):
                flag = True
                return flag
            if (semiprimes[j] >= N):
                break
        if (semiprimes[i] >= N):
            return flag
    return flag

# read number of test cases
T = int(input())
for _ in range(T):
    # read integer N
    N = int(input())
    # check if it is possible to express N as a sum of two semi-primes
    answer = check(N)
    if answer == True:
        print("YES")
    else:
        print("NO")
