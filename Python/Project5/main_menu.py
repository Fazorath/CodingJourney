import random
from func1 import numToName

# Main Menu Function



def main():
    choice = 0
    while choice == 0:
        print("Main Menu")
        print("1. Given the Port Number, Identify the Protocol")
        print("2. Given the Port Protocol, Identify the Port Number")
        print("3. Exit\n")
        portNumArray = [20, 21, 22, 23, 25, 53, 67, 68, 80,
                         110, 137, 139, 143, 161, 162, 389, 443, 445, 3389]
        portNameArray = ['FTP', 'FTP', 'SSH', 'Telnet', 'SMTP', 'DNS', 'DHCP', 'DHCP', 'HTTP',
                          'POP3', 'netBIOS', 'netBIOS', 'IMAP', 'SNMP', 'SNMP', 'LDAP', 'HTTPS', 'SMB', 'RDP']
        # Calling get input Function
        getinput()
        


def getinput():
    choice = (input("Choice: "))
    if choice == '1':
        print("Identify Port Number:\n")
        randport = random.randrange(1,19)
        numToName(randport) ## Calling numtoName
    elif choice == '2':
        print("Identify Port Protocol:\n")
        randName = random.randrange(1,19)
    elif choice == '3':
        print("Hopefully this program helped in studying !!")
    else:
        print("Try one more time with one of the numbers mane  \n")
    return choice
    

main()