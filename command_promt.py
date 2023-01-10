import subprocess

def run_win_cmd(cmd):
    result = []
    process = subprocess.Popen(cmd,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    for line in process.stdout:
        result.append(line)
    errcode = process.returncode
    for line in result:
        print(line)
    if errcode is not None:
        raise Exception('cmd %s failed, see above for details', cmd)
cmd="main.py"
run_win_cmd("git init")
print("\n")
run_win_cmd("git add --all")
print("\n")
run_win_cmd("git status")
print("next step")
run_win_cmd('git commit -m "added a new file"')
run_win_cmd("git remote add origin https://github.com/subhash-regati/jenkins_first_trail.git")
run_win_cmd("git remote -v")
print("run the command")
run_win_cmd("git status")
print("\n")