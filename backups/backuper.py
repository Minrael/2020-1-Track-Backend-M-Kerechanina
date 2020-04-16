import subprocess
import os
import time
import glob

user = 'messenger_app'
password = '123'
folder_name = '/home/maria/Projects/2020-1-Track-Backend-M-Kerechanina/backups/backups/'
host = '127.0.0.1'
port = '5432'
db_name = 'messenger_app'

def read_n(filename):
    with open(filename, 'r') as config:
        n = int(config.readlines()[0])
        return n

def backup(user, password, folder_name, host, port, db_name):
    time_now = str(time.strftime('%Y-%m-%d-%H.%M.%S', time.localtime()))
    file_name = folder_name + db_name + '-' + time_now + '.dump'

    os.putenv("PGPASSWORD", password)

    cmd = 'pg_dump -f {} -U {} -h {} -p {} -d {}'.format(file_name, user, host, port, db_name)

    subprocess.call(cmd, shell=True)


def main():

    n = read_n('backups/backup.config')

    list_dir = os.listdir(folder_name)
    list_dir.sort(key=lambda x: os.path.getmtime(folder_name + x))

    backup(user, password, folder_name, host, port, db_name)

    if (len(list_dir) > n - 1):
        os.remove(folder_name + list_dir[0])


if __name__ == '__main__':
    main()