from git import Repo

import  git 


# get current time
f = open("lineage.txt", "a")
f.write("Now the file has more content!")
f.close()

# Git Fetch
repo = git.Repo('')
repo.remote().fetch()

# Git Commit
repo.git.commit('-m', 'commit message from python script', author='rhyme1325@gmail.com')

# Git push
repo.git.commit('-m', 'commit message from python script', author='rhyme1325@gmail.com')
origin = repo.remote(name='origin')
origin.push()
