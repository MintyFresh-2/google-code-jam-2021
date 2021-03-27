def reversort(L):
    cost = 0
    for i in range(0, len(L)-1):
        minimum = min(L[i:])
        j = L.index(minimum)
        if i == 0:
            L = L[:i] + L[j::-1] + L[j+1:]
        else:
            L = L[:i] + L[j:i-1:-1] + L[j+1:]
        cost += j-i+1
    return cost


T = int(input())
for x in range(0, T):
    N = int(input())
    inputList = input().split(" ")
    inputList = [int(i) for i in inputList]
    print("Case #"+str(x+1)+": "+str(reversort(inputList)))
