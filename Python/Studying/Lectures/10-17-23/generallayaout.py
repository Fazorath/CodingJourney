from random import randrange
import random


port = [20,21,22,23,25,53,67,68,80,110,137,139,143,161,162,389,443,445,3389]
protocol = ['FTP', 'FTP', 'SSH', 'Telnet', 'SMTP', 'DNS', 'DHCP', 'DHCP', 'HTTP',
            'POP3', 'netBIOS', 'netBIOS', 'IMAP', 'SNMP', 'SNMP', 'LDAP', 'HTTPS',
            'SMB', 'RDP']

def numToName(portNumber,portNumArray=[20,21,22,23,25,53,67,68,80,110,137,139,143,161,162,389,443,445,3389], portNameArray=['FTP', 'FTP', 'SSH', 'Telnet', 'SMTP', 'DNS', 'DHCP', 'DHCP', 'HTTP',
            'POP3', 'netBIOS', 'netBIOS', 'IMAP', 'SNMP', 'SNMP', 'LDAP', 'HTTPS',
            'SMB', 'RDP']): 
  answer = ''
  question = input(f"What is the Port Protocol to this Port Number {portNumber}")
 # which uses the portNumber to find it in the portNumArray  and find the corresponding port name in the portNameArray.

def nameToNum(portNumArray,portNameArray,portNumber):
  print("Properly Selected")
  pass
 # which uses the portName to find it in the portNameArray  and find the corresponding port number in the portNumArray.
 
def getinput():
    ## menu prompt
    menu = f"1. Given the Port Number, Identify the Protocol\n2. Given the Port Protocol, Identify the Port Number\n3. Exit\n"
    userchoice = ''
    answerchocie = ['1','2','3']
    # Validate user input
    while (userchoice not in answerchocie):
       userchoice = input(f"{menu}\nChoice: ")
       return userchoice

def randindex(portNumArray=[20,21,22,23,25,53,67,68,80,110,137,139,143,161,162,389,443,445,3389], portNameArray=['FTP', 'FTP', 'SSH', 'Telnet', 'SMTP', 'DNS', 'DHCP', 'DHCP', 'HTTP',
            'POP3', 'netBIOS', 'netBIOS', 'IMAP', 'SNMP', 'SNMP', 'LDAP', 'HTTPS',
            'SMB', 'RDP']):
    randindex = random.randrange(1,19)
    randnum = portNumArray[randindex]
    return randnum

def ifusr(userchoice):
   ## USER INPUT
   if userchoice == '1':
      randnum = randindex()
      numToName(randnum)
   elif userchoice == '2':
      nameToNum()
   
   

def main():
	userchoice = getinput()
	while(userchoice != '3'):
		ifusr(userchoice)
		userchoice=getinput()
	print("Hopefully this helped with your studying")

  

      


if __name__=="__main__":
  main()