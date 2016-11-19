#!/usr/bin/python3
import sys
import operator

#część wspólna dwóch list
def compare(list1,list2):
    c = set(list1) & set(list2)
    return len(c)

def action(comp):
    a = comp.index(max(comp))
    return a

#laduje z hasla pliku
dict = {}
file = open('key_words.txt','r')
content = file.readlines()
for line in content:
    line = line.rstrip().split(',')
    if line[0] not in dict:
        dict[line[0]] = line[2:]
    else:
        dict[line[0]].extend(line[2:])
print(dict)
file.close()

while True:
    line = input().split()
    comp = {}
    for key in dict:
        comp[key] = (compare(dict[key],line))
    print(comp)
    print(max(comp, key=comp.get))
