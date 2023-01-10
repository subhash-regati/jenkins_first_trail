from git import Repo

full_local_path = "C:\Users\subhash.reddy\PycharmProjects\jenkins_first_trail"
username = "your-username"
password = "your-password"
remote = f"https://{'subhash-regati'}:{'PropertyRemoveThis@1997'}@github.com/subhash-regati/jenkins_first_trail.git"
Repo.clone_from(remote, full_local_path)
repo = Repo(full_local_path)
repo.git.add("C:\Users\subhash.reddy\PycharmProjects\jenkins_first_trail\hello.txt")
repo.index.commit("new text file")
repo = Repo(full_local_path)
origin = repo.remote(name="origin")
origin.push()