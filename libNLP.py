
def UPDOWNRULE(lineList,priorList,pattern):
    if pattern[0]!='^UP':
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
    else:
        return [lineList[1:]]

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
            if len(delimiters)==3:
                wordsHash[wordsType][line[0]] = line[1].split(delimiters[2])
            else:
                wordsHash[wordsType][line[0]] = line[1].split(delimiters[1])

# def rules(prioritized,rulesHash):
#     orders = []
#     for list in prioritized:
#         pattern = ""
#         rule = ""
#         order = ""
#         for elem in list:
#             elem = elem.split(':')
#             try:
#                 if rule != "":
#                     pattern += ',' + elem[2]
#                     order += elem[0]
#                 if elem[2] in rulesHash:
#                     rule = rulesHash[elem[2]]
#                     print(rule)
#                     pattern += elem[2]
#                     order += elem[2]
#             except:
#                 continue
#         for r in rule:
#             if pattern == r:
#                 orders.append(order)
#                 print(order)
#     return orders

def rules(prioritized,rulesHash):
    orders = []
    for list in prioritized:
        order = []
        rules = []
        rule_dict = {}
        for elem in list:
            elem = elem.split(':')
            try:
                if elem[2] in rulesHash:
                    rules.append(rulesHash[elem[2]])
                    rule_dict[elem[2]] = elem[2]
                elif elem[2] not in rule_dict:
                    rule_dict[elem[2]] = elem[0]
            except:
                continue
        # print(order)
        # print(rule_dict)
        # print(rules)

        for rule in rules:
            rule = rule[0].split(',')
            print(rule)
            licznik = len(rule)
            order = []
            for elem in rule:
                if elem in rule_dict:
                    order.append(rule_dict[elem])
                    # print(order)
                    licznik -= 1
                else:
                    break
            if licznik == 0:
                orders.append(order)
    return orders
