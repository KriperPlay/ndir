
'''
╭━╮╱╭┳━━━┳━━┳━━━╮
┃┃╰╮┃┣╮╭╮┣┫┣┫╭━╮┃
┃╭╮╰╯┃┃┃┃┃┃┃┃╰━╯┃
┃┃╰╮┃┃┃┃┃┃┃┃┃╭╮╭╯
┃┃╱┃┃┣╯╰╯┣┫┣┫┃┃╰╮
╰╯╱╰━┻━━━┻━━┻╯╰━╯
'''

import os
import sys
from datetime import datetime


def set_size(size: int) -> int:
    for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

def dir(path: str, secret_dir: str) -> None:
    files = os.listdir(path)
    
    if secret_dir == "-sdir":
        for file in files:
            print(file)
    if secret_dir == "-nsd":
        for file in files:
            if file[0] == '.':
                pass
            else:
                print(file)

def full_dir(path: str, secret_dir: str) -> None:
    try:
        dirr = os.listdir(path)
        files = []

        if secret_dir == "-sdir":
            for file in dirr:
                if os.path.isfile(path+file):
                    stat = os.stat(path+file)
                    ctime = stat.st_ctime
                    time = datetime.fromtimestamp(ctime)
                    full_name = f"{set_size(os.path.getsize(path+file))}  {str(time)[0:str(time).find('.')]}  {file}"
                    files.append(full_name)
                if not os.path.isfile(path+file) and os.path.exists(path+file):
                    stat = os.stat(path+file)
                    ctime = stat.st_atime
                    time = datetime.fromtimestamp(ctime)
                    size = sum(os.path.getsize(os.path.join(dp, f)) for dp, dn, fn in os.walk(path+file) for f in fn if os.path.isfile(os.path.join(dp, f)))
                    full_name = f"{set_size(size)}  {str(time)[0:str(time).find('.')]}  {file}"
                    files.append(full_name) 
        if secret_dir == "-nsd":
            for file in dirr:
                if file[0] == '.':
                    pass
                else:
                    if os.path.isfile(path+file):
                        stat = os.stat(path+file)
                        ctime = stat.st_ctime
                        time = datetime.fromtimestamp(ctime)
                        full_name = f"{set_size(os.path.getsize(path+file))}  {str(time)[0:str(time).find('.')]}  {file}"
                        files.append(full_name)
                    if not os.path.isfile(path+file) and os.path.exists(path+file):
                        stat = os.stat(path+file)
                        ctime = stat.st_atime
                        time = datetime.fromtimestamp(ctime)
                        size = sum(os.path.getsize(os.path.join(dp, f)) for dp, dn, fn in os.walk(path+file) for f in fn if os.path.isfile(os.path.join(dp, f)))
                        full_name = f"{set_size(size)}  {str(time)[0:str(time).find('.')]}  {file}"
                        files.append(full_name)          
    except FileNotFoundError:
        pass

    for file1 in files:
        print(file1)

def tree(path: str, secret_dir: str) -> None:
    if secret_dir == "-sdir":
        tree = list(os.walk(path))

        for i in tree:
            print(i[0])
            print()
            for a in i[1:]:
                for x in a:
                    if os.path.exists(i[0]) and not os.path.isfile(i[0]+'/'+x):
                        print(f"    {x}/")
                    else:
                        print(f"    {x}")
            print()
    if secret_dir == "-nsd":
        tree = list(os.walk(sys.argv[1]))

        for i in tree:
            print(i[0])
            print()
            for a in i[1:]:
                for x in a:
                    if x[0] == '.':
                        pass
                    else:
                        if os.path.exists(i[0]) and not os.path.isfile(i[0]+'/'+x):
                            print(f"    {x}/")
                        else:
                            print(f"    {x}")
            print()


if __name__ == "__main__":
    try:
        if sys.argv[3] == "-dir":
            dir(sys.argv[1], sys.argv[2])
        if sys.argv[3] == "-fdir":
            full_dir(sys.argv[1], sys.argv[2])
        if sys.argv[3] == "-tree":
            tree(sys.argv[1], sys.argv[2])
    except IndexError:
        print("Argmunets:\n[path] [-sdir] [-mode]")
        print("[path] - path\n[-sdir] - on(-sdir)/off(-nsd) secret dir\n[-mode]\n",
              "-dir - just files and dirs\n -fdir - datecreate and size of dirs/files\n",
              "-tree - tree of directories")