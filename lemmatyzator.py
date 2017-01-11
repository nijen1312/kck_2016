#!/usr/bin/python3

#modul odpowiada za sprowadzanie slow w zdaniu do ich form podstawowych
#np. "jedź do bazy" zamienia na "jechać do baza"

import sys
lineDelimeters = ['\t',]
dicFile = open('dictionary.txt','r')
dictionary = {}

#poniższa pętla for wczytuje linie z pliku z odmianami słów do hash'a pythonowego
#kluczem w hash'u jest odmienione słowo a wartością dla klucza hash z informacjami o odmianie

for line in dicFile:
    word, lemma, info, wordType = line.split(lineDelimeters[0])
    dictionary[word]={'LEMMA':lemma,'INFO':info,'TYPE':wordType}
#pętla while oczekuje cały czas na wejście
while True:
    line = sys.stdin.readline().strip().split()
    out = []
    #pętla for przetwarza każde słowo w wejściowej lini na formę podstawową
    for word in line:
        if word in dictionary:
            out.append(dictionary[word]['LEMMA'] + ':' + dictionary[word]['INFO'].split(':')[0])
        else:
            out.append(word+':')
    print(" ".join(out))
    sys.stdout.flush()
