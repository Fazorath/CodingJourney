def incsv(master,roster,classes):   # if roster codes are in the master code files
    print("Writing to file...")
    correctclasses = []
    for item in roster:
        if item in master:
            correctclass = (f'\t{classes[master.index(item)]}')
            correctclasses.append(correctclass)
    return correctclasses
