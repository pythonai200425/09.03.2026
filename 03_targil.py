
import os

def arrange(path, entries):
    # arrange folder first and ignot folder starts with .
    entry_list = []
    for entry in entries:
        if os.path.isdir(os.path.join(path, entry)):
            if entry[0] != '.':
                entry_list.append(entry)
        else:
            entry_list.insert(0, entry)

    return entry_list

def list_and_size(path, filename):
    # should return true if the file exist in the folder or subfolder , false if not
    entries = os.listdir(path)
    entry_list = arrange(path, entries)

    for entry in entry_list:
        if os.path.isdir(os.path.join(path, entry)):
            full_path = os.path.join(path, entry)
            list_and_size(full_path)  # recursive call !


# change to folder on your computer!!
list_and_size(r"D:\python_projects\AIDec\09_03_2026", 'main.py')


