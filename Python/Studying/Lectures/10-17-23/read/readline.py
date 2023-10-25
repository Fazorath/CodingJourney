path = 'CodingJourney\\Python\\Studying\\Lectures\\10-17-23\\read\\list.txt'

with open(path) as f: #With Open
    content = f.readlines()
    print(f"{content}\n\n\n")
    print("Using the for line loop and .rstrip()\nWill make the dictionary into line by line str")
    for line in content:
        line = line.rstrip()
        print(line)
    print(type(line))
