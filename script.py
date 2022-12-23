import os
from datetime import date
import random

os.system('git pull')

stack = [1, 7, 14, 28, 56]
chosen = stack[random.randint(0,4)]
commit = str(random.randint(0,999))

for i in range(chosen):
    time = "\n" + date.today().strftime("%Y-%m-%d %H:%M:%S")
    # get current time
    f = open("dependencies/lineage.txt", "a")
    f.write(time)
    f.close()

    os.system('git add .')
    temp = 'git commit -m "' + str(chosen) + 'x"'
    os.system(temp)

    os.system('git push')
