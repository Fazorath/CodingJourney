## Writing to a file using the 'w' mode
path = "CodingJourney/Python/Studying/Reading/Texts/empty.txt"
with open(path,'w') as file:
  file.write("Print first time writing into a file")