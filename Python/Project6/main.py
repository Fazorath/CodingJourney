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
           rostercodes.append(code)
       return rostercodes 

def readitems(list): 
    list.pop(0)
    for item in list:
        print(f"*{item}*")

def main():
  
    print("Processing Student input Files...\n")
    path1 = "Python\\Project6\\student roster example.csv"
    path2 = "Python\\Project6\\Program Codes.csv"
    classroster = readroster(path1)
    readitems(classroster)
   
    

    print("Program Completed!")

if __name__ == "__main__":
    main()
