# deviceID = 3500
# paymentTier = 1
# if (deviceID > 3000):
#     if (paymentTier == 1):
#         print("Statement A")
#     print("Statement B")
# elif (deviceID > 2000):
#     if (paymentTier == 2):
#         print("Statement C")
#     else:
#         print("Statement D")
# elif (deviceID > 1000):
#     if (paymentTier == 3):
#         print("Statement E")
#     elif (paymentTier == 2):
#         print("Statement F")
#     else:
#         print("Statement G")
# else:
#     print("Statement H")
# print("Statement I")

# deviceID = 3012
# if (deviceID >1000):
#      print("Do I know when this will print?")
# elif (deviceID > 2000):
#      print("Do I also know when this will print?")
# elif (deviceID > 3000):
#      print("When does this print?  Do I know?")
# else:
#      print("If I know when this prints, I have learned how if...elif...else statements work!")

# value = 0

# while(value < 10):
#     if(value % 3 == 0):
#         print(value)
#     value += 1


# loanedAmt = float(input('Enter Amount of loan: '))
# print(loanedAmt)


# hello = 'hello my name is blah blah blah'
# hello=hello.split()
# print(hello)
# x=10/0


def calculateValue(position1=0, position2=0):

    return position1*2+position2-5

print(calculateValue())
