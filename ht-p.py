#!/usr/bin/env python3
"""Calculate hardness and elastic modulus from UMIS output."""

import argparse

from matplotlib import pyplot as plt
import numpy


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "loadfile",
        type=argparse.FileType("rb"),
        help="UMIS output file containing penetration and load data",
    )
    args = parser.parse_args()

    i, h, P = numpy.genfromtxt(
        args.loadfile,
        delimiter=",",
        skip_header=1,
        usecols=(0,1, 2),
        unpack=True,
    )

    # i: indent
    # h: penetration
    # P: load

    plt.plot(h, P, "k.")
    plt.ylabel("Load (mN)")
    plt.xlabel("Penetration depth (um)")

    plt.show()

if __name__ == "__main__":
    main()
