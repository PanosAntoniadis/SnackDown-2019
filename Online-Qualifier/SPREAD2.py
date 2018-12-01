# read number of test cases
T = int(input())
for _ in range(T):
    # read number of people
    N = int(input())
    # read list A that tells us that person i can tell up
    # to Ai people pes day
    A = list(map(int,input().split()))
    # initialize total number of days
    days = 0
    # jump gives us the number of remaining people to be told in each day
    jump = A[0]
    # true if we should check the next day, else false
    new_day = True
    idx = 1
    # accumulator that keeps track of the number of
    # people that should be told the next day.
    acc = jump
    while (idx < N):
        # if we are in a new day, we initiliaze jump to the number of
        # people that should be told in this day we increase
        # total number of days and update acc.
        if new_day:
            jump = acc
            days += 1
            jump = jump -1
            acc = acc + A[idx]
            if jump != 0:
                new_day = False
        else:
            # in a certain day we tell in a person and we update
            # acc until jump is zero.
            jump = jump -1
            if jump == 0:
                new_day = True
            acc = acc + A[idx]
        idx += 1
    print(days)
