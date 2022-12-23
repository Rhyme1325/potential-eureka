import os

os.system('git pull')

# get current time
f = open("dependencies/lineage.txt", "a")
f.write("Now the file has more content!\n")
f.close()

os.system('git add .')

os.system('git commit -m "script" ')

os.system('git push')
