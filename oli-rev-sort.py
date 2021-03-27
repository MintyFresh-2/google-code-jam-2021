def reversort(num, numlist):
    
    switchcost = 0
    numlist = [int(i) for i in numlist]
    
    for i in range (0, num-1):
        j = numlist.index(min(numlist[i:]))
        begstring = numlist[0:i]
        endstring = numlist[j+1:]

        if i > 0:
            midstring = numlist[j:i-1:-1]
        else:
            midstring = numlist[j::-1]
        
        switchcost += j-i+1

        numlist = begstring+midstring+endstring

    return switchcost

reversort(4,"4213")

numbertest = int(input ())
for case in range (0, numbertest):
    num = input()
    testcase = input().split(" ")
    swicost = reversort(int(num),testcase)
    print("Case #"+str(case+1)+": "+str(swicost))