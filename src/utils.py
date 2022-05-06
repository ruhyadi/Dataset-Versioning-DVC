import git

def get_repo_tags(repository_path: str):
    repo = git.Repo(repository_path)
    tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime)

    return tags

def checkout_repo_tags(repository_path: str, tag_name: str):
    repo = git.Repo(repository_path)
    repo.checkout(tag_name)

if __name__ == '__main__':
    url = '.'
    tags = get_repo_tags(url)

    print(tags)