import os
from dbfread import DBF
import os.path

# get profile file
def search_profile(datadir):
    dbf_list = []
    for root, dirs, files in os.walk(os.path.join(datadir, 'elevation')):
        for file in files:
            if file.endswith(".dbf"):
                dbf_list.append(file)
        return get_profile_data(dbf_list, root)

def get_profile_data(files_list, root):
    x_list = []
    temp_list = []
    for file in files_list:
        row = 0
        for _ in DBF(os.path.join(root, file)):
            table = DBF(os.path.join(root, file), load=True)
            temp_list.append(table.records[0 + row]['z']) # if the problem with reading of the elevation data (z)
            if row == 0:
                x_list.append(0)
            row += 1
            x_list.append(row * 1000) # change the number here if the distance between points is vary from 100 meters
        x_list.pop()
    return temp_list, x_list