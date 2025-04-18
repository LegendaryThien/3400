import sys

class EmptyFile(Exception):
    pass

class ImproperTime(Exception):
    pass

def create_TimeList(inputfile):

    with open(inputfile) as file:
        lines = file.readlines()

    if not lines:
        raise EmptyFile("The file is empty")

    # https://stackoverflow.com/questions/51345024/read-text-file-and-parse-in-python
    # https://learning.oreilly.com/library/view/learning-python-5th/9781449355722/ch04.html#type-specific_methods
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
    thr = target[0]
    tmin = target[1]
    tpm = target[2]
    
    if tpm == "PM" and thr != 12:
        thr += 12
    if tpm == "AM" and thr == 12:
        thr = 0

    ttemp = []
    ttemp.append(thr)
    ttemp.append(tmin)
    ttemp.append(tpm)

    tres=""
    for i in ttemp:
        if i != ttemp[2]:
            tres+=str(i)
    tres=int(tres)

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

        if gres < tres:
            gres = gres + 2400

        nres = gres - tres

        if nres < 1000:
            strres = '0' + str(nres)
        else:
            strres = str(nres)
        listres = list(strres)
        
        if len(listres) > 2:
            if int(listres[2]) > 4:
                listres[2] = int(listres[2]) - 4
                listres[2] = str(listres[2])
        
        
        o = [(listres[i],listres[i+1]) for i in range(0,len(listres),2)]

        e = []
        for t in o:
            num1 = int(t[0])
            num2 = int(t[1])
            combine = num1 * 10 + num2
            e.append(combine)
        
        if len(e) >= 2:
            yield (e[0], e[1])
        else:
            yield (0, e[0])

############ MAIN #############

try:
    
    # 1 and 7
    
    timeList = create_TimeList(sys.argv[1])
    target = timeList[0]

    # 4
    c = [str(i[0]) + ':' + ('0' + str(i[1]) if i[1]<10 else str(i[1])) + " " + str(i[2]) for i in timeList] # ew ugly if statment 

    print(c)

    # 5 -----------------------------------------------------------
    def hrtomin(t):
        hours = t[0]
        if t[2] == "PM" and hours != 12:
            hours += 12
        elif t[2] == "AM" and hours == 12:
            hours = 0
        return hours * 60 + t[1]
    
    maxtime = max(timeList, key=hrtomin)
    print(maxtime)
    
    # 6 -----------------------------------------------------------

    unsortedTres = []

    for i in timeList:
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

    print(og)

    # 8 -----------------------------------------------------------

    tdiffs = [diff for diff in timeCompareGen(timeList, target)]
    print(tdiffs)

except IndexError:
    print("Error: No input file specified")
    sys.exit(1)
except FileNotFoundError:
    print(f"Error: File '{sys.argv[1]}' not found")
    sys.exit(1)
except EmptyFile as e:
    print(f"Error: {str(e)}")
    sys.exit(1)
except ImproperTime as e:
    print(f"Error: {str(e)}")
    sys.exit(1)