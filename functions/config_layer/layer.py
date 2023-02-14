import os
from dbfread import DBF
import os.path
# import formula
# from formula import formula_determination
# from formula import sharpton
# from formula import housen
# from formula import faset


def get_layer(dir_number, elevation_profile):
    final_elevations = []
    #qqq = len(next(os.walk('other/work_tasks/geological_crossections/data/layers'))[1])
    #print(qqq)
    #print(len(next(os.walk('other/work_tasks/geological_crossections/data/layers'))[1]))
    for folder in range(dir_number):
        # print(elevation_profile)
        final_elevations.append((search_layers(folder, elevation_profile)).copy())
        # print(final_elevations[folder])
    return final_elevations

# название папки
def search_layers(dir_name, elevation_profile):
    dbf_list = []
    for root, dirs, files in os.walk(os.path.abspath(f'../geological_crossections/data/layers/{dir_name}')):
        for file in files:
            if file.endswith(".dbf"):
                dbf_list.append(file)
    return get_layers_data(root, dbf_list, elevation_profile)

# извлечь данные из файла
def get_layers_data(root, files_list, elevation_profile):
    # layer_elevation = []
    for file in files_list:
        diameter = get_diameter(root, file)
        layer_thickness = get_thickness(root, file, diameter) # список с мощностью из файла
        for index in range(len(elevation_profile)):
            elevation_profile[index] -= layer_thickness[index]
    return elevation_profile

    # for each_elevation_point, each_profile_point in layer_thickness, elevation_profile:
    #     elevation_profile


def get_diameter(root, file):
    table = DBF(f'{root}\\{file}', load=True)
    diameter = table.records[0]['DIAM']
    return diameter #float

def get_thickness(root, file, diameter):
    row = 0
    temp_list = []
    table = DBF(f'{root}\\{file}', load=True)
    for _ in table:
        thickness = formula_determination(diameter, table.records[0 + row]['DISTANCE'])
        temp_list.append(thickness)
        row += 1
    return temp_list



#>> > table = DBF('people.dbf', load=True)
#>> > print(table.records[1]['NAME'])
#Bob


# determination of formula
def formula_determination(diameter, distance):
    if diameter < 45.0:
        thickness = sharpton(diameter, distance)
    elif diameter >= 45.0 and diameter <= 300.0:
        thickness = housen(diameter, distance)
    else:
        thickness = faset(diameter, distance)
    return thickness

# Sharpton - <45 km
def sharpton(diameter, distance):
    thickness = 3.95 * ((diameter * 500) ** 0.399) * (distance / (diameter * 500)) ** -3.0
    return thickness


# Hausen - 45-300 km
def housen(diameter, distance):
    thickness = 0.0078 * (diameter * 500) * (distance / (diameter * 500)) ** -2.61
    return thickness


# Faset - >300 km
def faset(diameter, distance):
    thickness = 2900.0 * (distance / (diameter * 500)) ** -2.8
    return thickness



    #     if temp_list:
    #         temp_list = map(sum, zip(temp_list, reworking_data(file, root)))
    #     else:
    #         temp_list = reworking_data(file, root)
    # temp_list = list(map(lambda x, y: x - y, elevation_profile, temp_list))
    # for num in range(len(temp_list)):
    #     xz_list.append(num * 1000)
    # return temp_list, xz_list





# def reworking_data(file, root):
#     row = 0
#     temp_list = []
#     table = DBF(f'{root}\{file}', load=True)
#     diameter = table.records[0]['DIAM']  ######
#     for _ in table:
#         thickness = formula_determination(diameter, table.records[0 + row]['DISTANCE'])
#         temp_list.append(thickness)
#         row += 1
#     return temp_list







# def search_layers(elevation_profile):
#     file_from_dirs = []
#     for x in range(count_of_dir):
#         print(x)
#
#         file_from_dirs.append(search_layer(elevation_profile, x))
#     return layers_points, number_of_laypoints


# def dir_number():
#     path = os.path.abspath('../test/geological_crossections/data/layers/')
#     num_files = len([f for f in os.listdir(path)
#                      if os.path.isfile(os.path.join(path, f))])
#     return num_files
