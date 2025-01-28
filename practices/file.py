

file = open("fileExample.py" , "w")
file.write("print(\"Hello World\")\n\n\nprint(\"This is a newest line\")")
file.close()



file = open("fileExample.py" , "r")

for f in file.readlines():
    print(f)


with open("newFile.txt" , "w") as file:
    file.write("Hello there, This was created by file.py\n")
    file.write("Second Line of this")



with open("newFile.txt" , "r") as file:
    for f in file:
        print(f)


from pathlib import Path

path = Path()
for f in path.glob("*"):
    print(f)
