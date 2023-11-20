## Yoenis Hernandez
## 12/31/2018
## The goal for this program is to take a CSV file and create JSON strings that can be used in JavaScript 
## for each row of data that is not the header row.  JavaScript is a scripting language used for web pages.  
## JSON is a common format used to transmit data for web apps from a web server to a client 
## (i.e. such as from sfcollege.edu's web server to your computer) so it can be displayed in a browser.
def opencsv():
    filename=input("Enter the file Name: ")
    with open(filename, 'r') as file:
        for line in file:
            content = file.readlines()
            print("\n")
            print(content[0])
            print(content[1])
            print(content[2])

def main():
    opencsv()

if __name__ == "__main__":
    main()


# 1. Open csv file
# 2. Read csv file 
# 3. Create JSON strings
# 4. Write JSON strings to a file

