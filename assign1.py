def readDataFromFile(fileName):
    dict = {}
    file = open(fileName)
    for line in file:
        key, value = line.split()
        dict[key] = value

    return dict

def meanLength(fileName):
    list = []
    readLen = 0.0
    lineCount = 0.0
    file = open(fileName)
    for line in file:
        lineCount += 1
        list = line.split()
        #print(len(list[1]))
        readLen += len(list[1])
    #print(readLen)
    return readLen/lineCount


def getOverlap(left, right):
    largestOverlap = min(len(left), len(right))
    right = right[:largestOverlap]
    left = left[len(left)-largestOverlap:]
    #print("left string= " + left +  " " + str(len(left)))
    #print("right string= " + right + " " + str(len(right)))

    for i in range(largestOverlap):
        #print(i)
        if left[i:] == right[:largestOverlap -i]:
            #print(len(left[i:]))
            return left[i:]
        #left = left[i:]
        #right = right[:largestOverlap-i]
        #print("left string= " + left +  " " + str(len(left)))
        #print("right string= " + right + " " + str(len(right)))

def getAllOverlaps(reads):
    dict = {}
    #creating an empty dict with the keys from the original dict
    for key, value in reads.items():
        dict[key] = {}
    for key, value in reads.items():
        #print(value)
        for k, v in dict.items():
            if key == k:
                continue
            #print("value of value: " + key + " value of k: " + k)
            dict[key][k] = str(getOverlap(value, reads[k]))
    #print(dict)
    #assigns length of overlaps
    for i in dict:
        for k in dict[i]:
            if dict[i][k] == "None":
                dict[i][k] = 0
            else:
                dict[i][k] = len(dict[i][k])
    #print(dict)
    return dict

def prettyPrint(overlaps):
    keys = sorted(overlaps.keys())
    print("%6s" %("1"), end ='')
    for i in range(2, len(keys)+1):
        print("%3s" %i , end ='')
    print()
    for i in keys:
        print("%3s" %i, end = '' )
        for k in overlaps[i].keys():
            print("%3s" %overlaps[i][k], end = '' )                            
        print()


def findFirstRead(overlaps):    
    for k,v in overlaps.items():
        count = 0
        for x, y in overlaps[k].items():
            if overlaps[x][k] > 0:
                count += 1
        if count < 3:
            return k

    #overlaps = dict(sorted(overlaps.items()))
    #print(overlaps)
    #firstRead = 0
    #storeVal = 0
    #for k, v in overlaps.items():
        #storeKeys.append(k)
    #for i in len(storeKeys):
        #print(6473647)
    #for k, v in overlaps.items():
        #for i, j in v.items():
            #print(overlaps[k][i])
    #print(storeKeys)
    #return 0

def findKeyForLargestValue(d):
    maxKey = max(d, key=d.get)
    if d[maxKey] <= 1:
        return 0
    else:
        return maxKey
   
def findOrder(name, overlaps):
    order = [name]
    nextVal = findKeyForLargestValue(overlaps[name])
    while(nextVal != 0):
        order.append(nextVal)
        nextVal = findKeyForLargestValue(overlaps[nextVal])
    return order

def assembleGenome(readOrder, reads, overlaps):
    genome = reads[readOrder[0]]
    for i in range(len(readOrder)-1):
        #print(i)
        overlap = overlaps[readOrder[i]][readOrder[i+1]]
        #print(overlap)
        genome += reads[str(i+1)][overlap:]

    return genome


#s1 = "CGATTCCAGGCTCCCCACGGGGTACCCATAACTTGACAGTAGATCTC"
#s2 = "GGCTCCCCACGGGGTACCCATAACTTGACAGTAGATCTCGTCCAGACCCCTAGC"
#answer = 'GGCTCCCCACGGGGTACCCATAACTTGACAGTAGATCTC'

#t1 = "CTTTACCCGGAAGAGCGGGACGCTGCCCTGCGCGATTCCAGGCTCCCCACGGG"
#t2 = "GGCTCCCCACGGGGTACCCATAACTTGACAGTAGATCTCGTCCAGACCCCTAGC"
#ans2 = "GGCTCCCCACGGG"

#print(len(s1))
#print(len(s2))
#print(s1[2:])

#print(getOverlap(t1, t2))
#print(getOverlap(s2,s1))
#getOverlap(s1,s2)

fileName = r'C:\Users\samia\Spring 2022\Intro To Bioinformatics\genome-assembly.txt'
reads = readDataFromFile(fileName)
print (meanLength(fileName))
#print(reads)
overlaps = getAllOverlaps(reads)
#print(overlaps)
prettyPrint(overlaps)
name = findFirstRead(overlaps)
#print(name)
order = findOrder(name, overlaps)

genome = assembleGenome(order, reads, overlaps)
print(genome)

#ans = "['4', '2', '5', '1', '6', '3']"
#prettyPrint(overlaps)
#print(findKeyForLargestValue(overlaps["2"]))
#print(findOrder2('4', overlaps))