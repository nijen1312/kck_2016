#!/usr/bin/python3
import sys

#część wspólna dwóch list
def compare(list1,list2):
    c = set(list1) & set(list2)
    return len(c)

def action(comp):
    a = comp.index(max(comp))
    if a==0:
        return "zatankuj"
    elif a==1:
        return "magazyn"
    elif a==2:
        return "odbierz"
    elif a==3:
        return "zawiez"
    elif a==4:
        return "odpocznij"
    elif a==5:
        return "pomoz"

#laduje z hasla pliku
file = open('key_words','r')
zatankuj = file.readline().rstrip().split(',')
magazyn = file.readline().rstrip().split(',')
odbierz = file.readline().rstrip().split(',')
zawiez = file.readline().rstrip().split(',')
odpocznij = file.readline().rstrip().split(',')
pomoz = file.readline().rstrip().split(',')
file.close()

while True:
    line = input().split()
    #lista powtórzeń
    comp = []
    comp.append(compare(zatankuj,line))
    comp.append(compare(magazyn,line))
    comp.append(compare(odbierz,line))
    comp.append(compare(zawiez,line))
    comp.append(compare(odpocznij,line))
    comp.append(compare(pomoz,line))
    print(action(comp))
