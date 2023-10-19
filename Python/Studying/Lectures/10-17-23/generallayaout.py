from random import randrange


port = [20,21,22,23,25,53,67,68,80,110,137,139,143,161,162,389,443,445,3389]

protocol = ['FTP', 'FTP', 'SSH', 'Telnet', 'SMTP', 'DNS', 'DHCP', 'DHCP', 'HTTP',
            'POP3', 'netBIOS', 'netBIOS', 'IMAP', 'SNMP', 'SNMP', 'LDAP', 'HTTPS',
            'SMB', 'RDP']

def numToName(portNumArray,portNameArray,portNumber): 
  pass
 # which uses the portNumber to find it in the portNumArray  and find the corresponding port name in the portNameArray.

def nameToNum(portNumArray,portNameArray,portNumber):
  pass
 # which uses the portName to find it in the portNameArray  and find the corresponding port number in the portNumArray.
 
def getinput():
  choice = 0
  while choice == 0:
    print("1. Given the Port Number, Identify the Protocol")
    print("2. Given the Port Protocol, Identify the Port Number")
    print("3. Exit\n")
    
    ## What to do with user response.
    ## Validating user input
    choice = (input("Choice: "))
    if choice == '1':
        print("\nIdentify Port Number:\n")
        ## Call num to name function 
    elif choice == '2':
        print("\nIdentify Port Protocol:\n")
        ## Call name to num function 
    elif choice == '3':
        print("\nHopefully this program helped in studying !!")
    elif choice == 'm':
        getinput() ## Loops if user presses M as their Choice
    else:
       print("Try one more time using the numbers: \n")
       getinput()


def main(): ## What you want to happen / intro to pseudocode
#   print(""" 
# Project must start by checking rubric:
# 1. Print a menu
# 1.1 Menu needs 3 options
# 1.2 Take user input This will happen multiple times user get input function

# 2. If user input 1
# 3. if user input is 2
# 4. else print end message
#         """)
  # getinput()
  pass
 # Call Every other Function

if __name__=="__main__":
  main()