file="C:/Users/ITE/myData.txt"
readyToEnd=False
while (not readyToEnd):
    firstNum=input("First number:  ")
    if (firstNum=="q"):
        readyToEnd=True
    if (not readyToEnd):
        secondNum=input("Second number:  ")
    if (secondNum=="q"):
        readyToEnd=True
    if (not readyToEnd):
        try:
            with open(file) as filename:
                results=filename.readlines()
            #print(results)
            answer=int(firstNum)/int(secondNum)
        except ZeroDivisionError:
            print("Error dividing by 0")
        except FileNotFoundError:
            print("Couldn't find file")
        else:
            print("Success")