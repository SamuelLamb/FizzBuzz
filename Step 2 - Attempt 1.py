### Checks to see if number is a multiple of 3 and appends the list if true ###
def Three(Count, List):
    if Count % 3 == 0:
        List.append("Fizz")
    Five(Count, List)


### Checks to see if number is a multiple of 5 and appends the list if true ###
def Five(Count, List):
    if Count % 5 == 0:
        List.append("Buzz")
    Seven(Count, List)


### Checks to see if number is a multiple of 7 and appends the list if true ###
def Seven(Count, List):
    if Count % 7 == 0:
        List.append("Bang")
    Eleven(Count, List)


### Checks to see if number is a multiple of 11 and appends the list if true ###
def Eleven(Count, List):
    if Count % 11 == 0:
        List = ["Bong"]
    Thirteen(Count, List)


### Checks to see if number is a multiple of 13. If so, all strings after the first string beginning with "B" are removed, and the previous checks are repeated ###
def Thirteen(Count, List):
    if Count % 13 == 0:
        if List.count("Buzz") == 1:
            List.insert(List.index("Buzz"), "Fezz")
        elif List.count("Bang") == 1:
            List.insert(List.index("Bang"), "Fezz")
        elif List.count("Bong") == 1:
            List.insert(0, "Fezz")
        else:
            List.append("Fezz")
    Seventeen(Count, List)


### Checks to see if number is a multiple of 17. If so, the list is reversed ###
def Seventeen(Count, List):
    if Count % 17 == 0:
        List.reverse()
    Printer(Count, List)


### Looping to recur the check for each number from 1 to 100 ###
def CheckLoop(Count):
    while Count < 101:
        List = []
        Three(Count, List)
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
Count = 1
CheckLoop(Count)
