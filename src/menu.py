"""
This is a re-write of the project on branch bacon et. al.
bacon is NOT to be merged with main or any other branch
DO NOT MERGE
"""
from sys import exit


def print_menu():
    menu_string: str = (''''\n\n\tEnter the action you would like to commit.
\t1) Get games won by White.
\t2) Get games won by Black.
\t3) Get games won by Checkmate by White.
\t4) Get games won by Checkmate by Black.
\t5) Exit
''')
    print(menu_string)


def get_user_choice():
    return int(input('\tEnter your choice: '))


def check_choice(choice: int):
    if isinstance(choice, int):
        if choice == 5:
            exit()


if __name__ == '__main__':
    pass

# DO NOT MERGE
