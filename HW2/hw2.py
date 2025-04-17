def create_TimeList(inputfile):

    # https://stackoverflow.com/questions/51345024/read-text-file-and-parse-in-python
    my_list = []
    for line in lines:             
        line = line.split(' ')
        line = [i.strip() for i in line]
        my_tuple = (int(line[0]), int(line[1]), line[2])
        my_list.append(my_tuple)
        
    return my_list

def timeCompareGen(listoftuples, target):

    print(target)
    
    thr = target[0]
    tmin = target[1]
    tpm = target[2]
    
    if tpm == "PM" and thr != 12:
        thr = thr + 12
    if tpm == "AM" and thr == 12:
        thr = 0

    #print(thr)
    #print(tmin)
    #print(tpm)

    ttemp = []
    ttemp.append(thr)
    ttemp.append(tmin)
    ttemp.append(tpm)

    # https://www.geeksforgeeks.org/python-convert-tuple-to-integer/
    tres=""
    for i in ttemp:
        if i != ttemp[2]:
            tres+=str(i)
    tres=int(tres)

    #print(tres)
    #print("--------------------------------")

    newList = []

    for i in listoftuples:
        
        ghr = i[0]
        gmin = i[1]
        gpm = i[2]
   
        
        if gpm == "PM" and ghr != 12:
            ghr = ghr + 12
        elif gpm == "AM" and ghr == 12:
            ghr = 0

        gtemp = []
        gtemp.append(ghr)
        gtemp.append(gmin)
        gtemp.append(gpm)

        gres=""
        for j in gtemp:
            if j != gtemp[2]:
                if j < 10:
                    gres+="0"+str(j)
                else:
                    gres+=str(j)
        gres=int(gres)

        #print(gres)
        if gres < tres:
            #print("add 2400 if less than")
            gres = gres + 2400

        #print(gres)
        #print(tres)
        #print("subtract")

        nres = gres - tres

        print(nres)

        # newList.append((nhr,nmin))

        # https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/
        if nres < 1000:
            straight = '0' + str(nres)
        else:
            straight = str(nres)
        gay = list(straight)
        print(gay)
        if len(gay) > 2:
            if int(gay[2]) > 4:
                gay[2] = int(gay[2]) - 4
                gay[2] = str(gay[2])
            print(gay)
        
        # https://stackoverflow.com/questions/4647050/collect-every-pair-of-elements-from-a-list-into-tuples-in-python
        o = [(gay[i],gay[i+1]) for i in range(0,len(gay),2)]
        print(o)

        e = []
        for t in o:
            num1 = int(t[0])
            num2 = int(t[1])
            combine = num1 * 10 + num2
            e.append(combine)
        
        print(e)

        print("--------------------------------")
    



    print("result")
    print(newList)

    print("--------------------------------")
    return

file = open('abc.txt')
lines = file.readlines()
file.close()
a = create_TimeList(lines)
print(a)
b = timeCompareGen(a, (a[0][0], a[0][1], a[0][2]))
print(b)