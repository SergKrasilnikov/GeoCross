from .loader import profile_layers
import argparse

def parser():
    parser = argparse.ArgumentParser(
                    prog = 'geocross',
                    description = 'Description: '
                                  'This program builds geological crosssections of the ejecta deposits on the Moon '
                                  'based on the models: Sharpton (2014), Housen et al., (1983) and  Fassett et al., '
                                  '(2011). '
                                  'The program has a data folder and an src folder. '
                                  'The data folder: folder with elevation - profile.dbf file with data of elevation '
                                  'every 100 m (based on LOLA 20 m/pix data); '
                                  'folder with layers - starts from the lower layer/layers at the zero folder until '
                                  'upper layer at the latest number; output - profiles in .jpg and .svg formats will '
                                  'be saved in this folder. '
                                  'The src folder: run.py is used to run this code (see the section "To run this '
                                  'code").'
                                  'main.py - parser and call of the loader. '
                                  'loader.py - call functions from different directories. '
                                  'profile.py (config_profile folder) - making a list with the data from the '
                                  'profile.dbf. '
                                  'layer.py - config each layer of ejecta from new (higher numbers in layers folder) '
                                  'to the older one (lover numbers). The thickness of each layer is calculated based '
                                  'on models in formula.py and minus from elevation of the profile or previous layer. '
                                  'formula.py - automatically determines the model for each layer\'s thickness '
                                  'calculation. Each model is based on crater diameter. '
                                  'plot.py (plotting folder) - parameters for plotting of elevation profile and '
                                  'thickness of ejecta deposits.',
                    epilog = 'To run this code: python run.py \'ABSOLUTE LOCATION OF THE \'data\' DIRECTORY\'')

    parser.add_argument('datadir')           # positional argument
    args = parser.parse_args()
    return args

def main():
    args = parser()

    if args.datadir is not None:
        profile_layers(args.datadir)
