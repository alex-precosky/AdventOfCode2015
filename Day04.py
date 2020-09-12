# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 22:41:17 2015

@author: Alex
"""

import hashlib
import binascii

# find hex MD5 hashes that start with at least five zeroes


# input for the hash is a decimal number and a key
# find lowest number to produce such a hash
def count_leading_zeros_in_hash(hash):
    num_leading_zeros = 0

    for char in hash:
        if char == "0":
            num_leading_zeros += 1
        else:
            break

    return num_leading_zeros


def generate_hash(key):
    m = hashlib.md5()
    m.update(key.encode("utf-8"))
    hash = m.digest()
    hash = str(binascii.hexlify(hash)).strip("b'")

    return hash


def find_md5_with_n_leading_zeros(key, num_leading_zeros):

    i = 0
    hash_found = False

    while not hash_found:
        value_to_hash = (key + str(i))

        hash = generate_hash(value_to_hash)

        if count_leading_zeros_in_hash(hash) >= num_leading_zeros:
            hash_found = True
        else:
            i += 1

    return i


if __name__ == "__main__":
    part1 = find_md5_with_n_leading_zeros("iwrupvqb", 5)
    print("Part1. The number is: %d" % part1)

    part2 = find_md5_with_n_leading_zeros("iwrupvqb", 6)
    print("Part2. The number is: %d" % part2)
