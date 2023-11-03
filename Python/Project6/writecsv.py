def writecsv(file,items):
    with open(file, "w") as f:
        for item in items:
            f.write(f"{item}\n")
