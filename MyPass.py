def readFile():

    filename = "diceware.wordlist.asc"
    wordlist = {}

    try:
        with open(filename, 'r') as f_obj:
            dice_list = f_obj.readlines()
    except FileNotFoundError:
            print("Not able to find dice password list.")
    else:
        for i in range(2,7754):
            key,val = dice_list[i].split("\t")
            wordlist[key] = val
        return wordlist

def main():
    try:
        wordlist = readFile()

        for word in wordlist:
            print(word.rstrip())
    except KeyboardInterrupt:
        print("Good bye!")

if __name__ == '__main__':
    main()
