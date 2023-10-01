'''message = input("Type something in: ")
translated = '' #cipher text is stored in this variable
i = len(message) - 1

while i >= 0:
   translated = translated + message[i]
   i = i - 1
print(f"The ciper text is:"+translated)
'''

def encrypt_text(plaintext,n):
    ans = ""
    # iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]
        
        # check if space is there then simply add space
        if ch==" ":
            ans+=" "
        # check if a character is uppercase then encrypt it accordingly 
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
    
    return ans

plaintext = input("Enter the Text to Encrypt: ")
n = 1
print(encrypt_text(plaintext,n))