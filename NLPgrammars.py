#!/usr/bin/python3
import sys
from libNLP import *

delimiters=[":",","]
words = {}
words['ACTION_WORDS'] = {}
words['ORDER_WORDS'] = {}

#laduje wyrazy z plików

readWords(words,'ORDER_WORDS','order_words.txt',delimiters)
readWords(words,'ACTION_WORDS','action_words.txt',delimiters)

print(words)
while True:
    line = sys.stdin.readline().split()
    if "na:" in line and "końcu:" in line:
        nIndx=line.index("na:")
        kIndx=line.index("końcu:")
        if nIndx == kIndx - 1:
            line = line[:nIndx]+["na końcu:"]+line[kIndx+1:]

    if "na:" in line and "początku:" in line:
        nIndx=line.index("na:")
        kIndx=line.index("początku:")
        if nIndx == kIndx - 1:
            line = line[:nIndx]+["na początku:"]+line[kIndx+1:]

    list_polecen = []
    temporary_list = []
    for token in line:
        word = token.split(':')[0]
        for key in words['ACTION_WORDS']:
            if word in words['ACTION_WORDS'][key]:
                token = token + ':' + key
                break
        list_polecen.append(token)
    prioritized=splitByPriority(list_polecen, words)
    
#     #     if token.split(':')[1] == 'adv' or token.split(':')[1] == 'qub':
#     #             list_polecen.append(temporary_list)
#     #             temporary_list = []
#     #             temporary_list.append(token)
#     #             continue
#     #     else:
#     #         temporary_list.append(token)
#     # if temporary_list[0].split(':')[0] in adv1:
#     #     list_polecen.insert(0,temporary_list)
#     # else:
#     # list_polecen.append(temporary_list)
#

    sys.stdout.flush()
