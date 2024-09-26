def testFunct(samplelist:list,var1:int):
    list_result = []
    samplelist.sort()
    for i in range(len(samplelist)):
        first = samplelist[i]
        for j in range(i+1,len(samplelist)):
            second = samplelist[j]
            if first + second == var1:
                list_result.append((first,second))
    return list_result
            

testout = testFunct([2,4,6,3,5,7,8,1,9],10)
print(testout)

testout2 = testFunct([2,3,4,5],10)
print(testout2)
