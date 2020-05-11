import sys
import os
from github import Github

dir_path = os.path.dirname(os.path.realpath(__file__))

username = "craiglobo1" #Insert your github username here
password = "Craig123$" #Insert your github password here

repoName = dir_path.split('\\')[-1]

print(repoName)

def create():
    md = open(dir_path + r'\README.md','w')
    md.close()
    user = Github(username, password).get_user()
    repo = user.create_repo(repoName)
    print(f"Succesfully created repository {repoName}")

if __name__ == "__main__":
    create()
