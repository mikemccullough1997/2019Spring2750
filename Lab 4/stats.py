def mean(myList):
    mean = sum(myList) / len(myList)
    return mean

def median(myList):
    myList2 - myList[:]
    myLIst2.sort()
    if len(myLIst2)%2 == 0:
        rightmid = len(myList2)//2
        leftmid = rightmid - 1
        median = (myList2[leftmid] + myList2[rightmid])/2
    else:
        mid = len(myList2)//2
        median = myList2 [mid]
    return median

def mode(myList):
     countdict = {}
     for item in myList:
             if item in countdict:
                     countdict[item] = countdict[item]+1
             else:
                     countdict[item] = 1
    countList = countdict.values()
    maxcount = max(countList)
     modeList = []
     for item in countdict:
             if countdict[item] == maxcount:
                     modeList.append(item)
     return modeList