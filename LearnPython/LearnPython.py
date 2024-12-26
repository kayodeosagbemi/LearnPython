# This is my first program. I have decided to learn Python and then use it for any programming interviews for big tech
# and also use it to pass MSc in Financial Engineering. Perhaps I will pivot to building all my side projects in Python. Lol

# name = input("What is your name ")
# print("Hello world ", name)
# length = 4
# namelen=len(name)
# if namelen < length:
#     print("the lenght of your name is ", namelen, " is shorter than 4")
# else:
#     print("The length of your name is just fine and it is ", namelen)

# fd=open('C:\\Users\\HP\\Documents\\PERSONAL\\personal\\CV\\Base CV - Revamped With New Knowledge\\Banking-Ready CVs\\C# Focus\\Kayode_Osagbemi_NET and Angular.pdf',"r")

# fd.close()

x = type(float(3))
print(x)
print ("Elements of a List of fruits are shown below ")
x, y, z = "Orange", "Banana", "Cherry"
print(x, y, z)
print("Now we want to start learning some operations on lists")
thisList=["Amala","Eba", "Agbado", "Cassava", "Potatoes", "Rice", "Cabbages", "Carrot"]
lengthval = len(thisList)
print(f"There are {lengthval} foods in the list")
print(thisList)
print("These are the foods from the 3rd food to the last one", thisList[2:])
# Lets check whether beans exist in the list
if "beans" in thisList:
    print("Beans dey this list o")
else:
    thisList.append("Beans") 
    print("Beans no dey this list")
    print ("After adding Beans to the list, this is the list now: ",  thisList)

tutorial_segment_title = "Now Testing Negative Indices"
print(tutorial_segment_title)
print ("*" * len("Now Testing Negative Indices"))
print ("The last 3 elements of theList are ", thisList[-3:])
print ("Changing the last 3 elements to Sharwama, burger, akara")
thisList[-3:] = ["Sharwama", "burger", "akara"]
print("This is the list after changing", thisList)

tutorial_segment_title=""
