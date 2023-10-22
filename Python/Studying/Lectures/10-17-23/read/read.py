#  reading inside a file
file=''
with open("/Users/exempt/Repo Codespace/CodingJourney/Python/Studying/Lectures/10-17-23/read/list.txt") as read_file:
  file = read_file.readlines()
  file2 = read_file.read()
for item in file:
  print(item)

for item in file2:
  print(item)










