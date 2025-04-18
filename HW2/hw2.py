import sys

class EmptyFile(Exception):
    pass

class ImproperTime(Exception):
    pass

def create_TimeList(inputfile):

    # https://stackoverflow.com/questions/51345024/read-text-file-and-parse-in-python
    my_list = []
    for line in lines:             
        line = line.split(' ')
        line = [i.strip() for i in line]
            
        if len(line) != 3:
            raise ImproperTime("Incorrect number of fields")
        
        try:
            hours = int(line[0])
            minutes = int(line[1])
            ampm = line[2]
            
            if hours < 1 or hours > 12:
                raise ImproperTime("Hours must be between 1 and 12")
            
            if minutes < 0 or minutes > 59:
                raise ImproperTime("Minutes must be between 0 and 59")
            
            if ampm not in ["AM", "PM"]:
                raise ImproperTime("AM/PM must be either 'AM' or 'PM'")
            
            my_tuple = (hours, minutes, ampm)
            my_list.append(my_tuple)
            
        except ValueError:
            raise ImproperTime("Invalid number format")
    
    return my_list

def timeCompareGen(listoftuples, target):

    # print(target)
    
    thr = target[0]
    tmin = target[1]
    tpm = target[2]
    
    if tpm == "PM" and thr != 12:
        thr += 12
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

    result = []

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

        # print(nres)

        # https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/
        if nres < 1000:
            strres = '0' + str(nres)
        else:
            strres = str(nres)
        listres = list(strres)
        # print(listres)
        if len(listres) > 2:
            if int(listres[2]) > 4:
                listres[2] = int(listres[2]) - 4
                listres[2] = str(listres[2])
            # print(listres)
        
        # https://stackoverflow.com/questions/4647050/collect-every-pair-of-elements-from-a-list-into-tuples-in-python
        o = [(listres[i],listres[i+1]) for i in range(0,len(listres),2)]
        # print(o)

        e = []
        for t in o:
            num1 = int(t[0])
            num2 = int(t[1])
            combine = num1 * 10 + num2
            e.append(combine)
        
        # print(e)
        
        # new
        if len(e) >= 2:
            result.append((e[0], e[1]))
        else:
            result.append((0, e[0]))

        # print("--------------------------------")
    
    # print("result")
    # print(result)

    # print("--------------------------------")
    return result

############ MAIN #############

try:
    with open(sys.argv[1]) as file:
        lines = file.readlines()

    if not lines:
        raise EmptyFile("The file is empty")

    a = create_TimeList(lines)

    c = [str(i[0]) + ':' + ('0' + str(i[1]) if i[1]<10 else str(i[1])) + " " + str(i[2]) for i in a] # ew ugly if statment 

    print(c)

    # -----------------------------------------------------------

    unsortedTres = []

    for i in a:
        thr = i[0]
        tmin = i[1]
        tpm = i[2]
        
        if tpm == "PM" and thr != 12:
            thr = thr + 12
        if tpm == "AM" and thr == 12:
            thr = 0

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
        unsortedTres.append(tres)

    sortedTres = sorted(unsortedTres)

    og = []

    for i in sortedTres:
        time_str = str(i).zfill(4)

        hours = int(time_str[:2])
        minutes = int(time_str[2:])


        ampm = "PM" if hours >= 12 else "AM"


        if hours > 12:
            hours -= 12
        elif hours == 0:
            hours = 12

        og.append((hours, minutes, ampm))

    print(og[len(og)-1])
    print(og)

    # ---------------------------------------------------------------------

    target = (a[0][0], a[0][1], a[0][2])
    b = timeCompareGen(a, target)
    print(b)

except IndexError:
    print("Error: No input file specified")
    sys.exit(1)
except FileNotFoundError:
    print(f"Error: File '{input_file}' not found")
    sys.exit(1)
except EmptyFile as e:
    print(f"Error: {str(e)}")
    sys.exit(1)
except ImproperTime as e:
    print(f"Error: {str(e)}")
    sys.exit(1)