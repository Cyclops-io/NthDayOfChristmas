from num2words import num2words

giftArr = ["Partridge in a pear-tree", "Turtle doves", "French hens","Colly birds","Gold rings","Geese a laying", "Swans a swimming","Maids a milking","Drummers drumming","Pipers piping","Ladies dancing","Lords a leaping"]

def printNthDay(n):
    if(n == 0):
        print("a " + giftArr[n] + ".  ")
    elif(n == 1):
            print(num2words(n + 1) + " " + giftArr[n] + ", and  ")
    else:
        print(num2words(n + 1) + " "  + giftArr[n] + ",  ")

if __name__ == "__main__":
    for i in range(1, 13):
        print ("On the " + num2words(i, ordinal=True) + " day of christmas\nMy true love gave to me:  ")
        for j in range(i-1,-1,-1):
            printNthDay(j)
        print("\n   ")
