from user.models import User
from chats.user_factory import RandomUserFactory


def createUsers():
    user1 = RandomUserFactory.create()
    users = RandomUserFactory.create_batch(10)

def main():
    createUsers()

if __name__ == "__main__":
    main()