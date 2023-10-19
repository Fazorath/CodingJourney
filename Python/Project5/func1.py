## Function one is 
## def numToName(portNumArray,portNameArray,portNumber):
import random
## Arrays
portNumArray = [20,21,22,23,25,53,67,68,80,110,137,139,143,161,162,389,443,445,3389]
portNameArray = ['FTP','FTP','SSH','Telnet','SMTP','DNS','DHCP','DHCP','HTTP','POP3','netBIOS','netBIOS','IMAP','SNMP','SNMP','LDAP','HTTPS','SMB','RDP']




def numToName(portNumber,portNumArray=[20,21,22,23,25,53,67,68,80,110,137,139,143,161,162,389,443,445,3389],portNameArray=['FTP','FTP','SSH','Telnet','SMTP','DNS','DHCP','DHCP','HTTP','POP3','netBIOS','netBIOS','IMAP','SNMP','SNMP','LDAP','HTTPS','SMB','RDP']
,): # Array of Num and Array of Name Player input portnumber solved externally
  ## display message with the random port number
  correctAns = portNameArray[portNumber] # Which index in the array the correct answer is
  randomport = portNumArray[portNumber] # Random number is index of num array with the number generated
  
  # User Choice
  playeranswer = input(f"What is the Protocol name for this Port Number {randomport}: ")
  if playeranswer == correctAns:
    print("Congrats youre a genius")
  else:
    print("try Again")
  print(correctAns)

  ## else


