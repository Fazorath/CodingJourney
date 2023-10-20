from random import randrange




port = [20,21,22,23,25,53,67,68,80,110,137,139,143,161,162,389,443,445,3389]
protocol = ['FTP', 'FTP', 'SSH', 'Telnet', 'SMTP', 'DNS', 'DHCP', 'DHCP', 'HTTP',
            'POP3', 'netBIOS', 'netBIOS', 'IMAP', 'SNMP', 'SNMP', 'LDAP', 'HTTPS',
            'SMB', 'RDP']

## Finished OCT 20
def numToName(portNumber,portNumArray=[20,21,22,23,25,53,67,68,80,110,137,139,143,161,162,389,443,445,3389], portNameArray=['FTP', 'FTP', 'SSH', 'Telnet', 'SMTP', 'DNS', 'DHCP', 'DHCP', 'HTTP',
            'POP3', 'netBIOS', 'netBIOS', 'IMAP', 'SNMP', 'SNMP', 'LDAP', 'HTTPS',
            'SMB', 'RDP']): 
    while True:
        random_index = randnumber()
        randomnumber = portNumArray[random_index]
        correct = portNameArray[random_index]
        prompt = f"What is the Port Protocol to this Port Number (m to menu) {randomnumber}: "
        
        while True:
            question = input(prompt)
            if question == correct:
                print(f"Correct: {correct} !\n")
                break  # Break the inner loop and generate a new random number for the next question
            elif question == 'm':
                print("Choice: menu")
                return  # Exit the function To other while loop
            elif question == "":
                print(question)
            # elif question == 'hint':  ## Messing with hints
            #     print(f"Hint: {correct[0:2]}\n")
            else:
                print(f"Sorry, Not Quite Right!\nTry Again:\n")
            
 # which uses the portNumber to find it in the portNumArray  and find the corresponding port name in the portNameArray.



def nameToNum(portNumber,portNumArray=[20,21,22,23,25,53,67,68,80,110,137,139,143,161,162,389,443,445,3389],portNameArray=['FTP', 'FTP', 'SSH', 'Telnet', 'SMTP', 'DNS', 'DHCP', 'DHCP', 'HTTP',
            'POP3', 'netBIOS', 'netBIOS', 'IMAP', 'SNMP', 'SNMP', 'LDAP', 'HTTPS',
            'SMB', 'RDP']):
    while True:
        random_index = randname()
        randomName = portNameArray[random_index]
        correct = portNumArray[random_index]
        prompt = f"What is the Port Number to this Port Protocol (m to menu) {randomName}: "
        
        while True:
            question = input(prompt)
            if question == str(correct):
                print(f"Correct: {correct} !\n")
                break  # Break the inner loop and generate a new random number for the next question
            elif question == "m":
                print("Choice: menu")
                return  # Exit the function if the user chooses the menu
            elif question == "":
                print(question)
            # elif question == 'hint':  ## Hint
            #     print(f"Hint: {correct}\n")
            else:
                print(f"Sorry, Not Quite Right!\nTry Again:\n")
              
      # which uses the portName to find it in the portNameArray  and find the corresponding port number in the portNumArray.
 


def getinput():
    ## menu prompt
    menu = f"\n1. Given the Port Number, Identify the Protocol\n2. Given the Port Protocol, Identify the Port Number\n3. Exit\n"
    userchoice = ''
    answerchocie = ['1','2','3']
    # Validate user input
    while (userchoice not in answerchocie):
       userchoice = input(f"{menu}\nChoice: ")
       return userchoice



def randnumber(port=port):
    randnumber = randrange(0, len(port) - 1)
    return randnumber

def randname(name=protocol):
    randname = randrange(0,len(name)-1)
    return randname

def ifusr(userchoice):
   ## USER INPUT
   if userchoice == '1':
      print("\nChoice 1: Identifiy Port Protocol\n")
      numToName(randnumber())
   elif userchoice == '2':
      print("\nChoice 2: Identifiy Port Name\n")
      randnumber()
      nameToNum(randnumber())
   
   

def main():
	userchoice = getinput()
	while(userchoice != '3'):
		ifusr(userchoice)
		userchoice=getinput()
	print("\nHopefully this helped with your studying :)")

  

      


if __name__=="__main__":
  main()