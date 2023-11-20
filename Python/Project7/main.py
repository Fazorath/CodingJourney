## Yoenis Hernandez
## 12/31/2018
## The goal for this program is to take a CSV file and create JSON strings that can be used in JavaScript 
## for each row of data that is not the header row.  JavaScript is a scripting language used for web pages.  
## JSON is a common format used to transmit data for web apps from a web server to a client 
## (i.e. such as from sfcollege.edu's web server to your computer) so it can be displayed in a browser.
import json

def opencsv():
    filename=input("Enter the file Name: ")
    with open(filename, 'r') as file:
        for line in file:
            content = file.readlines()
            print(content)
            print("\n\n")
        return content

def createJSON(content):
    jsonname = input("Enter the file Name: ")
    with open(jsonname, 'w') as file:
        json.dump(content, file)



def main():
    content = opencsv()
    createJSON(content)

if __name__ == "__main__":
    main()


# 1. Open csv file
# 2. Read csv file 
# 3. Create JSON strings
# 4. Write JSON strings to a file

