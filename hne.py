#!/usr/bin/env python3
"""Calculate hardness and elastic modulus from UMIS output."""

import argparse

from matplotlib import pyplot as plt
import numpy


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "hardnessfile",
        type=argparse.FileType("rb"),
        help="UMIS output file containing penetration and hardness data",
    )
    parser.add_argument(
        "elasticmodulusfile",
        type=argparse.FileType("rb"),
        help="UMIS output file containing penetration and elastic "
        "modulus data",
    )
    args = parser.parse_args()

    h, H = numpy.genfromtxt(
        args.hardnessfile,
        delimiter=",",
        skip_header=1,
        usecols=(1, 2),
        unpack=True,
    )

    E = numpy.genfromtxt(
        args.elasticmodulusfile,
        delimiter=",",
        skip_header=1,
        usecols=(2,),
        # unpack=True,
    )

    meanH = numpy.mean(H)
    stdH = numpy.std(H)
    meanE = numpy.mean(E)
    stdE = numpy.std(E)

    maskedH = numpy.ma.masked_outside(H, meanH - 3 * stdH, meanH + 3 * stdH)
    maskedE = numpy.ma.masked_outside(E, meanE - 3 * stdE, meanE + 3 * stdE)
    mask = numpy.ma.mask_or(maskedH.mask, maskedE.mask)
    maskedH.mask = maskedE.mask = mask
    maskedh = numpy.ma.array(h, mask=mask)

    print("mean hardness:", numpy.mean(maskedH))
    print("hardness standard deviation:", numpy.std(maskedH))
    print("mean elastic modulus:", numpy.mean(maskedE))
    print("elastic modulus standard deviation:", numpy.std(maskedE))

    plt.subplot(2, 1, 1)
    plt.plot(maskedh, maskedH, "k+")
    plt.ylabel("Hardness (GPa)")

    plt.subplot(2, 1, 2)
    plt.plot(maskedh, maskedE, "k.")
    plt.ylabel("Elastic modulus (GPa)")
    plt.xlabel("Penetration depth (nm)")

    plt.show()

if __name__ == "__main__":
    main()
