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
## Create Json String
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
                file_read = [line.strip() for line in f.readlines()] ## Read and create list
      
        except:
            print(f"{self.filename} not found")
       
        else:
            self.read_filename = file_read
            # print(file_read)
  
    def assign_header(self):
        self.header = self.read_filename[0].strip().split(",")  

    def pair_header_values(self):
        for line in self.read_filename[1:]:
            lines = line.split(",")
            # print(lines[3])
            row = {}
            for i in range(len(self.header)):
                row[self.header[i]] = lines[i]
            self.data.append(row)
        # print(self.data)
            
    def create_json_string(self):
        counter = 1
        json_str = "{"
        for item in self.data:
            json_str += f'"{counter}":{{'
            for i in range(len(self.header)):
                key = self.header[i]
                value = item[key]
                if i == 2 and 3:
                    # Convert to lowercase for the fourth column
                    json_str += f'"{key}":{value.lower()}'
                else:
                    json_str += f'"{key}":"{value}"'
                if i < len(self.header) - 1:
                    json_str += ","
            json_str += "}"
            if counter < len(self.data):
                json_str += ","
            counter += 1
        json_str += "}"
        return json_str

    
        
    def returnJsonString(self):
        print(self.create_json_string())
    
        
   
       



if __name__ == "__main__":
    ## Creates instance of class
    project7 = CSVtoJSON()
    
    ## Reads the Txt File
    project7.read_txt_file()
    # print(project7.read_filename)
   
    ## Assigns the header of the txt file
    project7.assign_header()
    # print(project7.header)

    project7.pair_header_values()
    # print(project7.data)

    project7.create_json_string()
    # print(project7.create_json_string())

    project7.returnJsonString()

