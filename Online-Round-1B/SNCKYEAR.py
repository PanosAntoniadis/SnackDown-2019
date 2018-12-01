# read number of test cases
T = int(input())
for _ in range(T):
    # read year
    N = int(input())
    # check the year and print accordingly
    if (N == 2010 or N == 2015 or N == 2016 or N == 2017 or N == 2019):
        print("HOSTED")
    else:
        print("NOT HOSTED")
