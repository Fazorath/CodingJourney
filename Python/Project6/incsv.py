def incsv(master,roster,classes):   # if roster codes are in the master code files
    for item in roster:
        if item in master:
            correctclass = (classes[master.index(item)])
            print(correctclass)
    return correctclass
