# class SocialMedia:

#     def __init__(self, name, profilePicture, background, friends):
#         self.name = name
#         self.profilePicture = profilePicture
#         self.background = background
#         self.friends = friends

#     def changePicture(self, picture):
#         self.profilePicture = picture
#         if picture.endswith(".jpg"):
#             print("1")
#         elif picture.endswith(".png"):
#             print("2")
#         else:
#             print("3")

#     def changeBackground(self, background):
#         self.background = background
#         print("Background change.")
#     def printInformation(self):
#         print(self.name + " " + self.profilePicture + " " + self.background)

# # Code to execute
# person1 = SocialMedia("Violet", "Image02.png", "CEO", ["Jeff", "Amanda", "Blanca", "Shane"])

# person2 = SocialMedia("Chad", "image1.jpg", "Student", ["Ryan", "Allison", "Blanca", "Omar"])
# person2.printInformation()
# person1.printInformation()
# person1.changeBackground("Front-End Developer")
# person1.printInformation()
# person2.changePicture("Classroom.png")
# person2.printInformation()

# class BuildingLocation:

#      def __init__(self, building, room, name):
#             self.building = building
#             self.room = room
#             self.name = name

# BuildingLocation("Science", "Room 1", "Mr. Smith")

# file="ITE.txt"
# readyToEnd=False
# while (not readyToEnd):
#     firstNum=input("First number:  ")
#     if (firstNum=="q"):
#         readyToEnd=True
#     if (not readyToEnd):
#         secondNum=input("Second number:  ")
#     if (secondNum=="q"):
#         readyToEnd=True
#     if (not readyToEnd):
#         try:
#             with open(file) as filename:
#                 results=filename.readlines()
#             #print(results)
#             answer=int(firstNum)/int(secondNum)
#         except ZeroDivisionError:
#             print("Error dividing by 0")
#         except FileNotFoundError:
#             print("Couldn't find file")
#         else:
#             print("Success")

# fridge={"butter":0.5, "milk":1, "bread":21, "eggs":6}
# print(fridge["butter"])
# fridge["eggs"]=3
# fridge["pancake mix"]=2
# print(fridge["pancake"])

# words = {"apple": "a fruit", "dog": "a pet", "car": "a vehicle"}
# print(words.get("linear search", "Term does not exist."))
# words.pop("apple")
# print(words)
# words["dog"] = "a fruit"
# print(words["car"])
# print(words)
# words.pop("dog")
# print(words)
