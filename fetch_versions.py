import json
import os
from dataclasses import dataclass
from datetime import datetime
from github import Auth, Github
from typing import Optional

@dataclass
class Version:
    name: str
    sha: str
    date: str

def fetch_versions(g: Github) -> list[Version]:
    repo = g.get_repo("defold/defold")
    tags = repo.get_tags()

    i = 0
    versions = []
    for tag in tags:
        versions.append(Version(tag.name, tag.commit.sha, tag.commit.commit.committer.date.isoformat()))
        print(tag.name, tag.commit.commit.committer.date)
        i +=1 
        if i > 5:
            pass
    return versions

def main():
    token = os.environ["GITHUB_TOKEN"]
    if token is not None:
        g = Github(auth=Auth.Token(token))
    else:
        g = Github()
        
    versions = fetch_versions(g)

    with open("versions.json", "w") as file:
        file.write(json.dumps(versions, default=vars, indent=4))

if __name__ == "__main__":
    main()