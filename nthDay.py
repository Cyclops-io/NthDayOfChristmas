from num2words import num2words

giftArr = ["partridge in a pear-tree", "turtle doves", "french hens","colly birds","gold rings","geese a laying", "swans a swimming","maids a milking","drummers drumming","pipers piping","ladies dancing","lords a leaping"]

def printNthDay(n):
    if(n == 0):
        print("a " + giftArr[n] + ".  ")
    elif(n == 1):
            print(num2words(n + 1) + " " + giftArr[n] + ", and  ")
    else:
        print(num2words(n + 1) + " "  + giftArr[n] + ",  ")

if __name__ == "__main__":
    for i in range(1, 13):
        print ("On the " + num2words(i, ordinal=True).capitalize() + " day of christmas\nMy true love gave to me:  ")
        for j in range(i-1,-1,-1):
            printNthDay(j)
        print("\n   ")
