import git
import os

def get_repo_tags(repository_path: str):
    repo = git.Repo(repository_path)
    tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime)
    return tags

def checkout_repo_tags(repository_path: str, tag_name: str):
    repo = git.Git(repository_path)
    repo.checkout(tag_name)
    # checkout with dvc
    os.system('dvc checkout')

def push_repo_tags(repository_path: str, tag_name: str):
    os.system('dvc add data')
    os.system('dvc push')

    repo = git.Repo(repository_path)
    repo.git.add(all=True)
    repo.git.commit('-m', 'Automatic tags {tag_name}', author='ruhyadi.dr@gmail.com')
    repo.create_tag(tag_name, message=f'Automatic tags {tag_name}')
    repo.remotes.origin.push(tag_name)

if __name__ == '__main__':
    url = '.'
    tags = get_repo_tags(url)

    print(tags)