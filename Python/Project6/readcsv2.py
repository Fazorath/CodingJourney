def readcsv2(file):
    with open(file, "r") as f:
        codes = []
        for line in f:
            columns = line.split(",")
            code = columns[1].strip()
            codes.append(code)
        return codes
