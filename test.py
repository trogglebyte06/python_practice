def biggest(a,b,c):
    disList = [a,b,c]
#disList = [6,9,3]
    datList = disList
    demList = [0,0,0]

#    print "comparing each pair"
    for x in range(len(disList)):
        for y in range(len(datList)):
#            print disList[x] , "," , datList[y]
            if disList[x] >= datList[y]:
                demList[x]+=1

#    print "here we have demList"
#    print demList

    for z in range(len(demList)):
        if demList[z] > 2:
#            print "your final answer is",datList[z]
            break

    return datList[z]

print biggest(2,2,1), "should be 2"
print biggest(1,2,3), "should be 3"
print biggest(3,1,2), "should be 3"
print biggest(2,3,1), "should be 3"
print biggest(1,3,2), "should be 3"
print biggest(2,1,3), "should be 3"
print biggest(3,2,1), "should be 3"
print biggest(3,6,9), "should be 9"
print biggest(6,9,3), "should be 9"
print biggest(9,3,6), "should be 9"
print biggest(3,3,9), "should be 9"
print biggest(9,3,9), "should be 9"
# print biggest(6,9,3)
# print biggest(9,3,6)
# print biggest(3,3,9)
# print biggest(9,3,9)

# def biggest(a,b,c):
#     disList = [a,b,c]
#     x = 0
#     for y in disList:
#         if y > x:
#             x = y
#     return x
