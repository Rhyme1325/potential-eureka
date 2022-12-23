import os
from datetime import date

os.system('git pull')

time = "\n" + date.today().strftime("%Y-%m-%d %H:%M:%S")
# get current time
f = open("dependencies/lineage.txt", "a")
f.write(time)
f.close()

os.system('git add .')

os.system('git commit -m "script" ')

os.system('git push')
