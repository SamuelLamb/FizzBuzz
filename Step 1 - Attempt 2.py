### Checks to see if number is a multiple of 3, appends to list if true ###
def Three(Count, List):
    if Count % 3 == 0:
        List.append("Fizz")
    Five(Count, List)


### Checks to see if number is a multiple of 5, appends to list if true ###
def Five(Count, List):
    if Count % 5 == 0:
        List.append("Buzz")
    Printer(Count, List)


### Looping to recur the check for each number from 1 to 100 ###
def CheckLoop(Count):
    while Count < 101:
        List = []
        Three(Count,List)
        Count += 1
    print("Done!")


### Checks list length to see if any requirements were met before printing ###
def Printer(Count, List):
    if len(List) == 0:
        print(Count)
    else:
        print(''.join(List))


### Initialising variable and list before functions are called ###
List = []
Count = 1
CheckLoop(Count)
