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
        print(rule_dict)
        print(rules)

        for rule in rules:
            rule = rule[0].split(',')
            print(rule)
            licznik = len(rule)
            order = []
            for elem in rule:
                if elem in rule_dict:
                    order.append(rule_dict[elem])
                    print(order)
                    licznik -= 1
                else:
                    break
            if licznik == 0:
                orders.append(order)
    return orders
