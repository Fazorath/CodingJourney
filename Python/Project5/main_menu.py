## Yoenis Hernandez
## COP 2002 0.M2
## Oct 12, 2023
## Using Functions Project 5
## Using several functions, it will prompt the user a menu
## User chooses an option from menu and depending on choice it will bring up corresponding function
## Function produces a random port or random name and asks for vice versa
## after user inputs the 'correct answer' it will validate using a series of while and If loops
## if right, prompts another question
## if wrong. try again. same question
## if m. takes you to main menu
## Added hints say 'hint' on your 2nd choice i added them for testing but i actually managed to learn 
## the ports from so much testing lol
from random import randrange

port = [20,21,22,23,25,53,67,68,80,110,137,139,143,161,162,389,443,445,3389]
protocol = ['FTP', 'FTP', 'SSH', 'Telnet', 'SMTP', 'DNS', 'DHCP', 'DHCP', 'HTTP',
            'POP3', 'netBIOS', 'netBIOS', 'IMAP', 'SNMP', 'SNMP', 'LDAP', 'HTTPS',
            'SMB', 'RDP']
## Checking if right right Lenght on the List.
# print(len(port))
# print(len(protocol))    

## Finished OCT 20
def numToName(portNumber,portNumArray=[20,21,22,23,25,53,67,68,80,110,137,139,143,161,162,389,443,445,3389], portNameArray=['FTP', 'FTP', 'SSH', 'Telnet', 'SMTP', 'DNS', 'DHCP', 'DHCP', 'HTTP',
            'POP3', 'netBIOS', 'netBIOS', 'IMAP', 'SNMP', 'SNMP', 'LDAP', 'HTTPS',
            'SMB', 'RDP']): 
    while True: 
        random_index = randnumber() #using function to find random pos (1,19)
        randomnumber = portNumArray[random_index] # random position is assigned to variable
        correct = portNameArray[random_index] # random position is given to "Correct" Variable
        prompt = f"What is the Protocol for port {randomnumber} (m=menu)? " # Prompt
        
        while True: # main while loop to validate
            question = input(prompt) # input assigned to variable
            if question == correct: # if input is equal to correct variable assigned
                print(f"Correct Answer: {correct} !\n")  # added to show the correct answer not in rubric but looks cleaner
                break  # Break the inner loop and generate a new random number for the next question
            elif question == 'm': # if input is m
                print("Choice: Menu")
                return  # Exit the function 
            elif question =="": # if input is blank prompt question again.
                print(question)
            elif question =='hint':  ## Messing with hints
                print(f"Hint: {correct}\n")
            else:
                print(f"Sorry, Not Quite Right!\nTry Again:\n")
# which uses the portNumber to find it in the portNumArray  and find the corresponding port name in the portNameArray.

## Essentally the same as function above EXCEPT look at comment
def nameToNum(portNumber,portNumArray=[20,21,22,23,25,53,67,68,80,110,137,139,143,161,162,389,443,445,3389],portNameArray=['FTP', 'FTP', 'SSH', 'Telnet', 'SMTP', 'DNS', 'DHCP', 'DHCP', 'HTTP',
            'POP3', 'netBIOS', 'netBIOS', 'IMAP', 'SNMP', 'SNMP', 'LDAP', 'HTTPS',
            'SMB', 'RDP']):
    while True:
        random_index = randname()
        randomName = portNameArray[random_index]
        correct = portNumArray[random_index]
        prompt = f"What is the Number for protocol {randomName} (m=menu)? "
        
        while True:
            question = input(prompt)
            if question == str(correct): #Since input returns a string i assigned the correct variable to also be a string
                ## Input is a string but 'correct' variable was int because of the array.
                print(f"Correct Answer: {correct} !\n")
                break 
            elif question == "m":
                print("Choice: Menu")
                return 
            elif question == "":
                print(question)
            elif question == 'hint':  ## Hint
                print(f"Hint: {correct}\n")
            else:
                print(f"Sorry, Not Quite Right!\nTry Again:\n")
# which uses the portName to find it in the portNameArray  and find the corresponding port number in the portNumArray.
 
## Function to get input shown in Lecture
def getinput():
    ## menu prompt
    menu = f"\nMain Menu:\n\n1. Given the Port Number, Identify the PROTOCOL\n2. Given the Port Protocol, Identify the Port NUMBER\n3. Exit\n"
    userchoice = ''
    answerchoice = ['1','2','3']
    # Validate user input
    while (userchoice not in answerchoice): # as long as user doesnt put {answerchoice}
       userchoice = input(f"{menu}\nChoice: ") # Choose an option
       return userchoice # exit and return variable

# Choose the random port and name using functions and the randrange
def randnumber(port=port):
    randnumber = randrange(0, len(port) - 1)
    return randnumber
def randname(name=protocol):
    randname = randrange(0,len(name)-1)
    return randname

## USER INPUT
def ifusr(userchoice):
   
    if userchoice == '1':
      print("\nChoice 1: Identifiy Port Protocol\n")
      numToName(randnumber()) # call numtoname func with port number arg being the function to create a random number
    elif userchoice == '2':
      print("\nChoice 2: Identifiy Port Name\n")
      nameToNum(randname()) # call nametonum func with port name arg being the function to create a random name

## main function from lecture
## - a loop to display  menu
def main():
	userchoice = getinput() #call input function
	while(userchoice != '3'): # if user doesnt select quit
		ifusr(userchoice) # call ifusr function
		userchoice=getinput() #reset
	print("\nHopefully this helped with your studying :)") 

if __name__=="__main__":
  main()

## END OF PROGRAM
