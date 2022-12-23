import os
from datetime import date
import random

os.system('git pull')

stack = [1, 7, 14, 28, 56]
chosen = random.randint(0,4)

for i in range(stack[chosen]):
    time = "\n" + date.today().strftime("%Y-%m-%d %H:%M:%S")
    # get current time
    f = open("dependencies/lineage.txt", "a")
    f.write(time)
    f.close()

    os.system('git add .')

    os.system('git commit -m "script" ')

    os.system('git push')
