from .loader import profile_layers
import argparse

def parser():
    parser = argparse.ArgumentParser(
                    prog = 'ProgramName',
                    description = 'What the program does',
                    epilog = 'Text at the bottom of help')

    parser.add_argument('datadir')           # positional argument
    args = parser.parse_args()
    return args

def main():
    args = parser()

    if args.datadir is not None:
        profile_layers(args.datadir)
