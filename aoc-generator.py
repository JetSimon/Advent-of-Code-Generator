import os

templateFile = open('template.py')
template = [line for line in templateFile]
templateFile.close()

sub = input("Enter subfolder name (or leave blank to use current directory): ")
if sub != "":
    if os.path.exists(sub):
        print("Folder already exists")
        exit()
    os.mkdir(sub)
    os.chdir(sub)

for day in range(25):
    d = str(day+1)
    folderName = "day " + d
    os.mkdir(folderName)
    path = os.path.join(folderName, "day" + d + ".py")
    f = open(path, 'w')
    for line in template:
        f.write(line)
    f.close()
    path = os.path.join(folderName, "input.txt")
    f = open(path, 'x')
    f.close()

print("Done generation! Merry coding! 🎅🎅🎅")