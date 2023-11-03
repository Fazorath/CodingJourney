def readroster(file):
   with open(file, "r") as f:
       rostercodes = []
       for line in f:
           columns = line.split(",")
           code = columns[5].strip()
           rostercodes.append(code)
       rostercodes.pop(0)
       return rostercodes 
