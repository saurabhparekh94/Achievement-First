import github
import sys


def find_public_repo(username):
    """
    For a given username the function returns the list of public repositories.
    :param username: The username whose
    :return:None
    """
    gh = github.Github()
    user = gh.get_user(username)
    for item in user.get_repos():
        print(item.name)


if __name__ == '__main__':

    find_public_repo(username = sys.argv[1])
    