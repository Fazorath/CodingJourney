## Yoenis Hernandez
## 12/31/2018
## The goal for this program is to take a txt file and create JSON strings that can be used in JavaScript 
## for each row of data that is not the header row.  JavaScript is a scripting language used for web pages.  
## JSON is a common format used to transmit data for web apps from a web server to a client 
## (i.e. such as from sfcollege.edu's web server to your computer) so it can be displayed in a browser.
## Create a class and FN
## Read a txt
## Keep CSV header
## Pair header with the values
## Ceate Json String
## Return JSON string to Screen
## return JSON string to file

class CSVtoJSON:
    def __init__(self):
        ## Source File Path
        self.filename = input("Enter the CSV file Name: ")
        ## Output File Path
        self.output_fileName = input("Enter the JSON file Name: ")
        ## Holds the Header row of the csv file
        self.header = []
        ## Holds the value of the source data
        self.read_filename = []
        ## Holds the JSON string
        self.data = []


    def read_txt_file(self):
      
        try: ## Exception handling
            with open(self.filename, "r") as f:
                file_read = f.readlines() ## Read and create list
      
        except:
            print(f"{self.filename} not found")
       
        else:
            self.read_filename = file_read
            # print(file_read)
  

    def assign_header(self):
        self.header = self.read_filename[0].strip().split(",")  


    def pair_header(self):
        for line in self.read_filename[1:]:
            lines = line.split(",")
            # print(lines)
            row = {}
            
            for i in range(len(self.header)):
                row[self.header[i]] = lines[i]
            print(row)
            

        
   
       



if __name__ == "__main__":
    ## Creates instance of class
    project7 = CSVtoJSON()
    
    ## Reads the Txt File
    project7.read_txt_file()
    # print(project7.read_filename)
   
    ## Assigns the header of the txt file
    project7.assign_header()
    # print(project7.header)
    
    project7.pair_header()
    # print(project7.data)

