# read number of test cases
testcases=int(input())
for i in range(testcases):
    # for each test case read N and K
    teams = list(map(int,input().split()))
    N = teams[0]
    K = teams[1]
    # read score of each team
    scores = list(map(int,input().split()))
    # initialize number of qualified teams
    count = 0
    # sort the list of scores in descending order
    list.sort(scores, reverse = True)
    # count teams after index K that have the same score as the score of the
    # team in index K
    for i in range(K, N):
        if(scores[i]==scores[K-1]):
            count+=1
        else:
            break
    # number of qualified teams is the first K teams plus count
    qualified = K + count
    print(qualified)
