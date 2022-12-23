from git import Repo

# To initiate new Git repo in the mentioned directory
repository = Repo.init(repo_path)

import  git 

# Git Clone
git.Git(repo_path).clone("https://github.com/digitalvarys/test.git")

# Git Checkout
repo.git.checkout('branchename')
repo.git.checkout('-b', 'branchename')

# Git Fetch
repo = git.Repo('name_of_repo')
repo.remote().fetch()

# Git Add
repo.git.add('--all')  # to add all the working files.
repo.git.add('index.html','style.css')  
# to add specific working file(s).

# Git Commit
repo.git.add('--all')  
repo.git.commit('-m', 'commit message from python script', author='test_user@test.com')

# Git push
repo.git.add('--all')
repo.git.commit('-m', 'commit message from python script', author='test_user@test.com')
origin = repo.remote(name='origin')
origin.push()

# Git Pull
repo = git.Repo('name_of_repo')
origin = repo.remote(name='origin')
origin.pull()

# Git Merge
repo = git.Repo('.')
master = repo.branches['master']
current = repo.branches['feature']
root = repo.merge_base(current, master)
repo.index.merge_tree(master, base=root)
repo.index.commit('merging master into current branch', parent_commits=(current.commit, master.commit))

# Git Reset
repo = git.Repo('.')
repo.git.reset('--hard')
