### Looping to recur the check for each number from 1 to 100 ###
def CheckLoop(Count):
    while Count < 101:
        List = []
        for i in range(0, 6):
            if Count % CheckList[i] == 0:
                if i == 5:
                    List.reverse()
                else:
                    List.append(WordList[i])
            if Count % 11 == 0:
                if Count % 13 == 0:
                    List = ["Fezz", "Bong"]
                else:
                    List = ["Bong"]
        Printer(Count, List)
        Count += 1
    print("Done!")


### Checks list length to see if any requirements were met before printing. If not, the number is printed instead ###
def Printer(Count, List):
    if len(List) == 0:
        print(Count)
    else:
        print(''.join(List))


### Initialising variable and list before functions are called ###
List = []
CheckList = [3, 13, 5, 7, 11, 17]
WordList = ["Fizz", "Fezz", "Buzz", "Bang", "Bong"]
Count = 1
CheckLoop(Count)
