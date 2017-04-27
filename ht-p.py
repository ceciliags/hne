#!/usr/bin/env python3
"""Calculate hardness and elastic modulus from UMIS output."""

import argparse
from itertools import groupby, islice
from operator import itemgetter

from matplotlib import pyplot as plt


def parseline(line):
    indent, depth, load = line.split(",")
    return (indent, float(depth), float(load))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "loadfile",
        type=argparse.FileType("r"),
        help="UMIS output file containing penetration and load data",
    )
    args = parser.parse_args()

    lines = islice(args.loadfile, 1, None)
    data = map(parseline, lines)
    for indent, subdata in groupby(data, itemgetter(0)):
        _, depth, load = zip(*subdata)
        plt.plot(depth, load)

    plt.xlabel("Penetration depth (um)")
    plt.ylabel("Load (mN)")

    plt.show()


if __name__ == "__main__":
    main()
