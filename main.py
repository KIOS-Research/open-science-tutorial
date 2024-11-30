from epyt import epanet
import os

import argparse
import os


def main(*args):
    # Initialize the argument parser
    parser = argparse.ArgumentParser(description="Process input parameters.")

    # Define the expected parameter with a default value
    parser.add_argument('--inpname', type=int, default=1,
                        help="Inpname (default: Net1.inp).")

    # Manually process '--node_indices=' format if passed as positional args
    processed_args = []
    for arg in args:
        if arg.startswith('--inpname='):
            key, value = arg.split('=', 1)
            processed_args.extend([key, value])
        else:
            processed_args.append(arg)

    # Parse the arguments
    parsed_args = parser.parse_args(processed_args)

    # Retrieve the parsed value
    inpname = parsed_args.inpname
    print(inpname)

    # Add all subdirectories of the current working directory to sys.path
    for root, dirs, files in os.walk(os.getcwd()):
        if root not in os.sys.path:
            os.sys.path.append(root)

    print("Paths Loaded.")


# Example usage
if __name__ == "__main__":
    import sys

    main(*sys.argv[1:])

    filename = 'data/Net1.inp'
    G = epanet(filename)
    print(G.InputFile)
    print(G.TempInpFile)
    h = G.plot()
    h.savefig('results/test.png')