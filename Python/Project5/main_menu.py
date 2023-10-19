

# Main Menu Function


def main():
    def getinput():
        choice = 0
        while choice == 0:
            print("1. Given the Port Number, Identify the Protocol")
            print("2. Given the Port Protocol, Identify the Port Number")
            print("3. Exit\n")
            portNumArray = [20, 21, 22, 23, 25, 53, 67, 68, 80,
                            110, 137, 139, 143, 161, 162, 389, 443, 445, 3389]
            portNameArray = ['FTP', 'FTP', 'SSH', 'Telnet', 'SMTP', 'DNS', 'DHCP', 'DHCP', 'HTTP',
                             'POP3', 'netBIOS', 'netBIOS', 'IMAP', 'SNMP', 'SNMP', 'LDAP', 'HTTPS', 'SMB', 'RDP']

            choice = (input("Choice: "))

            if choice == '1':
                print("\nIdentify Port Number:\n")
                ## Call num to name function 
            elif choice == '2':
                print("\nIdentify Port Protocol:\n")
            elif choice == '3':
                print("\nHopefully this program helped in studying !!")
            elif choice == 'm':
                getinput() ## Loops if user presses M as their Choice
            else:
                break
   
    getinput()


main()
