EXTENSIONS = {
    "DAABBCC": "selimanac/DAABBCC",
    "DEFOS": "subsoap/defos",
    "STEAMWORKS": "britzl/steamworks-defold"
}

import json
import os
from dataclasses import dataclass
from github import Auth, Github

@dataclass
class ExtensionVersion:
    date: str
    url: str

@dataclass
class Extension:
    symbol: str
    repo: str
    versions: list[ExtensionVersion]

def fetch_extension(g: Github, repo_name: str, symbol: str) -> Extension:
    print(f"Fetching {repo_name}...")
    repo = g.get_repo(repo_name)
    tags = repo.get_tags()
    versions = [ExtensionVersion(tag.commit.commit.committer.date.isoformat(), tag.zipball_url) for tag in tags]
    return Extension(symbol, repo_name, versions)

def fetch_extensions(g: Github, extensions: dict[str, str]) -> list[Extension]:
    return [fetch_extension(g, repo, symbol) for symbol, repo in extensions.items()]

def main():
    token = os.environ.get("GITHUB_TOKEN")
    if token is not None:
        g = Github(auth=Auth.Token(token))
    else:
        g = Github()
    
    versions = fetch_extensions(g, EXTENSIONS)

    with open("extension_versions.json", "w") as file:
        file.write(json.dumps(versions, default=vars, indent=4))

if __name__ == "__main__":
    main()