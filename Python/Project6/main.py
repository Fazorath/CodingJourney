## Yoenis Hernandez
## COP 2002 0.M2
## Oct 28, 2023
## Using CSV project 6

def readroster(file):
   with open(file, "r") as f:
       rostercodes = []
       for line in f:
           columns = line.split(",")
           code = columns[5].strip()
           print(f"*{code}*")
       return rostercodes  


def readmaster(file):
    with open(file, "r") as f:
         for line in f:
             splitline = line.split(",")
             return splitline



def coderoster(file):
    for line in file:
        splitline = line.split(",")
        splitline = splitline[5].strip()
        return splitline

        

def main():
    print("Processing Student input Files")
    path1 = "Python\\Project6\\Program Codes.csv"
    path2 = "Python\\Project6\\student roster example.csv"
    studentcodes = readroster(path2)
    mastercodes = readmaster(path1)
    for line in studentcodes:
        if line in mastercodes:
            print(f"Student Code {line} is valid")
    

    
    # format program codes
    # Print Program names
    # Write to file
    # End message
    print("Program Completed!")

if __name__ == "__main__":
    main()
