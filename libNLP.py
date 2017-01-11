#def getWordFromToken(word,pos=0):


def chceckForPriority(line,orderWords):
    "chcecks if there is order adv in text"
    for word in orderWords:
        if word in line:
            return True
        else:
            return False

def splitByPriority(lineList,wordsHash):
    "splits list of line into senteces by order adv that increase priority"
    orderIndx = [-1]
    out = []
    for word in lineList:
        if word[:word.index(':')] in wordsHash['ORDER_WORDS']['UP']:
            orderIndx.append(lineList.index(word))
    prev  = len(lineList)
    for index in reversed(orderIndx):
        out.append(lineList[index+1:prev])
        prev = index
    return out

def readWords(wordsHash,wordsType,filename,delimiters):
    with open(filename, mode='r') as wordsContent:
        for line in wordsContent:
            line = line.rstrip().split(delimiters[0])
            wordsHash[wordsType][line[0]] = line[1].split(delimiters[1])
