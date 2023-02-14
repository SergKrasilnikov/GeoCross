import os
import matplotlib.pyplot as plt
import numpy as np
from dbfread import DBF
import os.path

# get profile file
def search_profile():
    dbf_list = []
    for root, dirs, files in os.walk(os.path.abspath('../geological_crossections/data/elevation/')):
        for file in files:
            if file.endswith(".dbf"):
                dbf_list.append(file)
        return get_profile_data(dbf_list, root)

def get_profile_data(files_list, root):
    x_list = []
    perm_list = []
    temp_list = []
    for file in files_list:
        row = 0
        # perm_list.append(temp_list)
        for _ in DBF(f'{root}\{file}'):
            table = DBF(f'{root}\{file}', load=True)
            temp_list.append(table.records[0 + row]['z'])
            if row == 0:
                x_list.append(0)
            row += 1
            x_list.append(row * 100)
        x_list.pop()
    print(temp_list)
    print(x_list)
    return temp_list, x_list