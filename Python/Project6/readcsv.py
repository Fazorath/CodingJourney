def readcsv(file):
    with open(file, "r") as f:
        codes = []
        for line in f:
            columns = line.split(",")
            code = columns[0].strip()
            codes.append(code)
        return codes
