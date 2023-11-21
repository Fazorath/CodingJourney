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
                file_read = []
                for line in f.readlines():
                    file_read.append(line.strip())
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
        json = "{"
        for item in self.data:
            json += f'"{counter}":{{'
            for i in range(len(self.header)):
                key = self.header[i]
                value = item[key]
                if i == 2:
                    json += f'"{key}":{value}'
                elif i == 3:
                    # Convert to lowercase for the fourth column
                    json += f'"{key}":{value.lower()}'
                else:
                    json += f'"{key}":"{value}"'
                if i < len(self.header) - 1:
                    json += ","
            json += "}"
            if counter < len(self.data):
                json += ","
            counter += 1
        json += "}"
        return json
        
    def returnJsonString(self):
        print(self.create_json_string())
    
    def write_json_file(self):
        try:
            with open(self.output_fileName, "w") as f:
              f.write(self.create_json_string())
        except:
            print(f"{self.output_fileName} not found")
        else:
            print(f"Output written to {self.output_fileName}")

       



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

    project7.write_json_file()

