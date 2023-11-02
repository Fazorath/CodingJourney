## Yoenis Hernandez
## COP 2002 0.M2
## Oct 28, 2023
## Using CSV project 6

def mastercode(file):
    try:
        with open(file,"r") as f:
            content = f.readlines()
    except:
        print(f"{f} File not found")
    else:
        return content
        


def main():
    # print intro message
    print("Processing Student input Files")
    # read csv
    path = "Python\Project6\Program Codes.csv"
    file = mastercode(path)
    print(len(file))
    # get program code
    # format program codes
    # Print Program names
    # Write to file
    # End message
    print("Program Completed!")

if __name__ == "__main__":
    main()
