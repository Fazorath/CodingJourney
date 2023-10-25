## Handling Exceptions
## Handled using Try and Except blocks

## ZeroDivisionError
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

print("Give me 2 numbers, and ill divide them")
print("Enter 'q' to quit")


# Incorporating ZeroDivisionError into a while loop
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/ int(second_number)
    except ZeroDivisionError:
        print("You cannot divide by 0")
    else:
        print(answer)
