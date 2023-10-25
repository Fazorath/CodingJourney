## Lecture 10/24/23
## discussing the past Project but i aced that shit so ??

## Exception Handling
path = "CodingJournPython\\Studying\\Lectures\\10-24-23\\example.txt"
try: # code that you expect to fail or have some error
    with open(path) as f:
        content = f.readlines()
except: # What to do when the code fails
    print(f"The file you are looking for: {path}\nDoes Not Exist!")
else: # If the code Succeeds to the following
    index = 0
    for line in content:
        line = line.rstrip()
        print(f"{index}: {line}")
        index = index + 1
