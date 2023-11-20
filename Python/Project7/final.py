## Yoenis Hernandez
## 12/31/2018
## The goal for this program is to take a CSV file and create JSON strings that can be used in JavaScript 
## for each row of data that is not the header row.  JavaScript is a scripting language used for web pages.  
## JSON is a common format used to transmit data for web apps from a web server to a client 
## (i.e. such as from sfcollege.edu's web server to your computer) so it can be displayed in a browser.
## Create a class and FN
## Read a CSV
## Keep CSV header
## Paid header with the values
## Ceate Json String
## Return JSON string to Screen
## return JSON string to file

class CSVtoJSON:
    def __init__(self):
        ## Source File Path
        self.inputFile = input("Enter the CSV file Name: ")
        ## Output File Path
        self.outputFile = input("Enter the JSON file Name: ")
        ## Holds the Header row of the csv file
        self.header = []

if __name__ == "__main__":
    project7 = CSVtoJSON()
    

