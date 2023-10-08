def subtractValues(number):
    result = 100
    currentNum = 7
    while(currentNum >= number):
        result -= currentNum
        result -= 1
    return result

def main():
    print(subtractValues(7))

def calculateArea(length=0, width=0):

    return length*width+length+width

print(calculateArea(5))
