from random import randrange



port = [20,21,22,23,25,53,67,68,80,110,137,139,143,161,162,389,443,445,3389]
protocol = ['FTP', 'FTP', 'SSH', 'Telnet', 'SMTP', 'DNS', 'DHCP', 'DHCP', 'HTTP',
            'POP3', 'netBIOS', 'netBIOS', 'IMAP', 'SNMP', 'SNMP', 'LDAP', 'HTTPS',
            'SMB', 'RDP']

def numToName(portNumber,portNumArray=[20,21,22,23,25,53,67,68,80,110,137,139,143,161,162,389,443,445,3389], portNameArray=['FTP', 'FTP', 'SSH', 'Telnet', 'SMTP', 'DNS', 'DHCP', 'DHCP', 'HTTP',
            'POP3', 'netBIOS', 'netBIOS', 'IMAP', 'SNMP', 'SNMP', 'LDAP', 'HTTPS',
            'SMB', 'RDP']): 
  iscorrect = True
  while iscorrect == False:
      randnumber()
      question
  while iscorrect == True:
    randomnumber = portNumArray[portNumber]
    correct = portNameArray[portNumber]
    question = input(f"What is the Port Protocol to this Port Number( m to menu ) {randomnumber}: ")
    while(question==correct):
        print("Correct")
        break
    if(question==''):
       question
       continue
    elif( question == 'm'):
       print(f"Choice: menu")
       break
    elif (question != correct):
       print(f"Sorry, Not Quite Right: {correct} !\nTry Again:\n")
       iscorrect == False
 # which uses the portNumber to find it in the portNumArray  and find the corresponding port name in the portNameArray.



def nameToNum(portNumber,portNumArray=[20,21,22,23,25,53,67,68,80,110,137,139,143,161,162,389,443,445,3389],portNameArray=['FTP', 'FTP', 'SSH', 'Telnet', 'SMTP', 'DNS', 'DHCP', 'DHCP', 'HTTP',
            'POP3', 'netBIOS', 'netBIOS', 'IMAP', 'SNMP', 'SNMP', 'LDAP', 'HTTPS',
            'SMB', 'RDP']):
  randomname = portNameArray[portNumber]
  correctnum = portNumArray[portNumber]
  print(correctnum)
  iscorrect = True
  question = int(input(f"What is the Correct Port Number for this Protocol - {randomname}: "))
  
  while(question):
      if(question==correctnum):
          print("Correct!!\nHere is another one:\n")
          randnumber()
      elif(question==''):
          question
      elif(question=="m"):
          print(f"Choice: Menu") 
          break
      else:
          print("\nSorry, Not Quite Right !\nTry Again:\n")
          randnumber()
          nameToNum(randnumber())
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



def randnumber():
    randnumber = randrange(1,19)
    return randnumber



def ifusr(userchoice):
   ## USER INPUT
   if userchoice == '1':
      print("\nChoice 1: Identifiy Port Protocol\n")
      randomPort = randrange(1,19)
      numToName(randomPort)
   elif userchoice == '2':
      print("\nChoice 2: Identifiy Port Name\n")
      randnumber()
      nameToNum(randnumber())
   
   

def main():
	userchoice = getinput()
	while(userchoice != '3'):
		ifusr(userchoice)
		userchoice=getinput()
	print("Hopefully this helped with your studying")

  

      


if __name__=="__main__":
  main()