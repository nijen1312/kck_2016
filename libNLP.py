
def UPDOWNRULE(lineList,priorList,pattern):
        out=[]
        prev=0
        for word in priorList:
            current=int(word[:word.index(":")])
            piece=lineList[prev:current]
            if piece:
                out.append(piece)
            if (word == priorList[-1]) and (len(lineList)-1 > current):
                out.append(lineList[current+1:len(lineList)])
            prev=current+1
        if pattern == "*,BUT,*,UP".split(","):
            out[1]+=out[2]
            out.pop(2)
        out[0], out[1] = out[1], out[0]
        return out

def chceckForPriority(line,orderWords):
    "chcecks if there is order adv in text"
    for word in orderWords:
        if word in line:
            return True
        else:
            return False
def matchOrderRules(orderIndex,len):
    out = []
    prev = 0
    for word in orderIndex:
        counter=orderIndex.index(word)
        pos=int(word[:word.index(':')])
        if ((pos - prev) > 1) or (prev == 0 and pos == 1):
            out.append("*")
        if pos == len:
            out.append("$"+word[word.index(':')+1:])
        elif pos == 0:
            out.append("^"+word[word.index(':')+1:])
        else:
            out.append(word[word.index(':')+1:])
        prev=pos
    return out

def splitByPriority(lineList,wordsHash):
    "splits list of line into senteces by order adv that increase priority"
    orderIndx = []
    out = []
    for word in lineList:
        lemma = word[:word.index(':')]
        if lemma == "ale":
            orderIndx.append(str(lineList.index(word))+':BUT')
        if lemma == "i":
            orderIndx.append(str(lineList.index(word))+':AND')
        if lemma == "a":
            orderIndx.append(str(lineList.index(word))+':AND')
        if lemma in wordsHash['ORDER_WORDS']['UP'] :
            orderIndx.append(str(lineList.index(word))+':UP')
        if lemma in wordsHash['ORDER_WORDS']['DOWN'] :
            orderIndx.append(str(lineList.index(word))+':DOWN')
    # orderIndx.append(str(len(lineList)-1)+":END")

    return orderIndx
    # prev  = len(lineList)
    # for index in reversed(orderIndx):
    #     out.append(lineList[index+1:prev])
    #     prev = index
    # return out

def readWords(wordsHash,wordsType,filename,delimiters):
    with open(filename, mode='r') as wordsContent:
        for line in wordsContent:
            line = line.rstrip().split(delimiters[0])
            wordsHash[wordsType][line[0]] = line[1].split(delimiters[1])
