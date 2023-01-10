from git import Repo
editorname=input()
full_local_path = "C:\\Users\\subhash.reddy\\PycharmProjects\\trail"
username = "subhash-regati"
password = "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"
remote = f"https://{username}:{password}@github.com/subhash-regati/jenkins_first_trail.git"
repo = Repo(full_local_path)
repo.git.add('C:\\Users\\subhash.reddy\\PycharmProjects\\trail\\gitpush.py')
repo.index.commit("added new text file by " + editorname)
repo = Repo(full_local_path)
origin = repo.remote(name="origin")
origin.push()