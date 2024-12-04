from epyt import epanet
import os

import argparse
import os


def main(*args):
    # Initialize the argument parser
    parser = argparse.ArgumentParser(description="Process input parameters.")

    # Define the expected parameter with a default value
    parser.add_argument('--inpname', type=str, default='Net1',
                        help="Inpname (default: Net1.inp).")
    print(11)

    processed_args = []
    print(args)
    for arg in args:
        if arg.startswith('--inpname='):
            key, value = arg.split('=', 1)
            processed_args.extend([key, value])
        else:
            print(arg)
            break

    G = epanet(arg + '.inp')
    h = G.plot()
    h.savefig('../results/test.png')

    # Add all subdirectories of the current working directory to sys.path
    for root, dirs, files in os.walk(os.getcwd()):
        if root not in os.sys.path:
            os.sys.path.append(root)

    print("Paths Loaded.")


# Example usage
if __name__ == "__main__":
    import sys

    main(*sys.argv[1:])    
