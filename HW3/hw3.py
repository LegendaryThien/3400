import sys

fileName = sys.argv[1]
inFile = open(fileName)

lines = inFile.readlines()
inFile.close()

n = int(lines[0].rstrip())
hb = {}
ptrs = {}

for i in range(n):
    hb[str(i)] = []

for line in lines[1:]:
    
    line = line.rstrip()
     
     #error handle skip empty lines
    if line == '':
        continue
    
    parts = line.split(',')
    if len(parts) == 2:
        if parts[0].isdigit():
            # if its a digit -> heap block
            src = parts[0]
            dst = parts[1]
            hb[src].append(dst)
        else:
            # if its not a digit, probably string or char -> pointer
            name = parts[0]
            dst = parts[1]
            ptrs[name] = dst

#for k in sorted(hb.keys(), key=int):
#    print(k, '->', hb[k])

#for k in ptrs:
#    print(k, '->', ptrs[k])

mrked = []

def mark(node):
    
    #error handle if node alr in mark
    if node in mrked:
        return
    
    mrked.append(node)
    for neighbor in hb[node]:
        mark(neighbor)

for k in ptrs:
    start = ptrs[k]
    mark(start)

allnodes = []
for i in range(n):
    allnodes.append(str(i))

swept = []
for node in allnodes:
    if node not in mrked:
        swept.append(node)

mrkedint = [int(x) for x in mrked]
mrkedint.sort()
sweptint = [int(x) for x in swept]
sweptint.sort()

print('Marked nodes:', end=' ')
for i in range(len(mrkedint)):
    print(mrkedint[i], end='')
    if i != len(mrkedint) - 1:
        print(' ', end='')
print()

print('Swept nodes:', end=' ')
for i in range(len(sweptint)):
    print(sweptint[i], end='')
    if i != len(sweptint) - 1:
        print(' ', end='')
print()