import os


def check_user(user_id):
    path = f'prices/{str(user_id)}/{str(user_id)}'
    if os.path.exists(path):
        return "exists"
    else:
        return "doesn't exists"


def create_user_files(user_id):
    user_id = str(user_id)
    os.makedirs(f'prices/{user_id}')
    file = open(f'prices/{user_id}/{user_id}', 'w')
    file.close()

def get_list_of_items(user_id):
    """Just get a list of URLs of the items """
    file = open(f'prices/{user_id}/{user_id}', 'r', encoding='UTF-8')
    items = file.read().split(',')
    file.close()
    return items
