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
       rostercodes.pop(0)
       return rostercodes 

def readcsv(file):
    with open(file, "r") as f:
        codes = []
        for line in f:
            columns = line.split(",")
            code = columns[0].strip()
            codes.append(code)
        return codes

def readcsv2(file):
    with open(file, "r") as f:
        codes = []
        for line in f:
            columns = line.split(",")
            code = columns[1].strip()
            codes.append(code)
        return codes

def readitems(list):  # displays the Codes that are being Read from CSV file
    for item in list:
        print(f"*{item}*")

def incsv(master,roster,classes):   # if roster codes are in the master code files
    print("Writing to file...")
    correctclasses = []
    for item in roster:
        if item in master:
            correctclass = (f'\t{classes[master.index(item)]}')
            correctclasses.append(correctclass)
    return correctclasses

def writecsv(file,items):
    with open(file, "w") as f:
        for item in items:
            print(f"\t{item}")
        for item in items:
            f.write(f"{item}\n")

def main():
  
    print("Processing Student input Files...")
    # My 3 Paths
    path1 = "Python\\Project6\\student roster example.csv"
    path2 = "Python\\Project6\\Program Codes.csv"
    path3 = "Python\\Project6\\output.csv"
    classroster = readroster(path1)
    mastercodes = readcsv(path2)
    classname = readcsv2(path2)
    readitems(classroster)
    print("\n")
    correctclass = incsv(mastercodes, classroster, classname)
    writecsv(path3, correctclass)
    print("\nProgram Completed!")

if __name__ == "__main__":
    main()
