import random
from generallayaout import*

# def numToName(portNumArray, portNameArray,portNumber=randrange(1,19)):
#     iscorrect = False  # Initialize to False to enter the loop
#     while not iscorrect:
#         randomnumber = portNumArray[portNumber]
#         correct = portNameArray[portNumber]
#         prompt = f"What is the Port Protocol to this Port Number (m to menu) {randomnumber}: "
#         question = input(prompt)

#         if question == correct:
#             print(f"Correct: {correct} !")
#         elif question == 'm':
#             print("Choice: menu")
#             return
#         else:
#             print(f"Sorry, Not Quite Right: {correct} !\nTry Again:\n")
#             # Set iscorrect to False to stay in the loop
#             iscorrect = False

# Example usage:
def numToName(portNumber,portNumArray=port, portNameArray=protocol):
    while True:
        random_index = random.randint(0, len(portNumArray) - 1)
        randomnumber = portNumArray[random_index]
        correct = portNameArray[random_index]
        prompt = f"What is the Port Protocol to this Port Number (m to menu) {randomnumber}: "
        
        while True:
            question = input(prompt)
            
            if question == correct:
                print(f"Correct: {correct} !")
                break  # Break the inner loop and generate a new random number for the next question
            elif question == 'm':
                print("Choice: menu")
                return  # Exit the function if the user chooses the menu
            else:
                print(f"Sorry, Not Quite Right: {correct} !\nTry Again:\n")

# Example usage:
numToName(randnumber())


