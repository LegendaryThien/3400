import sys

def countPairs(filename):
    dictOfPairs = {}
    inFile = open(filename)
    content = ''
    for line in inFile:
        content += line
    content = content.lower()
    inFile.close()

    letters = set('abcdefghijklmnopqrstuvwxyz')
    i = 0
    while i < len(content) - 1:
        if content[i] in letters and content[i+1] in letters:
            pair = content[i] + content[i+1]
            if pair in dictOfPairs:
                dictOfPairs[pair] = dictOfPairs[pair] + 1
            else:
                dictOfPairs[pair] = 1
        i = i + 1
    return dictOfPairs

def getTopFivePairs(dictOfPairs):
    pairs_list = []
    for pair in dictOfPairs:
        pairs_list.append((pair, dictOfPairs[pair]))

    def get_count(item):
        return item[1]

    sp = sorted(pairs_list, key=get_count, reverse=True)
    sorted_pairs = []
    for item in sp:
        sorted_pairs.append(item)

    result = []
    if sorted_pairs:
        num_pairs = 5
        if len(sorted_pairs) < 5:
            num_pairs = len(sorted_pairs)
        i = 0
        while i < num_pairs:
            result.append(sorted_pairs[i])
            i = i + 1
            
        if len(sorted_pairs) > 5:
            fifth_count = sorted_pairs[4][1]
            j = 5
            while j < len(sorted_pairs):
                if sorted_pairs[j][1] == fifth_count:
                    result.append(sorted_pairs[j])
                else:
                    break
                j = j + 1

    return result

def createFollowsDict(dictOfPairs, letter):
    follows_dict = {}
    letters = 'abcdefghijklmnopqrstuvwxyz'
    i = 0
    while i < 26:
        char = letters[i]
        follows_dict[char] = 0
        i = i + 1

    for pair in dictOfPairs:
        if len(pair) == 2 and pair[0] == letter:
            follows_dict[pair[1]] = follows_dict[pair[1]] + dictOfPairs[pair]
    return follows_dict

input_file = sys.argv[1]
pairs = countPairs(input_file)
print(len(pairs))
total_pairs = 0
for pair, count in pairs.items():
    total_pairs = total_pairs + count
print(total_pairs)
top_pairs = getTopFivePairs(pairs)
print(top_pairs)

vowels = ['a', 'e', 'i', 'o', 'u']
for vowel in vowels:
    print(vowel)
    follows_dict = createFollowsDict(pairs, vowel)
    frequencies = []
    letters = 'abcdefghijklmnopqrstuvwxyz'
    i = 0
    while i < 26:
        char = letters[i]
        frequencies.append(follows_dict[char])
        i = i + 1
    print(frequencies)