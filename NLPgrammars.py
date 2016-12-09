#!/usr/bin/python3
import sys


def chceckForPriority(line,orderWords):
    "chcecks if there is order adv in text"
    for word in orderWords:
        if word in line:
            return True
        else:
            return False
def splitByPriority(lineList,orderAdvList):
    "splits list of line into senteces by order adv"
    orderSeparatorIndx = []
    out = []
    lineWithIndexes = enumerate(line)
    for word in orderAdvList:
        orderSeparatorIndx.extend([pos for pos,x in lineWithIndexes if x == word])
    prev  = len(line-1)
    for index in reversed(orderSeparatorIndx):
        out.append(line[index+1:prev])
        prev = index



words = {}
words['KEY_WORDS'] = {}
words['ORDER_WORDS'] = []

#laduje z hasla plików
orderWordsFile = open('order_words.txt','r')
orderWordsContent = orderWordsFile.readline()
words['ORDER_WORDS'].extend(orderWordsContent.split(','))

actionWordsFile = open('action_words.txt','r')
actionWordsContent = actionWordsFile.readlines()
for line in actionWordsContent:
    line = line.rstrip().split(',')
    print(line)
    #nie trzeba sprawdzać czy czynnosc jest w words['KEY_WORDS']ionary bo kazda czynnosc jest unikalna
    if line[0] not in words['KEY_WORDS']:
        words['KEY_WORDS'][line[0]] = line[1:]
    else:
        words['KEY_WORDS'][line[0]].extend(line[1:])
print(words['KEY_WORDS'])
actionWordsFile.close()

adv1 = ['najpierw']

while True:
    line = sys.stdin.readline().split()
    list_polecen = []
    temporary_list = []

    for token in line:
        token2 = token.split(':')[0]
        for key in words['KEY_WORDS']:
            if token2 in words['KEY_WORDS'][key]:
                token = token + ':' + key
                break
        list_polecen.append(token)
    #     if token.split(':')[1] == 'adv' or token.split(':')[1] == 'qub':
    #             list_polecen.append(temporary_list)
    #             temporary_list = []
    #             temporary_list.append(token)
    #             continue
    #     else:
    #         temporary_list.append(token)
    # if temporary_list[0].split(':')[0] in adv1:
    #     list_polecen.insert(0,temporary_list)
    # else:
    # list_polecen.append(temporary_list)
    
    print(list_polecen)
    sys.stdout.flush()
