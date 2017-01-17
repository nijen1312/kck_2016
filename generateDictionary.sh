#!/bin/bash

function genDict() {
  if [[ -e $3 ]]; then
    rm $3
  fi
  filename="$1"
  cut -f2 -d":" $filename | {
  while read -r line
  do
      IFS=','
      for x in $line
      do
        grep $x $2 >> $3
      done
  done
  }
  grep qub $2 >> $3
  grep adv $2 >> $3
}
genDict $1 $2 $3
