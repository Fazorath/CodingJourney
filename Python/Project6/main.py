## Yoenis Hernandez
## COP 2002 0.M2
## Oct 28, 2023
## Using CSV project 6

from readroster import *
from readcsv import *
from readcsv2 import *
from readitems import *
from writecsv import *
from incsv import *


def main():
  
    print("Processing Student input Files...")
    path1 = "Python\\Project6\\student roster example.csv"
    path2 = "Python\\Project6\\Program Codes.csv"
    path3 = "Python\\Project6\\output.csv"
    classroster = readroster(path1)
    # print(classroster)
    mastercodes = readcsv(path2)
    classname = readcsv2(path2)
    readitems(classroster)
    print("\n\n")
    correctclasses = incsv(mastercodes, classroster, classname)
    

            
        
        
            
    

    print("Program Completed!")

if __name__ == "__main__":
    main()
