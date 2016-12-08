#!/usr/bin/python3
import sys


#laduje z hasla pliku
dict = {}
file = open('key_words.txt','r')
content = file.readlines()
for line in content:
    line = line.rstrip().split(',')
    if line[0] not in dict:
        dict[line[0]] = line[1:]
    else:
        dict[line[0]].extend(line[1:])
print(dict)
file.close()

adv1 = ['najpierw']

while True:
    line = input().split()
    list_polecen = []
    temporary_list = []

    for token in line:
        token2 = token.split(':')[0]
        for key in dict:
            if token2 in dict[key]:
                token = token + ':' + key
                break
        if token.split(':')[1] == 'adv' or token.split(':')[1] == 'qub':
                list_polecen.append(temporary_list)
                temporary_list = []
                temporary_list.append(token)
                continue
        else:
            temporary_list.append(token)
    if temporary_list[0].split(':')[0] in adv1:
        list_polecen.insert(0,temporary_list)
    else:
        list_polecen.append(temporary_list)
    print(list_polecen)
