def costCalculation(cjCost, jcCost, mural):
    mural = mural.replace("?", "")
    cost = 0
    for x in range(0, len(mural)-1):
        if (mural[x]+mural[x+1]) == "CJ":
            cost += cjCost
        elif (mural[x]+mural[x+1]) == "JC":
            cost += jcCost
    return cost


T = int(input())
for x in range(0, T):
    testCase = input().split(" ")
    X = int(testCase[0])
    Y = int(testCase[1])
    mural = testCase[2]
    print("Case #" + str(x+1) + ": "+str(costCalculation(X, Y, mural)))
