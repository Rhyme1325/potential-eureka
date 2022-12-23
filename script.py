from git import Repo

import  git 


# get current time
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()


# Git Fetch
repo = git.Repo('name_of_repo')
repo.remote().fetch()

# Git Commit
repo.git.commit('-m', 'commit message from python script', author='test_user@test.com')

# Git push
repo.git.commit('-m', 'commit message from python script', author='test_user@test.com')
origin = repo.remote(name='origin')
origin.push()

