#!/usr/bin/env python

from num2words import num2words
import sys

write = False
if '-print' in sys.argv:
    write = True

giftArr = ["partridge in a pear-tree", "turtle doves", "french hens","colly birds","gold rings", \
           "geese a laying", "swans a swimming","maids a milking","drummers drumming", \
           "pipers piping","ladies dancing","lords a leaping"]

text = []

def printNthDay(n):
    if(n == 0):
        return str("a " + giftArr[n] + ".  ")
    elif(n == 1):
        return str(num2words(n + 1) + " " + giftArr[n] + ", and  ")
    else:
        return str(num2words(n + 1) + " "  + giftArr[n] + ",  ")

if __name__ == "__main__":
    for i in range(1, 13):
        word = num2words(i, ordinal=True).capitalize()
        text.append(str(f"On the {word} day of christmas\nMy true love gave to me:  "))
        for j in range(i-1,-1,-1):
            text.append(printNthDay(j))
        text.append(("\n   "))

    with open('nthDay.txt', 'w') as f:
        for t in text:
            f.write(t + '\n')
            if write: print(t)
        print(' wrote nthDay.txt')
