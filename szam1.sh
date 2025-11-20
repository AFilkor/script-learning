#!/bin/bash

#adatbevitel
read -p 'elso szam érteke:' a
echo A szam érteke $a
read -p 'A masodik szam érteke:' b
echo B szam érteke $b
#egyenloeke
if(( $a==$b))
then
echo egyenloek
#kisebb,nagyobb
elif(( $a>$b))
then
echo "$a" nagyobb
else
echo "$b" nagyobb
fi


###
