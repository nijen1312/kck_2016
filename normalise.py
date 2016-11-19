#!/usr/bin/python3
import sys, re

#czyta linia po lini z stdin
#zamienia wszystkie litery na małe (lower)
#usuwa wszystkie znaki poza literami, cyframi i spacjami (sub)
#drukuje wynik na stdio


while True:
        line = sys.stdin.readline().strip().lower()
        line = re.sub(r"\W"," ",line)
        print(line)
        sys.stdout.flush()