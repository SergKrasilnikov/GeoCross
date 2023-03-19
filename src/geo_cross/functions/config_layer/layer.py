import os
from dbfread import DBF
import os.path
from .formula import *


def get_layer(elevation_profile, datadir):
    final_elevations = []
    for folder in reversed(range(len(next(os.walk(os.path.join(datadir, 'layers')))[1]))):
        final_elevations.append((search_layers(folder, elevation_profile, datadir)).copy())
    return final_elevations


def search_layers(dir_name, elevation_profile, datadir): # name of the directory
    dbf_list = []
    for root, dirs, files in os.walk(os.path.join(datadir, fr'layers\{dir_name}')):
        for file in files:
            if file.endswith(".dbf"):
                dbf_list.append(file)
    return get_layers_data(root, dbf_list, elevation_profile, datadir)


def get_layers_data(root, files_list, elevation_profile, datadir): # get data from the file
    for file in files_list:
        diameter = get_diameter(root, file)
        layer_thickness, layers_dict = get_thickness(root, file, diameter) # list with thickness data
        create_thickness_report(layers_dict, datadir)
        for index in range(len(elevation_profile)):
            elevation_profile[index] -= layer_thickness[index]
    return elevation_profile

def get_diameter(root, file):
    table = DBF(os.path.join(root,file), load=True)
    diameter = table.records[0]['DIAM']
    return diameter # float

def get_thickness(root, file, diameter, layers_dict={}):
    row = 0
    temp_list = []
    table = DBF(os.path.join(root, file), load=True)
    layer_num = ''
    if layer_num != file:
        for letter in file:
            if letter != '.':
                layer_num += letter
            else:
                break

    min_elevation = 9999
    max_elevation = 0
    for _ in table:
        thickness = round(formula_determination(diameter, table.records[0 + row]['DISTANCE']), 2)
        temp_list.append(thickness)
        if thickness < min_elevation:
          min_elevation = thickness
        if thickness > max_elevation:
            max_elevation = thickness
        row += 1
    layers_dict[layer_num] = {'min': min_elevation, 'max': max_elevation}

    return temp_list, layers_dict

def create_thickness_report(layers_dict, datadir):
    with open(fr'{datadir}/output/thickness_report.txt', 'w') as file:
        for key, value in layers_dict.items():
            file.write('%s:%s\n' % (key, value))
