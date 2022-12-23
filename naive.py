import os
from datetime import date

os.system('git pull')

# get current time
f = open("dependencies/lineage.txt", "a")
f.write(date.today().strftime("%Y-%m-%d %H:%M:%S"))
f.write("\nNow the file has more content!")
f.close()

os.system('git add .')

os.system('git commit -m "script" ')

os.system('git push')
