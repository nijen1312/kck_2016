#!/usr/bin/python3

#modul odpowiada za sprowadzanie slow w zdaniu do ich form podstawowych
#np. "jedź do bazy" zamienia na "jechać do baza"

import sys, re
lineDelimeters = [';',',','/']
dicFile = open('dictionary.txt','r')
dictionary = {}

#poniższa pętla for wczytuje linie z pliku z odmianami słów do hash'a pythonowego
#kluczem w hash'u jest odmienione słowo a wartością dla klucza informacje o odmianie
#oraz co zrobic żeby zamienić dane słowo na formę podstawową

for line in dicFile:
    word,data = line.split(lineDelimeters[0])
    dictionary[word]=data
#pętla while oczekuje cały czas na wejście
while True:
    line = sys.stdin.readline().strip().split()
    out = []
    #pętla for przetwarza każde słowo w wejściowej lini na formę podstawową
    for word in line:
        dicLine = dictionary[word]
        #ile uciąc z odmienionej formy
        charsToCut  = re.findall(r"[0-9]+",dicLine)[0]
        core = word[:len(word) - int(charsToCut)]
        #co dodać żeby uzyskać formę podstawową
        charsToAdd = dicLine[len(charsToCut):dicLine.index(lineDelimeters[1])] 
        out.append(core + charsToAdd)
    print(" ".join(out))
    sys.stdout.flush()
